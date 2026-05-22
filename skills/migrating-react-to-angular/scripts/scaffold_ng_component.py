import os
import argparse

def to_kebab_case(name):
    import re
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1).lower()

def to_camel_case(name):
    components = to_kebab_case(name).split('-')
    return components[0] + ''.join(x.title() for x in components[1:])

def to_pascal_case(name):
    return ''.join(x.title() for x in to_kebab_case(name).split('-'))

def scaffold(component_name, out_dir):
    kebab = to_kebab_case(component_name)
    pascal = to_pascal_case(component_name)
    comp_dir = os.path.join(out_dir, kebab)
    os.makedirs(comp_dir, exist_ok=True)

    ts_content = f"""import {{ Component, signal }} from '@angular/core';
import {{ CommonModule }} from '@angular/common';
import {{ MatButtonModule }} from '@angular/material/button';
import {{ MatInputModule }} from '@angular/material/input';
import {{ MatFormFieldModule }} from '@angular/material/form-field';
import {{ ReactiveFormsModule }} from '@angular/forms';

@Component({{
  selector: 'app-{kebab}',
  standalone: true,
  imports: [
    CommonModule,
    MatButtonModule,
    MatInputModule,
    MatFormFieldModule,
    ReactiveFormsModule
  ],
  templateUrl: './{kebab}.component.html',
  styleUrls: ['./{kebab}.component.css']
}})
export class {pascal}Component {{
  // State signal placeholders
  // constructor() {{}}
}}
"""

    html_content = f"""<div class="{kebab}-container">
  <!-- TODO: Translate JSX template to Angular Material here -->
  <p>{kebab} works!</p>
</div>
"""

    css_content = f""".{kebab}-container {{
  display: block;
  padding: 16px;
}}
"""

    with open(os.path.join(comp_dir, f"{kebab}.component.ts"), "w") as f:
        f.write(ts_content)
    with open(os.path.join(comp_dir, f"{kebab}.component.html"), "w") as f:
        f.write(html_content)
    with open(os.path.join(comp_dir, f"{kebab}.component.css"), "w") as f:
        f.write(css_content)

    print(f"Scaffolded Angular 17+ standalone component '{pascal}Component' inside '{comp_dir}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True, help="Component name in PascalCase")
    parser.add_argument("--out", required=True, help="Output destination folder")
    args = parser.parse_args()
    scaffold(args.name, args.out)
