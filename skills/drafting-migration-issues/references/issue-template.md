# Issue Template

When drafting issues, output them as a JSON array of objects matching this schema. Do not deviate.

```json
[
  {
    "title": "[Frontend] Migrate {FileName} to Angular Material",
    "labels": ["migration", "frontend", "angular-material"],
    "body": "**Original File:** `{FilePath}`\n**Target:** Angular 17+ & Material\n\n**Acceptance Criteria:**\n- [ ] Create `.ts`, `.html`, `.scss` files.\n- [ ] Replace React hooks with Angular properties/Signals.\n- [ ] Map HTML to `<mat-*>` components.\n\n**Dependencies:** {List dependencies or 'None'}"
  },
  {
    "title": "[Backend] Migrate {FileName} to Python",
    "labels": ["migration", "backend", "python"],
    "body": "**Original File:** `{FilePath}`\n**Target:** Python Backend\n\n**Acceptance Criteria:**\n- [ ] Create Python endpoint matching original route.\n- [ ] Replicate request validation and response schema.\n\n**Dependencies:** {List dependencies or 'None'}"
  }
]
```
