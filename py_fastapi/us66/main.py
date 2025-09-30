from fastapi import FastAPI
from user_logic import User, process_user

app = FastAPI()

@app.post("/user")
def create_user(user: User):
    return {"success": True, "data": process_user(user)}
