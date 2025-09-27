# User Story 64: Using Pydantic Validators and Default Values

## Overview
This user story demonstrates intermediate features of Pydantic, focusing on the use of default values for fields and custom validators to enforce data integrity.

## Default Values
Pydantic models allow you to specify default values for fields. If a value is not provided during model instantiation, the default is automatically assigned.

**Example:**
```python
from pydantic import BaseModel

class Product(BaseModel):
    name: str = "Unknown Product"
    price: float

product = Product(price=9.99)  # 'name' is omitted
print(product.name)  # Output: Unknown Product
```

## Custom Validators
Custom validators in Pydantic are used to enforce additional constraints on fields. Validators are defined using the `@validator` decorator and can raise errors with custom messages if validation fails.

**Example:**
```python
from pydantic import BaseModel, validator, ValidationError

class User(BaseModel):
    username: str

    @validator('username')
    def username_must_be_alphanumeric(cls, v):
        if not v.isalnum():
            raise ValueError('username must be alphanumeric')
        return v

try:
    user = User(username="invalid user!")
except ValidationError as e:
    print(e)
```

## Summary
- Default values make models robust to missing data.
- Custom validators provide fine-grained control over data validation and error messages.

---
For more details, see 
 - the user story in [User Story 64: [Pydantic] Explore intermediate Pydantic features](https://dev.azure.com/gabriel-raby/Python/_workitems/edit/64)
 - the implementation in `us64.py` and `models.py` 
 - validators documentation in [Pydantic Validators](https://docs.pydantic.dev/latest/concepts/validators/)
