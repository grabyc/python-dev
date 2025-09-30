import gradio as gr
import requests
import json

def post_user(api_url, name, email):
    try:
        payload = {"name": name, "email": email}
        response = requests.post(api_url, json=payload)
        return response.status_code, response.json()
    except Exception as e:
        return 0, {"error": str(e)}

with gr.Blocks() as demo:
    gr.Markdown("## Test FastAPI POST /user Endpoint")
    api_url = gr.Textbox(label="API URL", value="http://127.0.0.1:8000/user")
    name = gr.Textbox(label="Name", value="Alice")
    email = gr.Textbox(label="Email", value="alice@example.com")
    status = gr.Number(label="Status Code")
    output = gr.JSON(label="Response")
    gr.Button("Send POST Request").click(post_user, inputs=[api_url, name, email], outputs=[status, output])

if __name__ == "__main__":
    demo.launch()
