import os
import json
import argparse
import urllib.request
import urllib.error

def create_label(repo, token, name, color):
    url = f"https://api.github.com/repos/{repo}/labels"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = json.dumps({"name": name, "color": color}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        if e.code != 422: # 422 means label already exists, which is fine
            print(f"Failed to create label {name}: {e.read().decode()}")

def push_issues(repo, file_path):
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN environment variable not set.")
        return

    # Setup standard labels
    labels = {"frontend": "1D76DB", "backend": "0E8A16", "angular-material": "DD0031", "python": "3572A5", "migration": "FBCA04"}
    for name, color in labels.items():
        create_label(repo, token, name, color)

    with open(file_path, 'r') as f:
        issues = json.load(f)

    url = f"https://api.github.com/repos/{repo}/issues"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    for issue in issues:
        data = json.dumps({
            "title": issue["title"],
            "body": issue["body"],
            "labels": issue["labels"]
        }).encode('utf-8')
        
        req = urllib.request.Request(url, data=data, headers=headers, method='POST')
        try:
            response = urllib.request.urlopen(req)
            res_data = json.loads(response.read().decode())
            print(f"Created Issue #{res_data['number']}: {issue['title']}")
        except urllib.error.HTTPError as e:
            print(f"Failed to create issue: {e.read().decode()}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True, help="GitHub repo (owner/name)")
    parser.add_argument("--file", required=True, help="Path to drafted_issues.json")
    args = parser.parse_args()
    push_issues(args.repo, args.file)
