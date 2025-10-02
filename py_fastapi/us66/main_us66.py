from fastapi import FastAPI
from py_fastapi.us66.user_logic import User, process_user

app = FastAPI()

@app.post("/user")
def create_user(user: User):
    return {"success": True, "data": process_user(user)}
