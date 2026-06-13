#!/usr/bin/env python3
import re
import sys
import argparse
from typing import List, Tuple, Dict

class MermaidLinter:
    def __init__(self, content: str, file_type: str = "markdown"):
        self.content = content
        self.file_type = file_type
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def log_error(self, line_num: int, message: str, block_start: int = 1):
        self.errors.append(f"Line {block_start + line_num - 1}: [ERROR] {message}")

    def log_warning(self, line_num: int, message: str, block_start: int = 1):
        self.warnings.append(f"Line {block_start + line_num - 1}: [WARNING] {message}")

    def run(self) -> Tuple[List[str], List[str]]:
        if self.file_type == "markdown":
            blocks = self.extract_mermaid_blocks(self.content)
            for block_code, start_line in blocks:
                self.lint_diagram(block_code, start_line)
        else:
            self.lint_diagram(self.content, 1)
        return self.errors, self.warnings

    def extract_mermaid_blocks(self, text: str) -> List[Tuple[str, int]]:
        blocks = []
        lines = text.splitlines()
        in_block = False
        current_block = []
        start_line = 0

        for i, line in enumerate(lines, 1):
            if line.strip().startswith("```mermaid"):
                in_block = True
                current_block = []
                start_line = i + 1
            elif line.strip().startswith("```") and in_block:
                in_block = False
                blocks.append(("\n".join(current_block), start_line))
            elif in_block:
                current_block.append(line)
        return blocks

    def lint_diagram(self, code: str, start_line: int):
        lines = code.splitlines()
        if not lines:
            return

        # Find first non-empty, non-comment, non-frontmatter line to identify type
        diag_type = ""
        diag_type_line_idx = -1
        in_frontmatter = False

        for idx, line in enumerate(lines):
            stripped = line.strip()
            if not stripped or stripped.startswith("%%"):
                continue
            if stripped == "---":
                in_frontmatter = not in_frontmatter
                continue
            if in_frontmatter:
                continue
            diag_type = stripped.split()[0]
            diag_type_line_idx = idx
            break

        if not diag_type:
            self.log_warning(1, "Empty or fully commented diagram block.", start_line)
            return

        # Core flowchart check
        if diag_type in ("flowchart", "graph"):
            if diag_type == "graph":
                self.log_warning(diag_type_line_idx + 1, f"Legacy keyword 'graph' used. Consider migrating to 'flowchart' for better rendering.", start_line)
            self.lint_flowchart(lines, start_line)
        elif diag_type == "sequenceDiagram":
            self.lint_sequence_diagram(lines, start_line)
        elif diag_type == "erDiagram":
            self.lint_er_diagram(lines, start_line)
        elif diag_type == "stateDiagram-v2" or diag_type == "stateDiagram":
            if diag_type == "stateDiagram":
                self.log_warning(diag_type_line_idx + 1, "Legacy keyword 'stateDiagram' used. Consider migrating to 'stateDiagram-v2' for modern rendering.", start_line)
            self.lint_state_diagram(lines, start_line)

    def lint_flowchart(self, lines: List[str], start_line: int):
        subgraphs_count = 0
        ends_count = 0

        # Regexes
        # Detects links like -->|label| or -.->|label|
        # Group 1 is the label content
        link_label_pattern = re.compile(r'(?:-->|-\.-|==>|--|-.->)\s*\|([^|]+)\|')
        
        # Detects shape brackets with nested parenthesies, e.g. NodeId(Fetch (v1))
        # Group 1 is the outer/inner delimiter and label
        node_shape_pattern = re.compile(r'\b([a-zA-Z0-9_-]+)\s*(?:\[([^\]]+)\]|\(([^)]+)\)|\{([^}]+)\})')

        for idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if not stripped or stripped.startswith("%%"):
                continue

            # Check for unmatched subgraphs
            if stripped.startswith("subgraph"):
                subgraphs_count += 1
            elif stripped == "end":
                ends_count += 1

            # Check link labels
            for match in link_label_pattern.finditer(line):
                label = match.group(1).strip()
                # Check if it has parentheses/special characters and is NOT quoted
                if any(char in label for char in "()[],:;/") and not (label.startswith('"') and label.endswith('"')):
                    self.log_error(
                        idx, 
                        f"Unquoted special characters inside link label: '|{label}|'. "
                        f"Wrap the label in double quotes to prevent rendering errors: '|\"{label}\"|'.",
                        start_line
                    )

            # Check node text shape definitions for nested unquoted parenthesis or brackets
            for match in node_shape_pattern.finditer(line):
                node_id = match.group(1)
                # Check text segments (group 2 is [], group 3 is (), group 4 is {})
                for g_idx in (2, 3, 4):
                    label = match.group(g_idx)
                    if label:
                        label = label.strip()
                        # If label contains unquoted parens, brackets, or other shapes
                        if any(char in label for char in "()[]{}") and not (label.startswith('"') and label.endswith('"')):
                            self.log_error(
                                idx, 
                                f"Unquoted brackets or parenthesis in node '{node_id}' label: '{label}'. "
                                f"Wrap the text in double quotes inside the delimiters: '{node_id}(\"{label}\")'.",
                                start_line
                            )

        if subgraphs_count != ends_count:
            self.log_error(
                len(lines),
                f"Mismatched subgraphs! Found {subgraphs_count} 'subgraph' definitions but {ends_count} 'end' delimiters.",
                start_line
            )

    def lint_sequence_diagram(self, lines: List[str], start_line: int):
        has_autonumber = False
        # Sequence diagrams do not support flowchart arrows (like -->)
        invalid_arrow_pattern = re.compile(r'-->(?!>)|---')

        for idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if not stripped or stripped.startswith("%%"):
                continue

            if stripped == "autonumber":
                has_autonumber = True

            if invalid_arrow_pattern.search(line):
                self.log_error(
                    idx,
                    "Flowchart style arrow (--> or ---) used in sequence diagram. "
                    "Use sequence arrows like '->>', '-->>', '->', or '-->' (without node IDs).",
                    start_line
                )

        if not has_autonumber:
            self.log_warning(
                1,
                "Consider adding 'autonumber' to the sequence diagram to make step ordering highly legible.",
                start_line
            )

    def lint_er_diagram(self, lines: List[str], start_line: int):
        # Relationship syntax: ENTITY1 ||--|{ ENTITY2 : "relationship label"
        # Often LLMs forget the quotes or the colon
        relationship_pattern = re.compile(r'([a-zA-Z0-9_-]+)\s+[^:]+:\s*([^"\s]+)')
        
        for idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if not stripped or stripped.startswith("%%"):
                continue

            match = relationship_pattern.search(line)
            if match:
                unquoted_label = match.group(2)
                self.log_error(
                    idx,
                    f"Unquoted relationship label '{unquoted_label}'. Wrap ER relationship labels in double quotes, e.g. ': \"{unquoted_label}\"'.",
                    start_line
                )

    def lint_state_diagram(self, lines: List[str], start_line: int):
        # Transition syntax: State1 --> State2 : "Label"
        transition_pattern = re.compile(r'([a-zA-Z0-9_-]+)\s*-->\s*([a-zA-Z0-9_-]+)\s*:\s*([^"\s]+)')

        for idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if not stripped or stripped.startswith("%%"):
                continue

            match = transition_pattern.search(line)
            if match:
                unquoted_label = match.group(3)
                self.log_error(
                    idx,
                    f"Unquoted transition description '{unquoted_label}'. State diagram transitions with labels must be quoted, e.g. ': \"{unquoted_label}\"'.",
                    start_line
                )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lint and validate Mermaid.js code blocks.")
    parser.add_argument("file", help="Path to markdown or mermaid file to validate")
    parser.add_argument("--type", choices=["markdown", "raw"], default="markdown", help="File format")
    args = parser.parse_args()

    try:
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file {args.file}: {e}")
        sys.exit(1)

    linter = MermaidLinter(content, args.type)
    errors, warnings = linter.run()

    if warnings:
        print("\n=== Mermaid Warnings ===")
        for warning in warnings:
            print(warning)

    if errors:
        print("\n=== Mermaid Lint/Syntax Errors ===")
        for error in errors:
            print(error)
        print(f"\nValidation failed with {len(errors)} error(s).")
        sys.exit(1)
    else:
        print("\n✅ Mermaid validation passed successfully!")
        sys.exit(0)
