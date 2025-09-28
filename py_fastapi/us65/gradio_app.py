import gradio as gr
import requests

def get_root_message(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

with gr.Blocks() as demo:
    gr.Markdown("## FastAPI Root Endpoint Tester")
    api_url = gr.Textbox(label="API Root URL", value="http://127.0.0.1:8000/")
    output = gr.JSON(label="Response")
    gr.Button("Get Root Message").click(get_root_message, inputs=api_url, outputs=output)

if __name__ == "__main__":
    demo.launch()
