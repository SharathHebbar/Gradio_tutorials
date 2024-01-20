import gradio as gr

def change_textbox(choice):
    if choice == "short":
        return gr.Textbox.update(
            lines=2,
            visible=True
        )
    elif choice == "long":
        return gr.Textbox.update(
            lines=8,
            visible=True
        )
    else:
        return gr.Textbox.update(
            visible=False
        )

with gr.Blocks() as app:
    radio = gr.Radio(
        ["short", "long", "none"],
        label="What kind of essay would you like to write?"
    )

    text = gr.Textbox(
        lines=2,
        interactive=True
    )

    radio.change(fn=change_textbox, inputs=radio, outputs=text)


app.launch(live=True)