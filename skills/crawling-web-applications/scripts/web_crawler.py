#!/usr/bin/env python3
"""
Baseline Link & UI Element Crawler for Web Application Auditing.
This script is a zero-dependency, pure Python tool to systematically crawl a target
web application, check HTTP statuses of all internal and external links, catalog forms,
and identify semantic and imposter buttons.
"""

import argparse
import json
import ssl
import sys
import time
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen


class WebAppParser(HTMLParser):
    """
    Parser to extract links, titles, forms, inputs, buttons,
    and button-like elements from HTML content.
    """
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.title = ""
        self.in_title = False
        self.links = []
        self.buttons = []
        self.forms = []
        self.current_form = None
        
        # Track current state for extracting text of elements
        self.active_element = None
        self.temp_element_text = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        # Track title tag
        if tag == "title":
            self.in_title = True
            return

        # Extract links
        if tag == "a" and "href" in attrs_dict:
            href = attrs_dict["href"].strip()
            # Resolve relative URLs
            resolved_url = urljoin(self.base_url, href)
            # Remove hash/fragments for crawling purposes, but record if it is a hash link
            parsed_resolved = urlparse(resolved_url)
            clean_url = parsed_resolved._replace(fragment="").geturl()
            
            self.links.append({
                "raw_href": href,
                "resolved_url": clean_url,
                "is_fragment": href.startswith("#"),
                "is_javascript": href.lower().startswith("javascript:"),
                "text": ""  # Will be populated in handle_data
            })
            self.active_element = {"type": "link", "index": len(self.links) - 1}
            self.temp_element_text = ""

        # Extract semantic buttons
        elif tag == "button" or (tag == "input" and attrs_dict.get("type") in ["button", "submit", "reset"]):
            btn_type = attrs_dict.get("type", "button") if tag == "input" else "button"
            btn_text = attrs_dict.get("value", "") if tag == "input" else ""
            self.buttons.append({
                "tag": tag,
                "is_semantic": True,
                "type": btn_type,
                "text": btn_text,
                "class": attrs_dict.get("class", ""),
                "id": attrs_dict.get("id", ""),
                "role": attrs_dict.get("role", "button")
            })
            if tag == "button":
                self.active_element = {"type": "button", "index": len(self.buttons) - 1}
                self.temp_element_text = ""

        # Extract imposter buttons (non-semantic elements acting or looking like buttons)
        elif tag in ["div", "span", "a"]:
            classes = attrs_dict.get("class", "").lower()
            role = attrs_dict.get("role", "").lower()
            
            # Look for button indicators in classes or roles
            is_imposter = (
                role == "button" or
                any(indicator in classes for indicator in ["btn", "button", "clickable", "touchable"])
            )
            
            # Avoid duplicating standard links that are styled like buttons as separate links
            # (they will be captured as links, but we also flag them here as imposter buttons)
            if is_imposter:
                self.buttons.append({
                    "tag": tag,
                    "is_semantic": False,
                    "type": "imposter",
                    "text": "",
                    "class": attrs_dict.get("class", ""),
                    "id": attrs_dict.get("id", ""),
                    "role": role,
                    "href_attribute": attrs_dict.get("href", None)
                })
                self.active_element = {"type": "imposter", "index": len(self.buttons) - 1}
                self.temp_element_text = ""

        # Track forms and their fields
        elif tag == "form":
            self.current_form = {
                "action": attrs_dict.get("action", ""),
                "method": attrs_dict.get("method", "get").upper(),
                "id": attrs_dict.get("id", ""),
                "inputs": []
            }
            self.forms.append(self.current_form)

        elif tag in ["input", "textarea", "select"] and self.current_form is not None:
            self.current_form["inputs"].append({
                "tag": tag,
                "name": attrs_dict.get("name", ""),
                "type": attrs_dict.get("type", "text") if tag == "input" else tag,
                "id": attrs_dict.get("id", ""),
                "required": "required" in attrs_dict
            })

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        
        elif tag == "form":
            self.current_form = None

        elif self.active_element:
            element_type = self.active_element["type"]
            idx = self.active_element["index"]
            clean_text = " ".join(self.temp_element_text.split())
            
            if element_type == "link":
                self.links[idx]["text"] = clean_text
            elif element_type == "button":
                if not self.buttons[idx]["text"]:  # Only override if not already set (e.g. from input value)
                    self.buttons[idx]["text"] = clean_text
            elif element_type == "imposter":
                self.buttons[idx]["text"] = clean_text
                
            self.active_element = None

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        elif self.active_element:
            self.temp_element_text += data


class WebCrawler:
    def __init__(self, start_url, max_depth=3, timeout=10, user_agent=None, form_inputs=None):
        self.start_url = start_url
        self.max_depth = max_depth
        self.timeout = timeout
        self.user_agent = user_agent or "Mozilla/5.0 (Compatible; MercilessQACrawler/1.0)"
        self.form_inputs = form_inputs or {}
        self.submitted_forms = set()  # Track (action_url, input_names_tuple)
        
        parsed_start = urlparse(start_url)
        self.allowed_netloc = parsed_start.netloc
        self.scheme = parsed_start.scheme
        
        # Crawl results
        self.visited_urls = set()
        self.pages_data = {}
        self.link_statuses = {}  # URL -> {status, content_type, error}
        
        # Bypass SSL verification issues for localhost or staging sites
        self.ssl_context = ssl._create_unverified_context()

    def get_request(self, url, method="GET"):
        req = Request(url, method=method)
        req.add_header("User-Agent", self.user_agent)
        return req

    def encode_multipart(self, fields, files):
        """
        Encodes form fields and file uploads into a standard multipart/form-data payload.
        """
        boundary = f"---FormBoundary{str(time.time())}"
        CRLF = b"\r\n"
        parts = []
        
        for name, value in fields.items():
            parts.append(f'--{boundary}'.encode('utf-8'))
            parts.append(f'Content-Disposition: form-data; name="{name}"'.encode('utf-8'))
            parts.append(b'')
            parts.append(str(value).encode('utf-8'))
            
        for name, file_info in files.items():
            filename = "uploaded_file"
            file_content = b"dummy content"
            
            if isinstance(file_info, dict):
                filename = file_info.get("filename", filename)
                content = file_info.get("content", "")
                file_content = content.encode('utf-8') if isinstance(content, str) else content
            elif isinstance(file_info, str):
                import os
                filename = os.path.basename(file_info)
                try:
                    with open(file_info, "rb") as f:
                        file_content = f.read()
                except Exception:
                    file_content = b"dummy file content"
                    
            parts.append(f'--{boundary}'.encode('utf-8'))
            parts.append(f'Content-Disposition: form-data; name="{name}"; filename="{filename}"'.encode('utf-8'))
            parts.append(b'Content-Type: application/octet-stream'.encode('utf-8'))
            parts.append(b'')
            parts.append(file_content)
            
        parts.append(f'--{boundary}--'.encode('utf-8'))
        parts.append(b'')
        body = CRLF.join(parts)
        content_type = f'multipart/form-data; boundary={boundary}'
        return content_type, body

    def submit_form(self, form, parent_url, depth):
        """
        Processes a form, maps user/LLM-provided inputs, builds the HTTP request,
        and crawls the resulting page.
        """
        action = form.get("action", "")
        method = form.get("method", "GET").upper()
        form_id = form.get("id", "")
        
        # Resolve action URL relative to parent URL
        action_url = urljoin(parent_url, action)
        
        # Gather inputs
        fields = {}
        files = {}
        has_file_input = False
        
        for input_field in form.get("inputs", []):
            name = input_field.get("name")
            if not name:
                continue
                
            input_type = input_field.get("type", "text")
            
            # Match input in user provided mapping
            value = self.form_inputs.get(name)
            if value is None and form_id:
                # Also try matching by scoped ID: form_id.input_name
                value = self.form_inputs.get(f"{form_id}.{name}")
                
            if value is None:
                value = ""
                if input_field.get("required"):
                    print(f"  [Warning] Required input '{name}' in form '{form_id}' has no matching value in --form-inputs.", file=sys.stderr)
            
            if input_type == "file":
                has_file_input = True
                if value:
                    files[name] = value
            else:
                fields[name] = value

        # To prevent infinite loops, check if we've already submitted this form setup
        submission_key = (action_url, tuple(sorted(list(fields.keys()) + list(files.keys()))))
        if submission_key in self.submitted_forms:
            return
        self.submitted_forms.add(submission_key)

        print(f"[Form Submit] Method: {method} | Action: {action_url}", file=sys.stderr)

        try:
            if method == "POST":
                req = Request(action_url, method="POST")
                req.add_header("User-Agent", self.user_agent)
                
                if has_file_input:
                    content_type, body = self.encode_multipart(fields, files)
                    req.add_header("Content-Type", content_type)
                    req.data = body
                else:
                    from urllib.parse import urlencode
                    data = urlencode(fields).encode("utf-8")
                    req.add_header("Content-Type", "application/x-www-form-urlencoded")
                    req.data = data
            else:
                # GET request: append fields to query params
                from urllib.parse import parse_qsl, urlencode, urlunparse
                parsed_action = urlparse(action_url)
                query_params = parse_qsl(parsed_action.query)
                query_params.extend(fields.items())
                new_query = urlencode(query_params)
                action_url = urlunparse(parsed_action._replace(query=new_query))
                
                req = self.get_request(action_url, method="GET")

            # Execute the request
            with urlopen(req, timeout=self.timeout, context=self.ssl_context) as response:
                result_url = response.geturl()
                html_bytes = response.read()
                charset = response.info().get_content_charset() or "utf-8"
                html_content = html_bytes.decode(charset, errors="ignore")
                
                status_code = response.getcode()
                self.link_statuses[action_url] = {
                    "status": status_code,
                    "content_type": response.info().get_content_type(),
                    "error": None,
                    "parents": {parent_url},
                    "is_internal": urlparse(action_url).netloc == self.allowed_netloc
                }
                
                if result_url != action_url:
                    self.link_statuses[result_url] = {
                        "status": status_code,
                        "content_type": response.info().get_content_type(),
                        "error": None,
                        "parents": {parent_url},
                        "is_internal": urlparse(result_url).netloc == self.allowed_netloc
                    }

                # Parse resulting HTML
                parser = WebAppParser(result_url)
                parser.feed(html_content)
                
                # Store resulting page
                page_data = {
                    "title": parser.title.strip(),
                    "url": result_url,
                    "depth": depth + 1,
                    "status": status_code,
                    "links": parser.links,
                    "buttons": parser.buttons,
                    "forms": parser.forms,
                    "is_form_submission_result": True,
                    "submitted_form_id": form_id
                }
                self.pages_data[result_url] = page_data
                self.visited_urls.add(result_url)
                
                # Recurse from the resulting page
                for link_info in parser.links:
                    resolved_url = link_info["resolved_url"]
                    is_internal = urlparse(resolved_url).netloc == self.allowed_netloc
                    link_status = self.check_link_status(resolved_url, parent_url=result_url)
                    
                    if is_internal and resolved_url not in self.visited_urls and (depth + 1) < self.max_depth:
                        if link_status["status"] == 200 and (not link_status["content_type"] or "html" in link_status["content_type"]):
                            self.crawl_page(resolved_url, depth + 2)
                            
        except Exception as e:
            print(f"  [Error] Form submission failed: {e}", file=sys.stderr)
            self.link_statuses[action_url] = {
                "status": "FORM_SUBMISSION_FAILED",
                "content_type": None,
                "error": str(e),
                "parents": {parent_url},
                "is_internal": urlparse(action_url).netloc == self.allowed_netloc
            }

    def check_link_status(self, url, parent_url=None):
        """
        Pings a URL with a HEAD request (or GET fallback) to determine if it is alive.
        """
        if url in self.link_statuses:
            if parent_url:
                self.link_statuses[url]["parents"].add(parent_url)
            return self.link_statuses[url]

        result = {
            "status": None,
            "content_type": None,
            "error": None,
            "parents": {parent_url} if parent_url else set(),
            "is_internal": urlparse(url).netloc == self.allowed_netloc
        }

        # Handle javascript / local fragments directly without network calls
        if url.lower().startswith("javascript:") or url.startswith("#") or not url.startswith("http"):
            result["status"] = "N/A (Non-navigable)"
            self.link_statuses[url] = result
            return result

        try:
            # Try HEAD request first for efficiency
            req = self.get_request(url, method="HEAD")
            with urlopen(req, timeout=self.timeout, context=self.ssl_context) as response:
                result["status"] = response.getcode()
                result["content_type"] = response.info().get_content_type()
        except HTTPError as e:
            result["status"] = e.code
            result["error"] = str(e)
        except Exception as e:
            # Fall back to GET if HEAD failed or is blocked
            try:
                req = self.get_request(url, method="GET")
                with urlopen(req, timeout=self.timeout, context=self.ssl_context) as response:
                    result["status"] = response.getcode()
                    result["content_type"] = response.info().get_content_type()
            except HTTPError as e:
                result["status"] = e.code
                result["error"] = str(e)
            except URLError as e:
                result["status"] = "CONNECTION_FAILED"
                result["error"] = str(e.reason)
            except Exception as ex:
                result["status"] = "ERROR"
                result["error"] = str(ex)

        self.link_statuses[url] = result
        return result

    def crawl_page(self, url, depth=0):
        if url in self.visited_urls or depth > self.max_depth:
            return
        
        print(f"[Crawl] Depth {depth}: {url}", file=sys.stderr)
        self.visited_urls.add(url)
        
        # Verify page status
        status_info = self.check_link_status(url)
        if status_info["status"] != 200:
            print(f"  [Error] Page status: {status_info['status']}", file=sys.stderr)
            return

        # Fetch page HTML
        try:
            req = self.get_request(url, method="GET")
            with urlopen(req, timeout=self.timeout, context=self.ssl_context) as response:
                html_bytes = response.read()
                # Try to decode
                charset = response.info().get_content_charset() or "utf-8"
                html_content = html_bytes.decode(charset, errors="ignore")
        except Exception as e:
            print(f"  [Error] Failed to read page HTML: {e}", file=sys.stderr)
            return

        # Parse HTML
        parser = WebAppParser(url)
        parser.feed(html_content)

        page_data = {
            "title": parser.title.strip(),
            "url": url,
            "depth": depth,
            "status": status_info["status"],
            "links": parser.links,
            "buttons": parser.buttons,
            "forms": parser.forms
        }
        self.pages_data[url] = page_data

        # Process found forms (auto-submit if matched inputs exist)
        for form in parser.forms:
            if self.form_inputs:
                has_matching_inputs = any(
                    inp.get("name") in self.form_inputs or f"{form.get('id')}.{inp.get('name')}" in self.form_inputs
                    for inp in form.get("inputs", []) if inp.get("name")
                )
                if has_matching_inputs:
                    self.submit_form(form, url, depth)

        # Process found links
        for link_info in parser.links:
            resolved_url = link_info["resolved_url"]
            is_internal = urlparse(resolved_url).netloc == self.allowed_netloc
            
            # Check link validity
            link_status = self.check_link_status(resolved_url, parent_url=url)
            
            # Recurse if internal, not visited, and within depth limit
            if is_internal and resolved_url not in self.visited_urls and depth < self.max_depth:
                # Ensure it's HTML content before crawling
                if link_status["status"] == 200 and (not link_status["content_type"] or "html" in link_status["content_type"]):
                    self.crawl_page(resolved_url, depth + 1)

    def run(self):
        self.crawl_page(self.start_url, depth=0)
        
        # Clean up sets for JSON serialization
        serializable_statuses = {}
        for k, v in self.link_statuses.items():
            serializable_statuses[k] = {
                "status": v["status"],
                "content_type": v["content_type"],
                "error": v["error"],
                "is_internal": v["is_internal"],
                "parents": list(v["parents"])
            }

        return {
            "start_url": self.start_url,
            "domain": self.allowed_netloc,
            "total_pages_crawled": len(self.visited_urls),
            "pages": self.pages_data,
            "link_statuses": serializable_statuses
        }


def print_cli_summary(results):
    pages = results["pages"]
    statuses = results["link_statuses"]
    
    print("\n" + "="*60)
    print("               MERCILESS QA CRAWLER SUMMARY")
    print("="*60)
    print(f"Start URL: {results['start_url']}")
    print(f"Pages Audited: {results['total_pages_crawled']}")
    
    working_links = 0
    broken_links = []
    
    for url, info in statuses.items():
        if info["status"] == 200:
            working_links += 1
        elif isinstance(info["status"], int) and info["status"] >= 400:
            broken_links.append((url, info["status"], info["parents"]))
        elif info["status"] in ["CONNECTION_FAILED", "ERROR"]:
            broken_links.append((url, f"FAILED ({info['error']})", info["parents"]))

    print(f"Total Unique Links Checked: {len(statuses)}")
    print(f"  - Working (200 OK): {working_links}")
    print(f"  - Broken/Failing: {len(broken_links)}")
    
    if broken_links:
        print("\n[!] BROKEN LINKS DETECTED:")
        for url, err, parents in broken_links:
            print(f"  - {url} (Status: {err})")
            print(f"    Parent Pages: {', '.join(parents)}")
            
    # Count imposter buttons
    imposter_count = 0
    total_buttons = 0
    for page_url, p_data in pages.items():
        total_buttons += len(p_data["buttons"])
        imposter_count += sum(1 for b in p_data["buttons"] if not b["is_semantic"])

    print(f"\nUI Buttons Detected: {total_buttons}")
    print(f"  - Semantic <button> / Inputs: {total_buttons - imposter_count}")
    print(f"  - Imposter divs/spans (A11Y Alerts): {imposter_count}")
    
    if imposter_count > 0:
        print("\n[!] IMPOSTER BUTTONS DETECTED (No Semantic <button> Tag):")
        for page_url, p_data in pages.items():
            imposters = [b for b in p_data["buttons"] if not b["is_semantic"]]
            if imposters:
                print(f"  On page {page_url}:")
                for imp in imposters:
                    print(f"    - Tag: <{imp['tag']}> | Class: '{imp['class']}' | Text: '{imp['text']}'")
    print("="*60 + "\n")


def main():
    parser = argparse.ArgumentParser(description="Merciless Web Application QA Crawler")
    parser.add_argument("--url", required=True, help="Starting URL to crawl (e.g. http://localhost:3000)")
    parser.add_argument("--max-depth", type=int, default=3, help="Maximum depth of links to crawl (default: 3)")
    parser.add_argument("--timeout", type=int, default=10, help="HTTP timeout in seconds (default: 10)")
    parser.add_argument("--output-json", help="Path to write the detailed JSON crawl report")
    parser.add_argument("--user-agent", help="Custom User-Agent header")
    parser.add_argument("--form-inputs", help="JSON string or path to JSON file containing form inputs mapping (e.g. '{\"username\": \"admin\", \"resume_upload\": \"/path/to/resume.pdf\"}')")
    
    args = parser.parse_args()
    
    form_inputs = {}
    if args.form_inputs:
        try:
            # Try parsing as inline JSON first
            form_inputs = json.loads(args.form_inputs)
        except json.JSONDecodeError:
            # Try reading as file path
            try:
                with open(args.form_inputs, "r", encoding="utf-8") as f:
                    form_inputs = json.load(f)
            except Exception as e:
                print(f"Error loading --form-inputs: {e}", file=sys.stderr)
                sys.exit(1)
                
    crawler = WebCrawler(
        start_url=args.url,
        max_depth=args.max_depth,
        timeout=args.timeout,
        user_agent=args.user_agent,
        form_inputs=form_inputs
    )
    
    try:
        results = crawler.run()
    except Exception as e:
        print(f"Fatal crawling error: {e}", file=sys.stderr)
        sys.exit(1)
        
    if args.output_json:
        try:
            with open(args.output_json, "w", encoding="utf-8") as f:
                json.dump(results, f, indent=2)
            print(f"Detailed crawl logs written to: {args.output_json}", file=sys.stderr)
        except Exception as e:
            print(f"Failed to write output JSON: {e}", file=sys.stderr)

    print_cli_summary(results)


if __name__ == "__main__":
    main()
