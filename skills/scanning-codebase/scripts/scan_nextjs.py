import os
import json
import argparse

def scan_project(root_path):
    ignore_dirs = {'node_modules', '.next', '.git', 'public', 'dist'}
    architecture = {"routes": [], "api_endpoints": [], "components": []}

    for dirpath, dirnames, filenames in os.walk(root_path):
        dirnames[:] = [d for d in dirnames if d not in ignore_dirs]
        for file in filenames:
            if not file.endswith(('.js', '.jsx', '.ts', '.tsx')):
                continue
            
            rel_path = os.path.relpath(os.path.join(dirpath, file), root_path)
            parts = rel_path.split(os.sep)
            
            if 'api' in parts:
                architecture["api_endpoints"].append(rel_path)
            elif 'pages' in parts or 'app' in parts:
                architecture["routes"].append(rel_path)
            elif 'components' in parts:
                architecture["components"].append(rel_path)

    print(json.dumps(architecture, indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True, help="Path to Next.js project")
    args = parser.parse_args()
    scan_project(args.path)
