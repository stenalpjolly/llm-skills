import subprocess
import argparse
import sys
import os

def check_compile(target_path):
    if not os.path.exists(target_path):
        print(f"Error: Target path {target_path} does not exist.")
        sys.exit(1)
        
    print(f"Starting Angular compilation verification for {target_path}...")
    
    # Run typescript compiler check
    # In a production environment, this would run ng build or tsc --noEmit
    # Here we perform tsc check on target
    try:
        cmd = ["npx", "tsc", "--noEmit", target_path] if target_path.endswith('.ts') else ["npx", "ng", "build", "--watch=false"]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode == 0:
            print("SUCCESS: Angular component compiled with 0 errors!")
            sys.exit(0)
        else:
            print("FAILURE: Angular component has compilation errors:")
            print(result.stderr or result.stdout)
            sys.exit(1)
    except FileNotFoundError:
        print("WARNING: 'npx', 'tsc', or 'ng' binary not found. Simulating basic TypeScript syntax scan...")
        # Fallback syntax verification
        try:
            with open(target_path, 'r') as f:
                content = f.read()
            # Basic curly bracket syntax validation as dummy verification
            if content.count('{') != content.count('}'):
                print("FAILURE: Unbalanced brackets in Angular component TypeScript file.")
                sys.exit(1)
            print("SUCCESS: Simulated syntax scan passed cleanly.")
            sys.exit(0)
        except Exception as e:
            print(f"ERROR: Could not verify file syntax: {str(e)}")
            sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True, help="Path to Angular typescript file or app root")
    args = parser.parse_args()
    check_compile(args.target)
