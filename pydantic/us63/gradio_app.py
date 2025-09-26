import gradio as gr

def greet(name):
    return f"Hello, {name}!"

app = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="Your Name"),
    outputs=gr.Textbox(label="Greeting"),
    title="Greeting App",
    description="Enter your name to receive a greeting."
)

if __name__ == "__main__":
    app.launch()
