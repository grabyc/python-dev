# User Story 63: Using Pydantic Models

## Overview
This user story demonstrates how to use Pydantic models for data validation in Python applications. Pydantic provides a simple way to define data schemas using Python classes, ensuring that input data is valid and well-structured.

## Example: User Model
We define a `User` model with two fields:
- `name`: a string representing the user's name
- `email`: a string representing the user's email address, validated as a proper email

```python
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
```

## Creating and Validating Instances
When you create an instance of the model with valid data, Pydantic automatically validates the fields:

```python
user = User(name="Alice", email="alice@example.com")
print(user)
```

If the data is invalid (e.g., an incorrect email format), Pydantic will raise a validation error.

## Integration Example
In this project, the Pydantic model is used in a Gradio app to validate user input for name and email. When valid data is provided, the app accepts and displays it; otherwise, it shows an error message.

---
For more details, see 
 - the implementation in `gradio_app.py` and `pydantic_use_case.py`.
 - models documentation in [Pydantic Models](https://docs.pydantic.dev/latest/concepts/models/)
