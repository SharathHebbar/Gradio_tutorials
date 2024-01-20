
from flask import Flask
import gradio as gr

app = Flask(__name__)

@app.route('/')

def hello_world():
	return 'Hello World'
io = gr.Interface(lambda x: "Hello, " + x + "!", "textbox", "textbox")
app = gr.mount_gradio_app(app, io, path="/gradio")
if __name__ == '__main__':
	app.run()


