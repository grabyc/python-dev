from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr

def process_user(user: User):
    # In a real app, you might save to DB or perform other logic
    return {"name": user.name, "email": user.email}
