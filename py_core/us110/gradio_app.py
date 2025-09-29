import gradio as gr
from data_types import integer_operations, string_operations, boolean_evaluation

with gr.Blocks() as demo:
    gr.Markdown("## Integer Operations")
    int_a = gr.Number(label="Integer A", value=2)
    int_b = gr.Number(label="Integer B", value=3)
    int_output = gr.JSON(label="Results")
    gr.Button("Compute Integer Operations").click(integer_operations, inputs=[int_a, int_b], outputs=int_output)

    gr.Markdown("## String Operations")
    str_input = gr.Textbox(label="Input String", value="hello")
    str_output = gr.JSON(label="Results")
    gr.Button("Compute String Operations").click(string_operations, inputs=str_input, outputs=str_output)

    gr.Markdown("## Boolean Evaluation")
    bool_a = gr.Number(label="A", value=2)
    bool_b = gr.Number(label="B", value=3)
    bool_output = gr.JSON(label="Results")
    gr.Button("Evaluate Booleans").click(boolean_evaluation, inputs=[bool_a, bool_b], outputs=bool_output)

if __name__ == "__main__":
    demo.launch()
