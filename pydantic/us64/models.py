from pydantic import BaseModel, validator

# Scenario 1: Default values applied
class Product(BaseModel):
    name: str = "Unknown Product"
    price: float

# Scenario 2: Custom validator
class User(BaseModel):
    username: str

    @validator('username')
    def username_must_be_alphanumeric(cls, v):
        if not v.isalnum():
            raise ValueError('username must be alphanumeric')
        return v
