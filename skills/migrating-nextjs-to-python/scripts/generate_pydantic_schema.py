import os
import re
import argparse

def ts_interface_to_pydantic(ts_text):
    # Search for standard TS interfaces
    interface_pattern = re.compile(r'interface\s+(\w+)\s*\{(.*?)\}', re.DOTALL)
    matches = interface_pattern.findall(ts_text)
    
    pydantic_classes = ["from pydantic import BaseModel, EmailStr, Field\nfrom typing import Optional, List\n"]
    
    type_mapping = {
        "string": "str",
        "number": "float",
        "boolean": "bool",
        "any": "str",
        "string[]": "List[str]",
        "number[]": "List[float]",
        "boolean[]": "List[bool]",
    }

    for name, body in matches:
        class_lines = [f"class {name}(BaseModel):"]
        lines = body.strip().split('\n')
        for line in lines:
            line = line.strip()
            if not line or line.startswith('//'):
                continue
            
            # Match field_name?: type or field_name: type
            field_match = re.match(r'(\w+)(\?)?\s*:\s*([\w\[\]]+)', line)
            if field_match:
                f_name, optional, f_type = field_match.groups()
                py_type = type_mapping.get(f_type, "str")
                
                # Check optional
                if optional:
                    class_lines.append(f"    {f_name}: Optional[{py_type}] = None")
                else:
                    class_lines.append(f"    {f_name}: {py_type}")
                    
        pydantic_classes.append('\n'.join(class_lines))
        
    return '\n\n'.join(pydantic_classes)

def run(source_path):
    if not os.path.exists(source_path):
        print(f"Error: source file {source_path} does not exist.")
        return
    with open(source_path, 'r') as f:
        content = f.read()
    
    pydantic_code = ts_interface_to_pydantic(content)
    print(pydantic_code)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, help="Path to TypeScript/JavaScript API route file")
    args = parser.parse_args()
    run(args.source)
