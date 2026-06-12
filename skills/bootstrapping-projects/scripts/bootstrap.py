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
        "PLAN.md": "# Project Plan\n\n## Phase 1: Setup & Initialization\n- [ ] Initialize repository <!-- id: 0 -->\n- [ ] Configure standard environment files <!-- id: 1 -->\n",
        "AGENTS.md": "# AI Agent Rules\n\nRules and guidelines for LLMs operating in this codebase.\n"
    }
    
    for filename, content in placeholders.items():
        file_path = os.path.join(target_dir, filename)
        if os.path.exists(file_path):
            print(f"  [~] {filename} already exists. Skipping creation.")
        else:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  [+] Created placeholder {filename}")

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
    
    # 3. Create core placeholders
    create_placeholders(target)
    
    # 4. Optional: git init if .git folder is missing
    git_dir = os.path.join(target, ".git")
    if not os.path.exists(git_dir):
        print("[*] No existing .git directory detected. Run 'git init' to track your workspace.")
        
    print("[*] Bootstrapping files completed successfully!")

if __name__ == "__main__":
    main()
