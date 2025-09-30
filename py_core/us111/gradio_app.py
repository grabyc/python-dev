import gradio as gr
from data_types import list_operations, dict_access, tuple_immutability, set_uniqueness

def parse_list(s):
    return [int(x.strip()) for x in s.split(",") if x.strip()]

def parse_dict(s):
    try:
        return dict(item.split(":") for item in s.split(",") if ":" in item)
    except Exception:
        return {}

def parse_tuple(s):
    return tuple(x.strip() for x in s.split(",") if x.strip())

def parse_set(s):
    return [x.strip() for x in s.split(",") if x.strip()]

with gr.Blocks() as demo:
    gr.Markdown("## List Operations")
    list_input = gr.Textbox(label="List of numbers (comma-separated)", value="1,2,3")
    to_append = gr.Number(label="Number to append", value=4)
    to_remove = gr.Number(label="Number to remove", value=2)
    list_output = gr.JSON(label="Results")
    gr.Button("Run List Operations").click(
        lambda s, a, r: list_operations(parse_list(s), a, r),
        inputs=[list_input, to_append, to_remove], outputs=list_output)

    gr.Markdown("## Dictionary Key-Value Access")
    dict_input = gr.Textbox(label="Dictionary (key1:val1,key2:val2)", value="a:1,b:2")
    dict_key = gr.Textbox(label="Key to access", value="a")
    dict_output = gr.JSON(label="Results")
    gr.Button("Access Dictionary").click(
        lambda s, k: dict_access(parse_dict(s), k),
        inputs=[dict_input, dict_key], outputs=dict_output)

    gr.Markdown("## Tuple Immutability")
    tuple_input = gr.Textbox(label="Tuple values (comma-separated)", value="x,y,z")
    tuple_index = gr.Number(label="Index to modify", value=1)
    tuple_value = gr.Textbox(label="New value", value="new")
    tuple_output = gr.JSON(label="Results")
    gr.Button("Test Tuple Immutability").click(
        lambda s, i, v: tuple_immutability(parse_tuple(s), int(i), v),
        inputs=[tuple_input, tuple_index, tuple_value], outputs=tuple_output)

    gr.Markdown("## Set Uniqueness")
    set_input = gr.Textbox(label="Set values (comma-separated)", value="1,2,2,3,3,3")
    set_output = gr.JSON(label="Results")
    gr.Button("Show Unique Set Values").click(
        lambda s: set_uniqueness(parse_set(s)),
        inputs=set_input, outputs=set_output)

if __name__ == "__main__":
    demo.launch()
