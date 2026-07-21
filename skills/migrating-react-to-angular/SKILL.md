---
name: migrating-react-to-angular
description: >-
  Converts React components (.jsx/.tsx) into standalone Angular 17+ components using Angular Material. Use when a user asks to migrate frontend components or translate React hooks/JSX into Angular. Don't use for backend Python API migrations, database design, or pipeline scheduling.
---

# Migrating React to Angular

This skill facilitates the safe, structural conversion of React components to modern standalone Angular 17+ components with Angular Material design.

## Rules
1. **Never build from scratch manually.** To avoid import mistakes, always execute `python3 ../shared-migration-utils/scaffold_ng_component.py --name {component_name} --out {dest_dir}` first to generate perfect, syntactically correct Angular standalone boilerplate.
2. **Implement Angular Signals.** Map all React `useState` hooks to Angular `signal()` properties. Use `references/hooks-to-signals-map.md` as the mapping standard.
3. **Strict Material Mappings.** Convert HTML elements and MUI tags to their matching Angular Material modules. Use `references/material-components.md` as the mapping standard.
4. **Standalone Architecture.** All generated components MUST be `standalone: true` and list their dependent material modules inside the `@Component.imports` array.

## Workflow
1. Identify the component name and destination directory.
2. Run the scaffolding script:
   ```bash
   python3 ../shared-migration-utils/scaffold_ng_component.py --name {ComponentName} --out {dest_dir}
   ```
3. Read the generated `.ts`, `.html`, and `.css` files.
4. Parse the React component file, using `references/hooks-to-signals-map.md` to translate component logic and hooks into `.ts`.
5. Use `references/material-components.md` to translate React JSX into Angular HTML in `.component.html`.
6. Write the final outputs into the scaffolded files.
