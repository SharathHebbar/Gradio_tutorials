import gradio as gr

# api = gr.Interface.load("huggingface/EleutherAI/gpt-j-6B")

def complete_with_gpt(text):
    return "Hello" + text[:-50] #+ api(text[-50:])

with gr.Blocks() as app:
    textbox = gr.Textbox(
        placeholder="Type here and press enter...",
        lines=4
    )
    button = gr.Button("Generate")

    button.click(
        complete_with_gpt,
        textbox,
        textbox
    )

app.launch()

# import gradio as gr

# def greet(name):
#     return "Hello " + name + "!"

# with gr.Blocks() as demo:
#     name = gr.Textbox(label="Name")
#     output = gr.Textbox(label="Output Box")
#     greet_btn = gr.Button("Greet")
#     greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

# demo.launch()