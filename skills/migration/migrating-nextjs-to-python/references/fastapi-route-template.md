# FastAPI Endpoint Construction Template

Always write FastAPI endpoints conforming to the structural template below.

```python
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
# import database models/sessions as needed

router = APIRouter(prefix="/api/v1/resource", tags=["Resource"])

# 1. Define input/output Pydantic Schemas
class ResourceCreate(BaseModel):
    name: str
    description: Optional[str] = None
    category: str

class ResourceResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    category: str

    class Config:
        from_attributes = True

# 2. Define HTTP router endpoints with type hints and status codes
@router.post("/", response_model=ResourceResponse, status_code=status.HTTP_201_CREATED)
def create_resource(payload: ResourceCreate):
    try:
        # Perform DB insertion / processing logic
        # Example validation error:
        if payload.name.lower() == "admin":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Resource name 'admin' is reserved"
            )
            
        dummy_response = {
            "id": 1,
            "name": payload.name,
            "description": payload.description,
            "category": payload.category
        }
        return dummy_response
    except Exception as e:
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal database error: {str(e)}"
        )
```
