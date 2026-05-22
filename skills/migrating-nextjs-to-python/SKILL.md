---
name: migrating-nextjs-to-python
description: >-
  Translates Next.js JavaScript/TypeScript API routes (req, res) into clean FastAPI Python backend endpoints. Use when translating server-side API endpoints, request validation interfaces, and database handlers to Python. Don't use for frontend React component migration, building Dockerfiles, or creating GitHub backlogs.
---

# Migrating Next.js to Python Backend

This skill converts JavaScript/TypeScript serverless routes into highly performant, type-hinted FastAPI endpoints.

## Rules
1. **Never manual map TypeScript interfaces.** To avoid schema compilation errors, always run `python3 scripts/generate_pydantic_schema.py --source {ts_file}` to extract typescript interfaces and output clean Pydantic V2 schemas.
2. **Implement Type Hints and Pydantic.** Every input payload must be validated via a Pydantic Model. Every response must define a `response_model` type in FastAPI.
3. **SQLModel / SQLAlchemy Integration.** Map all database operations to SQLModel sessions instead of JS-based prisma or mongodb queries. Follow templates in `references/fastapi-route-template.md`.
4. **HTTP Exception Handling.** React/Next.js API error returns (`res.status(400).json(...)`) must be raised as standard FastAPI `HTTPException(status_code=400, detail="...")` responses.

## Workflow
1. Identify the TypeScript interfaces or payloads in the Next.js API route.
2. Run the pydantic translator helper:
   ```bash
   python3 scripts/generate_pydantic_schema.py --source {path_to_api_file}
   ```
3. Read the outputted Pydantic model and paste it in your new schema module.
4. Open `references/fastapi-route-template.md` to see the structure of endpoints.
5. Create the Python route module using FastAPI APIRouter, referencing the generated schema.
