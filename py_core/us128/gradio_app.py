import gradio as gr
from conditional_logic import simple_if_else, multiple_conditions

def try_simple_if_else(x):
    return simple_if_else(int(x))

def try_multiple_conditions(score):
    return multiple_conditions(int(score))

with gr.Blocks() as demo:
    gr.Markdown("## Simple Condition with if/else")
    x_input = gr.Number(label="x", value=10)
    x_output = gr.Textbox(label="Result")
    gr.Button("Evaluate if/else").click(try_simple_if_else, inputs=x_input, outputs=x_output)

    gr.Markdown("## Multiple Conditions with elif")
    score_input = gr.Number(label="score", value=85)
    score_output = gr.Textbox(label="Result")
    gr.Button("Evaluate elif").click(try_multiple_conditions, inputs=score_input, outputs=score_output)

if __name__ == "__main__":
    demo.launch()
