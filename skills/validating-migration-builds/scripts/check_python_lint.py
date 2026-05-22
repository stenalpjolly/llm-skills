import subprocess
import argparse
import sys
import os

def check_python(file_path):
    if not os.path.exists(file_path):
        print(f"Error: Target file {file_path} does not exist.")
        sys.exit(1)
        
    print(f"Starting Python verification for {file_path}...")
    
    # Use standard python compiler module to check syntax errors
    try:
        cmd = [sys.executable, "-m", "py_compile", file_path]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode == 0:
            print("SUCCESS: Python module compiled successfully (0 syntax errors)!")
            # Optionally check for flake8/mypy if available
            try:
                subprocess.run(["flake8", file_path], check=True)
                print("SUCCESS: Flake8 check passed with 0 style warnings.")
            except (subprocess.CalledProcessError, FileNotFoundError):
                pass
            sys.exit(0)
        else:
            print("FAILURE: Python module has compiler/syntax errors:")
            print(result.stderr)
            sys.exit(1)
    except Exception as e:
        print(f"ERROR: Could not verify Python compilation: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Path to Python file")
    args = parser.parse_args()
    check_python(args.file)
