import numpy as np
import gradio as gr

app = gr.Blocks()

def flip_text(x):
    return x[::-1]


def flip_img(x):
    return np.fliplr(x)


with app:
    gr.Markdown(
        """
        # Flipper
        """
    )

    with gr.Tabs():
        with gr.TabItem("Flip Text"):
            with gr.Row():
                text_input = gr.Textbox()
                text_output = gr.Textbox()
            text_button = gr.Button("Flip")
        
        with gr.TabItem("Flip Image"):
            with gr.Row():
                image_input = gr.Image()
                image_output = gr.Image()
            image_button = gr.Button("Flip")

        
        text_button.click(
            flip_text,
            inputs=text_input,
            outputs=text_output
        )

        image_button.click(
            flip_img,
            inputs=image_input,
            outputs=image_output
        )

app.launch()