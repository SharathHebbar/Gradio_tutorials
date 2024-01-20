import gradio as gr

def flip_text(x):
    return x[::-1]


app = gr.Blocks()

with app:
    gr.Markdown(
        """
        # Flip the given Text

        """
    )
    
    input_text = gr.Textbox(placeholder="Flip this text")
    output = gr.TextArea()

    input_text.change(fn=flip_text, inputs=input_text, outputs=output)

app.launch()