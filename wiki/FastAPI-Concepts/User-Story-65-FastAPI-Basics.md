# User Story 65: FastAPI Basics

## Overview
This user story demonstrates the basics of using the FastAPI library to build web APIs in Python. FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Creating a FastAPI App
To create a FastAPI application, instantiate the `FastAPI` class and define route handlers using decorators such as `@app.get()` for GET endpoints.

**Example:**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

## Running the App
You can run the app using Uvicorn:
```bash
uvicorn main:app --reload
```

- Visiting `/` returns a JSON response: `{ "message": "Hello World" }`
- Visiting `/docs` opens the interactive Swagger UI documentation.

## Summary
- FastAPI makes it easy to build APIs with automatic validation and documentation.
- Routes are defined with decorators and return JSON responses by default.
- The `/docs` endpoint provides interactive API documentation out of the box.

---
For more details, see 
 - the user story in [User Story 65: [FastAPI] Create a basic API endpoint with FastAPI](https://dev.azure.com/gabriel-raby/Python/_workitems/edit/65)
 - the implementation in `gradio_app.py` and `main.py`
 - FastAPI basic documentation in [FastAPI First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)