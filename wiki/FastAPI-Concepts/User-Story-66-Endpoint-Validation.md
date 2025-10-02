# User Story 66: Endpoint Payload Validation

## Overview
This user story demonstrates how to use Pydantic models for request payload validation in FastAPI endpoints. It also highlights FastAPI's automatic error handling for invalid input data.

## Using Pydantic Models for Validation
FastAPI leverages Pydantic models to define the expected structure and types of request payloads. When a request is made to an endpoint, FastAPI automatically parses and validates the incoming JSON against the Pydantic model.

**Example:**
```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr

app = FastAPI()

@app.post("/user")
def create_user(user: User):
    return {"success": True, "data": user}
```

## Automatic Error Handling
If a request payload is missing required fields or contains invalid data (e.g., an invalid email), FastAPI automatically returns a 422 Unprocessable Entity response with a detailed error message.

**Example Error Response:**
```json
{
  "detail": [
    {
      "loc": ["body", "user", "email"],
      "msg": "value is not a valid email address",
      "type": "value_error.email"
    }
  ]
}
```

## Summary
- Pydantic models define and validate request payloads in FastAPI endpoints.
- FastAPI automatically returns clear error messages for invalid input, with no extra code required.
- This approach ensures robust and user-friendly API input validation.

---
For more details, see 
 - the user story in [User Story 66: [FastAPI] Build an endpoint with request body validation using Pydantic](https://dev.azure.com/gabriel-raby/Python/_workitems/edit/66)
 - the implementation in `gradio_app.py`, `user_logic.py` and `main_us66.py`
 - FastAPI POST method documentation in [FastAPI POST](https://fastapi.tiangolo.com/reference/fastapi/#fastapi.FastAPI.post)
