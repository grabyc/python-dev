import gradio as gr
from pydantic import ValidationError
from models import Product, User

# Gradio interface functions

def product_interface(price, name=None):
    try:
        if name:
            product = Product(name=name, price=price)
        else:
            product = Product(price=price)
        return f"Product created: name={product.name}, price={product.price}"
    except ValidationError as e:
        return str(e)

def user_interface(username):
    try:
        user = User(username=username)
        return f"User created: username={user.username}"
    except ValidationError as e:
        return str(e)

with gr.Blocks() as demo:
    gr.Markdown("## Product Creation (Default Value Demo)")
    price = gr.Number(label="Price", value=9.99)
    name = gr.Textbox(label="Name (optional)")
    product_output = gr.Textbox(label="Result")
    gr.Button("Create Product").click(product_interface, inputs=[price, name], outputs=product_output)

    gr.Markdown("## User Creation (Custom Validator Demo)")
    username = gr.Textbox(label="Username")
    user_output = gr.Textbox(label="Result")
    gr.Button("Create User").click(user_interface, inputs=username, outputs=user_output)

if __name__ == "__main__":
    demo.launch()
