# User Story 63: Using Pydantic Basic Models

## Overview
This user story demonstrates how to use Pydantic models for data validation in Python applications. Pydantic provides a simple way to define data schemas using Python classes, ensuring that input data is valid and well-structured.

## BasicModel in User Story 63
Pydantic's `BaseModel` (sometimes referred to as the basic model) is the foundation for creating data models. In user story 63, `BaseModel` is used to define a `User` model, which automatically provides data validation, type enforcement, and helpful error messages. By inheriting from `BaseModel`, you can easily create robust data structures for your application.

### Key Features of BaseModel
- Automatic type validation and conversion
- Helpful error messages for invalid data
- Easy integration with other libraries (e.g., FastAPI, Gradio)
- Serialization and parsing support (dict, JSON, etc.)

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
 - the user story in [User Story 63: [Pydantic] Define and validate data models with Pydantic](https://dev.azure.com/gabriel-raby/Python/_workitems/edit/63)
 - the implementation in `gradio_app.py`
 - models documentation in [Pydantic Models](https://docs.pydantic.dev/latest/concepts/models/)
