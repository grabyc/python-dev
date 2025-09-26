import gradio as gr
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr

def greet_with_email(name, email):
    try:
        user = User(name=name, email=email)
        return f"Hello, {user.name}! Your email {user.email} is valid."
    except Exception as e:
        return f"Error: {e}"

app = gr.Interface(
    fn=greet_with_email,
    inputs=[gr.Textbox(label="Your Name"), gr.Textbox(label="Your Email")],
    outputs=gr.Textbox(label="Result"),
    title="Greeting App with Email Validation",
    description="Enter your name and email to receive a greeting and validate your email."
)

if __name__ == "__main__":
    app.launch()
