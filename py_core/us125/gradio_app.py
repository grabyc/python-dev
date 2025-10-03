import gradio as gr
from mutability_logic import modify_list, modify_tuple, shared_reference_side_effects

def try_modify_list(lst_str, to_append):
    lst = [int(x.strip()) for x in lst_str.split(",") if x.strip()]
    result = modify_list(lst, int(to_append))
    return f"Modified list: {result}"

def try_modify_tuple(tpl_str, index, value):
    tpl = tuple(int(x.strip()) for x in tpl_str.split(",") if x.strip())
    result, id_mutation = modify_tuple(tpl, int(index), int(value))
    return f"Result: {result}; tpl ID: {id(tpl)}; tpl_mutation ID: {id_mutation}"

def try_shared_reference():
    a, b = shared_reference_side_effects()
    return f"a: {a}, b: {b}"

with gr.Blocks() as demo:
    gr.Markdown("## Modifying a List (Mutable)")
    list_input = gr.Textbox(label="List (comma-separated)", value="1,2,3")
    to_append = gr.Number(label="Element to append", value=4)
    list_output = gr.Textbox(label="Result")
    gr.Button("Append to List").click(try_modify_list, inputs=[list_input, to_append], outputs=list_output)

    gr.Markdown("## Attempting to Modify a Tuple (Immutable)")
    tuple_input = gr.Textbox(label="Tuple (comma-separated)", value="1,2,3")
    tuple_index = gr.Number(label="Index to modify", value=0)
    tuple_value = gr.Number(label="New value", value=9)
    tuple_output = gr.Textbox(label="Result")
    gr.Button("Modify Tuple").click(try_modify_tuple, inputs=[tuple_input, tuple_index, tuple_value], outputs=tuple_output)

    gr.Markdown("## Shared Reference Side Effects")
    shared_output = gr.Textbox(label="Result")
    gr.Button("Show Shared Reference Effect").click(try_shared_reference, outputs=shared_output)

if __name__ == "__main__":
    demo.launch()
