#!/usr/bin/env python3
import os
import argparse
import sys

# Stack-specific Gitignore configuration templates
GITIGNORE_TEMPLATES = {
    "generic": """# Global OS files
.DS_Store
Thumbs.db
*.log

# IDE files
.vscode/
.idea/
*.suo
*.ntvs*
*.njsproj
*.sln

# Environments & secrets
.env
.env.local
.env.*.local
""",
    "python": """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/

# Environments
.env
.venv/
venv/
ENV/
env/

# Testing / coverage
.cache/
.pytest_cache/
.coverage
htmlcov/
""",
    "typescript": """# Dependency directories
node_modules/
jspm_packages/

# Transpilation / Build outputs
dist/
out/
build/
*.tsbuildinfo

# Debug logs
npm-debug.log*
yarn-debug.log*
pnpm-debug.log*
lerna-debug.log*

# Environments & secrets
.env
.env.local
.env.development.local
.env.test.local
.env.production.local
""",
    "go": """# Binaries and templates
bin/
pkg/
obj/

# Testing
*.test
*.out

# Environments & secrets
.env
""",
    "rust": """# Build artifacts
target/

# Backup files
*.rs.bk

# Environments & secrets
.env
"""
}

def setup_directory_tree(stack, target_dir):
    # Standard agnostic structure
    dirs = [
        "docs",
        "src",
        "tests"
    ]
    
    # Specific stack variations
    if stack == "go":
        dirs.extend(["cmd", "pkg", "internal"])
    
    print(f"[*] Initializing project directories for stack: '{stack}'...")
    for d in dirs:
        path = os.path.join(target_dir, d)
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
            print(f"  [+] Created directory: {d}/")
        else:
            print(f"  [~] Directory already exists: {d}/")

def create_gitignore(stack, target_dir):
    gitignore_path = os.path.join(target_dir, ".gitignore")
    if os.path.exists(gitignore_path):
        print("  [~] .gitignore already exists. Skipping creation to avoid overwriting rules.")
        return
        
    template = GITIGNORE_TEMPLATES.get(stack, GITIGNORE_TEMPLATES["generic"])
    if stack != "generic":
        # Prepend standard generic rules to the stack-specific ones
        template = GITIGNORE_TEMPLATES["generic"] + "\n# " + stack.upper() + " Specifics\n" + template
        
    with open(gitignore_path, "w", encoding="utf-8") as f:
        f.write(template)
    print("  [+] Created .gitignore")

def create_placeholders(target_dir):
    # Placeholders are written as starting files if they do not exist
    placeholders = {
        "README.md": "# Project Title\n\nProvide description here.\n",
        "PLAN.md": "# Project Plan\n\n## Phase 1: Setup & Initialization\n- [ ] Initialize repository <!-- id: 0 -->\n- [ ] Configure standard environment files <!-- id: 1 -->\n"
    }
    
    for filename, content in placeholders.items():
        file_path = os.path.join(target_dir, filename)
        if os.path.exists(file_path):
            print(f"  [~] {filename} already exists. Skipping creation.")
        else:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  [+] Created placeholder {filename}")

def setup_agent_rules(target_dir):
    """
    Ensures a single canonical AGENTS.md exists and creates relative symlinks
    to .agent/AGENTS.md and .agents/AGENTS.md (or root AGENTS.md) to eliminate duplicate copies.
    """
    root_agents = os.path.join(target_dir, "AGENTS.md")
    agents_dir = os.path.join(target_dir, ".agents")
    agent_dir = os.path.join(target_dir, ".agent")
    dot_agents_file = os.path.join(agents_dir, "AGENTS.md")
    dot_agent_file = os.path.join(agent_dir, "AGENTS.md")

    placeholder_content = "# AI Agent Rules\n\nRules and guidelines for LLMs operating in this codebase.\n"

    # Identify primary canonical file if one already exists
    canonical_file = None
    if os.path.exists(root_agents) and not os.path.islink(root_agents):
        canonical_file = root_agents
    elif os.path.exists(dot_agents_file) and not os.path.islink(dot_agents_file):
        canonical_file = dot_agents_file
    elif os.path.exists(dot_agent_file) and not os.path.islink(dot_agent_file):
        canonical_file = dot_agent_file

    if not canonical_file:
        with open(root_agents, "w", encoding="utf-8") as f:
            f.write(placeholder_content)
        print("  [+] Created canonical placeholder AGENTS.md at root")
        canonical_file = root_agents
    else:
        rel_path = os.path.relpath(canonical_file, target_dir)
        print(f"  [~] Using existing canonical agent rules from: {rel_path}")

    # If canonical file is located inside a subfolder, link root AGENTS.md to it
    if canonical_file != root_agents:
        if not os.path.exists(root_agents) and not os.path.islink(root_agents):
            rel_target = os.path.relpath(canonical_file, target_dir)
            try:
                os.symlink(rel_target, root_agents)
                print(f"  [+] Created symlink AGENTS.md -> {rel_target}")
            except Exception as e:
                print(f"  [!] Failed to create symlink for root AGENTS.md: {e}")

    # Create relative symlink for .agents/AGENTS.md -> root AGENTS.md (or canonical)
    os.makedirs(agents_dir, exist_ok=True)
    _create_or_update_symlink(dot_agents_file, root_agents, agents_dir, target_dir, canonical_file)

    # Create relative symlink for .agent/AGENTS.md -> root AGENTS.md (or canonical)
    os.makedirs(agent_dir, exist_ok=True)
    _create_or_update_symlink(dot_agent_file, root_agents, agent_dir, target_dir, canonical_file)

def _create_or_update_symlink(symlink_path, target_file, parent_dir, root_dir, canonical_file):
    rel_target = os.path.relpath(target_file, parent_dir)
    display_path = os.path.relpath(symlink_path, root_dir)

    if os.path.islink(symlink_path):
        current_target = os.readlink(symlink_path)
        print(f"  [~] {display_path} is already a symlink -> {current_target}")
        return

    if os.path.exists(symlink_path):
        if os.path.abspath(symlink_path) == os.path.abspath(canonical_file):
            # This is the canonical source itself, so don't replace it
            return
        # It's an existing duplicate regular file
        print(f"  [!] Replacing duplicate file {display_path} with symlink -> {rel_target}...")
        try:
            os.remove(symlink_path)
        except Exception as e:
            print(f"  [!] Could not remove duplicate file {display_path}: {e}")
            return

    try:
        os.symlink(rel_target, symlink_path)
        print(f"  [+] Created symlink {display_path} -> {rel_target}")
    except Exception as e:
        print(f"  [!] Failed to create symlink {display_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Bootstrap a development workspace with directories and agnostic templates.")
    parser.add_argument("--stack", default="generic", choices=["generic", "python", "typescript", "go", "rust"], help="Core programming tech stack")
    parser.add_argument("--dir", default=".", help="Target root directory to bootstrap (defaults to current directory)")
    args = parser.parse_args()

    target = os.path.abspath(args.dir)
    
    # 1. Initialize Directories
    setup_directory_tree(args.stack, target)
    
    # 2. Write Gitignore
    create_gitignore(args.stack, target)
    
    # 3. Create core placeholders (README.md, PLAN.md)
    create_placeholders(target)
    
    # 4. Setup single canonical AGENTS.md with relative symlinks (.agents/AGENTS.md, .agent/AGENTS.md)
    setup_agent_rules(target)
    
    # 5. Optional: git init if .git folder is missing
    git_dir = os.path.join(target, ".git")
    if not os.path.exists(git_dir):
        print("[*] No existing .git directory detected. Run 'git init' to track your workspace.")
        
    print("[*] Bootstrapping files completed successfully!")

if __name__ == "__main__":
    main()
