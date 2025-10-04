import gradio as gr
from looping_logic import for_loop_elements, while_loop_counter

def for_loop_demo():
    lst = [1, 2, 3]
    result = for_loop_elements(lst)
    return "\n".join(result)

def while_loop_demo():
    x = 0
    result = while_loop_counter(x)
    return "\n".join(result)

with gr.Blocks() as demo:
    gr.Markdown("""# Python Looping Use Cases\n\nDemonstrates for and while loop scenarios.""")
    with gr.Tab("For Loop"):
        for_output = gr.Textbox(label="For Loop Output")
        for_btn = gr.Button("Run For Loop")
        for_btn.click(fn=for_loop_demo, outputs=for_output)
    with gr.Tab("While Loop"):
        while_output = gr.Textbox(label="While Loop Output")
        while_btn = gr.Button("Run While Loop")
        while_btn.click(fn=while_loop_demo, outputs=while_output)

demo.launch()
