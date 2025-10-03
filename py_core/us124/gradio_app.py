import gradio as gr
from type_conversion_logic import implicit_conversion, explicit_conversion, conversion_error

def try_implicit(a, b):
    try:
        result = implicit_conversion(a, b)
        return f"Result: {result} (type: {type(result).__name__})"
    except Exception as e:
        return f"Error: {e}"

def try_explicit(num_str):
    try:
        result = explicit_conversion(num_str)
        return f"Result: {result} (type: {type(result).__name__})"
    except Exception as e:
        return f"Error: {e}"

def try_error(invalid_str):
    result = conversion_error(invalid_str)
    return f"Result: {result}"

with gr.Blocks() as demo:
    gr.Markdown("## Implicit Conversion (Type Coercion)")
    a = gr.Number(label="Integer a", value=2)
    b = gr.Number(label="Float b", value=3.5)
    implicit_output = gr.Textbox(label="Result")
    gr.Button("Add").click(try_implicit, inputs=[a, b], outputs=implicit_output)

    gr.Markdown("## Explicit Conversion (String to Int)")
    num_str = gr.Textbox(label="String num_str", value="42")
    explicit_output = gr.Textbox(label="Result")
    gr.Button("Convert to Int").click(try_explicit, inputs=num_str, outputs=explicit_output)

    gr.Markdown("## Conversion Error")
    invalid_str = gr.Textbox(label="Invalid String", value="abc")
    error_output = gr.Textbox(label="Result")
    gr.Button("Try Conversion").click(try_error, inputs=invalid_str, outputs=error_output)

if __name__ == "__main__":
    demo.launch()
