import gradio as gr
from type_hints_logic import add, sum_list

def try_add(a, b):
    try:
        result = add(a, b)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e}"

def try_sum_list(numbers_str):
    try:
        numbers = [int(x.strip()) for x in numbers_str.split(",") if x.strip()]
        result = sum_list(numbers)
        return f"Sum: {result}"
    except Exception as e:
        return f"Error: {e}"

with gr.Blocks() as demo:
    gr.Markdown("## Function with Parameter Hints")
    a = gr.Number(label="a (int)", value=2)
    b = gr.Number(label="b (int)", value=3)
    add_output = gr.Textbox(label="Add Result")
    gr.Button("Add").click(try_add, inputs=[a, b], outputs=add_output)

    gr.Markdown("## Complex Type Hints (List[int])")
    numbers_input = gr.Textbox(label="List of integers (comma-separated)", value="1,2,3")
    sum_output = gr.Textbox(label="Sum Result")
    gr.Button("Sum List").click(try_sum_list, inputs=numbers_input, outputs=sum_output)

if __name__ == "__main__":
    demo.launch()
