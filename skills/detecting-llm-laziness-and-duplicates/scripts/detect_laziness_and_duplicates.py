#!/usr/bin/env python3
"""
detect_laziness_and_duplicates.py

A local QCO (Quality Control Oracle) parser to scan a codebase for LLM defects:
1. Laziness Markers: Ellipses comments, stub abbreviations, or shortcut indicators (e.g., '// ... rest of code stays the same').
2. TODO / FIXME annotations.
3. Code Duplication: Identical blocks of code across the repository (using diagonal-merging clone detection).

Outputs a lightweight, structured JSON/Markdown report to avoid bloating the LLM's context window.
"""

import os
import re
import json
import argparse
import hashlib
from collections import defaultdict

# Supported file extensions for analysis
SUPPORTED_EXTENSIONS = {
    '.js', '.jsx', '.ts', '.tsx', '.py', '.java', '.go', '.rb', '.rs',
    '.cpp', '.h', '.c', '.cs', '.sh', '.php', '.swift', '.kt', '.scala', '.m'
}

# Directories to skip during scanning
IGNORE_DIRS = {
    '.git', 'node_modules', 'venv', 'env', '.venv', '__pycache__',
    '.next', '.nuxt', 'dist', 'build', 'target', 'out', 'coverage',
    '.idea', '.vscode'
}

# Regex patterns for laziness & placeholder markers
LAZINESS_PATTERNS = [
    (r'(?i)//\s*\.\.\.\s*$', 'ellipses_comment', "Ellipses indicating omitted code (e.g. '// ...')"),
    (r'(?i)#\s*\.\.\.\s*$', 'ellipses_comment', "Ellipses indicating omitted code (e.g. '# ...')"),
    (r'(?i)/\*?\s*\.\.\.\s*\*?/', 'ellipses_comment', "Block ellipses indicating omitted code (e.g. '/* ... */')"),
    (r'(?i)//\s*(?:rest\s+of\s+code|keep\s+existing|same\s+as\s+before|insert\s+here|your\s+code\s+here|logic\s+here|code\s+stays\s+the\s+same)', 'lazy_placeholder', "Lazy placeholder comment indicating omitted code"),
    (r'(?i)#\s*(?:rest\s+of\s+code|keep\s+existing|same\s+as\s+before|insert\s+here|your\s+code\s+here|logic\s+here|code\s+stays\s+the\s+same)', 'lazy_placeholder', "Lazy placeholder comment indicating omitted code"),
    (r'(?i)//\s*(?:\[previous\s+code\s+stays|code\s+remains|keep\s+other\s+imports)', 'lazy_placeholder', "Lazy placeholder comment indicating omitted code"),
    (r'(?i)#\s*(?:\[previous\s+code\s+stays|code\s+remains|keep\s+other\s+imports)', 'lazy_placeholder', "Lazy placeholder comment indicating omitted code"),
    (r'(?i)(?:NotImplementedError|NotImplementedException)', 'not_implemented_stub', "Explicit 'NotImplemented' stub exception"),
    (r'(?i)return\s+["\'](?:todo|placeholder|need\s+to\s+be\s+done|implemented)["\']', 'static_mock_return', "Static mock/placeholder return value"),
    (r'(?i)return\s+\[\s*(?:["\'][^"\']+["\']\s*,\s*){2,}["\'][^"\']+["\']\s*\]', 'static_mock_return', "Hard-coded static list return"),
    (r'(?i)return\s+\[\s*\{.*?\}\s*(?:,\s*\{.*?\})*\s*\]', 'static_mock_return', "Hard-coded static array of objects return"),
    (r'(?i)return\s+(?:\[\s*\]|\{\s*\})\s*;?\s*(?://|#)\s*(?:mock|dummy|stub|todo)', 'static_mock_return', "Empty mock/stub return with comment")
]

# Regex patterns for TODOs and FIXMEs
TODO_PATTERNS = [
    (r'(?i)//\s*(?:todo|fixme|need\s+to\s+be\s+done|to\s+be\s+done)', 'todo_comment', "Pending TODO/FIXME comment"),
    (r'(?i)#\s*(?:todo|fixme|need\s+to\s+be\s+done|to\s+be\s+done)', 'todo_comment', "Pending TODO/FIXME comment"),
    (r'(?i)/\*?\s*(?:todo|fixme|need\s+to\s+be\s+done|to\s+be\s+done)\b', 'todo_comment', "Pending TODO/FIXME block comment")
]

TRIVIAL_NORMALIZED = {
    '', '{', '}', '[', ']', '(', ')', ';', 'return;', 'pass', 'break', 'continue', 'else:', 'else', 'try:', 'finally:'
}

def normalize_line(line):
    """
    Remove comments, whitespace, and lowercase the line to perform structural clone matching.
    """
    # Remove single line comments
    line = re.sub(r'//.*', '', line)
    line = re.sub(r'#.*', '', line)
    # Strip whitespace and lowercase
    normalized = "".join(line.split()).lower()
    return normalized

def get_context(lines, target_idx, num_context=3):
    """
    Gets surrounding lines of context for a given index.
    """
    start = max(0, target_idx - num_context)
    end = min(len(lines), target_idx + num_context + 1)
    context = []
    for i in range(start, end):
        context.append({
            "line_num": i + 1,
            "text": lines[i].rstrip('\n'),
            "is_target": i == target_idx
        })
    return context

def scan_file_heuristics(filepath, lines, relative_path):
    """
    Scans a single file for laziness, placeholders, and TODOs.
    """
    laziness_findings = []
    todo_findings = []

    for idx, line in enumerate(lines):
        # 1. Check for Laziness Heuristics
        for pattern, category, desc in LAZINESS_PATTERNS:
            if re.search(pattern, line):
                # Ignore static mock returns in test files since they are expected
                if category == 'static_mock_return' and is_test_file(relative_path):
                    continue
                laziness_findings.append({
                    "file": relative_path,
                    "line_num": idx + 1,
                    "category": category,
                    "description": desc,
                    "matched_text": line.strip(),
                    "context": get_context(lines, idx)
                })
                break  # Record once per line

        # 2. Check for TODOs / FIXMEs
        for pattern, category, desc in TODO_PATTERNS:
            if re.search(pattern, line):
                todo_findings.append({
                    "file": relative_path,
                    "line_num": idx + 1,
                    "category": category,
                    "description": desc,
                    "matched_text": line.strip(),
                    "context": get_context(lines, idx)
                })
                break

    return laziness_findings, todo_findings

def is_test_file(filepath):
    """
    Determines if a file is likely a test file based on its path and name.
    """
    path_lower = filepath.lower()
    return ('/test/' in path_lower or 
            '/tests/' in path_lower or 
            '__tests__' in path_lower or 
            'test_' in os.path.basename(path_lower) or 
            '_test.' in os.path.basename(path_lower) or 
            '.test.' in os.path.basename(path_lower) or 
            '.spec.' in os.path.basename(path_lower))

def detect_clones(file_lines_map, min_dup_lines=6):
    """
    Detects structural clones across scanned files using a sliding window diagonal-merging technique.
    """
    # Build list of non-trivial normalized lines for each file
    # file_non_trivial[filepath] = list of (original_line_num, normalized_line, original_line_text)
    file_non_trivial = {}
    for filepath, lines in file_lines_map.items():
        non_trivial = []
        for idx, line in enumerate(lines):
            norm = normalize_line(line)
            if norm not in TRIVIAL_NORMALIZED and len(norm) > 2:
                non_trivial.append((idx + 1, norm, line.rstrip('\n')))
        file_non_trivial[filepath] = non_trivial

    # Build sliding window index
    # window_hash -> list of (filepath, start_index_in_non_trivial)
    window_index = defaultdict(list)
    window_size = 5  # Fixed sliding window size for hashing; duplicates will be merged to size >= min_dup_lines

    for filepath, non_trivial in file_non_trivial.items():
        if len(non_trivial) < window_size:
            continue
        for idx in range(len(non_trivial) - window_size + 1):
            window = tuple(item[1] for item in non_trivial[idx : idx + window_size])
            window_hash = hashlib.md5("".join(window).encode('utf-8')).hexdigest()
            window_index[window_hash].append((filepath, idx))

    # Identify matching pairs and offsets
    # key: (file_1, file_2, offset) -> value: list of starting indices in file_1
    matches_by_diagonal = defaultdict(list)

    for window_hash, locations in window_index.items():
        if len(locations) < 2:
            continue
        # Generate all unique pairs
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                loc1 = locations[i]
                loc2 = locations[j]
                
                f1, idx1 = loc1
                f2, idx2 = loc2

                # Enforce alphabetical order of file paths to merge (f1, f2) and (f2, f1)
                if f1 > f2:
                    f1, f2 = f2, f1
                    idx1, idx2 = idx2, idx1
                elif f1 == f2 and idx1 > idx2:
                    idx1, idx2 = idx2, idx1

                offset = idx2 - idx1
                matches_by_diagonal[(f1, f2, offset)].append(idx1)

    # Merge contiguous matches along each diagonal
    merged_clones = []

    for (f1, f2, offset), start_indices in matches_by_diagonal.items():
        # Sort starting indices to find contiguous runs
        start_indices = sorted(list(set(start_indices)))
        if not start_indices:
            continue

        runs = []
        current_run = [start_indices[0]]

        for idx in start_indices[1:]:
            if idx == current_run[-1] + 1:
                current_run.append(idx)
            else:
                runs.append(current_run)
                current_run = [idx]
        runs.append(current_run)

        # For each contiguous run, check if its length in non-trivial lines meets the min_dup_lines threshold
        for run in runs:
            run_length = len(run) + window_size - 1
            if run_length >= min_dup_lines:
                idx1_start = run[0]
                idx1_end = run[-1] + window_size - 1
                
                idx2_start = idx1_start + offset
                idx2_end = idx1_end + offset

                # Ignore duplicates if they are mock data within test files
                if is_test_file(f1) and is_test_file(f2):
                    continue

                # Get original line numbers
                orig_start_1 = file_non_trivial[f1][idx1_start][0]
                orig_end_1 = file_non_trivial[f1][idx1_end][0]

                orig_start_2 = file_non_trivial[f2][idx2_start][0]
                orig_end_2 = file_non_trivial[f2][idx2_end][0]

                # Extract preview code lines from f1
                preview_lines = []
                for item in file_non_trivial[f1][idx1_start : idx1_end + 1]:
                    preview_lines.append(f"{item[0]}: {item[2]}")

                merged_clones.append({
                    "file_a": f1,
                    "file_a_start": orig_start_1,
                    "file_a_end": orig_end_1,
                    "file_b": f2,
                    "file_b_start": orig_start_2,
                    "file_b_end": orig_end_2,
                    "duplicate_non_trivial_lines": run_length,
                    "code_preview": preview_lines[:15]  # Limit preview size in report
                })

    # Sort merged clones by size (descending)
    merged_clones.sort(key=lambda x: x["duplicate_non_trivial_lines"], reverse=True)
    return merged_clones

def write_markdown_report(report_data, output_path):
    """
    Formats the analysis findings into a human-readable Markdown report.
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# QCO (Quality Control Oracle) Code Defects Report\n\n")
        f.write("This report lists candidate code defects discovered via local heuristic analysis. ")
        f.write("Use this to selectively audit files without overflowing LLM context.\n\n")

        # Summary Table
        f.write("## Summary of Findings\n\n")
        f.write("| Category | Candidates Found |\n")
        f.write("| :--- | :---: |\n")
        f.write(f"| Laziness & Placeholders | {len(report_data['laziness_candidates'])} |\n")
        f.write(f"| Pending TODOs & FIXMEs | {len(report_data['todo_candidates'])} |\n")
        f.write(f"| Duplicate Code Blocks | {len(report_data['duplicate_blocks'])} |\n\n")

        # 1. Laziness Candidates
        f.write("## 1. Laziness & Placeholder Candidates\n")
        if not report_data['laziness_candidates']:
            f.write("No active laziness or placeholder stubs detected. Excellent!\n\n")
        else:
            for idx, item in enumerate(report_data['laziness_candidates']):
                f.write(f"### L-{idx+1}: {item['description']} in `{item['file']}`\n")
                f.write(f"* **File**: `{item['file']}` (Line {item['line_num']})\n")
                f.write(f"* **Matched Code**: `{item['matched_text']}`\n\n")
                f.write("```\n")
                for line in item['context']:
                    prefix = "=> " if line['is_target'] else "   "
                    f.write(f"{prefix}{line['line_num']}: {line['text']}\n")
                f.write("```\n\n")

        # 2. TODO Candidates
        f.write("## 2. Pending TODOs & FIXMEs\n")
        if not report_data['todo_candidates']:
            f.write("No active TODOs or FIXMEs found.\n\n")
        else:
            for idx, item in enumerate(report_data['todo_candidates']):
                f.write(f"### T-{idx+1}: TODO in `{item['file']}`\n")
                f.write(f"* **File**: `{item['file']}` (Line {item['line_num']})\n")
                f.write(f"* **Comment**: `{item['matched_text']}`\n\n")
                f.write("```\n")
                for line in item['context']:
                    prefix = "=> " if line['is_target'] else "   "
                    f.write(f"{prefix}{line['line_num']}: {line['text']}\n")
                f.write("```\n\n")

        # 3. Duplicate Blocks
        f.write("## 3. Duplicate Code Blocks\n")
        if not report_data['duplicate_blocks']:
            f.write("No duplicate code blocks found.\n\n")
        else:
            for idx, item in enumerate(report_data['duplicate_blocks']):
                is_internal = item['file_a'] == item['file_b']
                dup_type = "Internal Duplication" if is_internal else "Cross-File Duplication"
                f.write(f"### D-{idx+1}: {dup_type} ({item['duplicate_non_trivial_lines']} identical lines)\n")
                f.write(f"* **Location A**: `{item['file_a']}` (Lines {item['file_a_start']}-{item['file_a_end']})\n")
                f.write(f"* **Location B**: `{item['file_b']}` (Lines {item['file_b_start']}-{item['file_b_end']})\n\n")
                f.write("**Code Preview (from Location A):**\n")
                f.write("```\n")
                for line in item['code_preview']:
                    f.write(f"{line}\n")
                f.write("```\n\n")

def main():
    parser = argparse.ArgumentParser(description="Scan codebase for LLM laziness, placeholder stubs, and code duplication.")
    parser.add_argument("--path", default=".", help="Root path of the repository to scan.")
    parser.add_argument("--output", default="qco-report.json", help="Path to write the report file.")
    parser.add_argument("--min-dup-lines", type=int, default=6, help="Minimum number of contiguous normalized lines to classify as duplicate.")
    parser.add_argument("--format", choices=["json", "markdown", "both"], default="json", help="Output report format.")
    args = parser.parse_args()

    root_path = os.path.abspath(args.path)
    
    file_lines_map = {}
    all_laziness_candidates = []
    all_todo_candidates = []

    # Step 1: Walk the repository and scan each file for heuristics
    for dirpath, dirnames, filenames in os.walk(root_path):
        # Prune ignore directories in-place
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        
        for file in filenames:
            ext = os.path.splitext(file)[1]
            if ext not in SUPPORTED_EXTENSIONS:
                continue

            full_path = os.path.join(dirpath, file)
            rel_path = os.path.relpath(full_path, root_path)

            try:
                with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                
                file_lines_map[rel_path] = lines

                # Run local heuristics
                laziness_finds, todo_finds = scan_file_heuristics(full_path, lines, rel_path)
                all_laziness_candidates.extend(laziness_finds)
                all_todo_candidates.extend(todo_finds)

            except Exception as e:
                # Silently ignore unreadable files to ensure robust execution
                continue

    # Step 2: Run structural duplication analysis across all files
    duplicate_blocks = detect_clones(file_lines_map, min_dup_lines=args.min_dup_lines)

    # Step 3: Bundle results
    report_data = {
        "summary": {
            "total_laziness_candidates": len(all_laziness_candidates),
            "total_todo_candidates": len(all_todo_candidates),
            "total_duplicate_blocks": len(duplicate_blocks),
            "scanned_files_count": len(file_lines_map)
        },
        "laziness_candidates": all_laziness_candidates,
        "todo_candidates": all_todo_candidates,
        "duplicate_blocks": duplicate_blocks
    }

    # Step 4: Write output report(s)
    if args.format in ("json", "both"):
        json_output = args.output if args.output.endswith('.json') else f"{args.output}.json"
        with open(json_output, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2)
        print(f"Successfully generated structured JSON report: {json_output}")

    if args.format in ("markdown", "both"):
        md_output = args.output
        if args.format == "both":
            md_output = os.path.splitext(json_output)[0] + ".md"
        elif not md_output.endswith('.md'):
            md_output = f"{md_output}.md"
            
        write_markdown_report(report_data, md_output)
        print(f"Successfully generated human-readable Markdown report: {md_output}")

if __name__ == "__main__":
    main()
