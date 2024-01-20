import os
import gradio as gr
from langchain.llms import HuggingFaceHub


models_name = (
        "HuggingFaceH4/zephyr-7b-beta",
        "Sharathhebbar24/chat_gpt2",
        "Sharathhebbar24/convo_bot_gpt_v1",
        "Sharathhebbar24/Instruct_GPT",
        "Sharathhebbar24/math_gpt2",
        "Sharathhebbar24/llama_chat_small_7b",
        "Deci/DeciCoder-6B",
        "Deci/DeciLM-7B-instruct",
        "Deci/DeciCoder-1b",
        "Deci/DeciLM-7B-instruct-GGUF",
        "Open-Orca/Mistral-7B-OpenOrca",
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        "Sharathhebbar24/llama_7b_chat",
        "CultriX/MistralTrix-v1",
        "ahxt/LiteLlama-460M-1T",
        "gorilla-llm/gorilla-7b-hf-delta-v0",
        "codeparrot/codeparrot"
    )
models = gr.Dropdown(
    choices=models_name,
    label="Choose your models",
)

temperature = gr.Slider(
    minimum=0.1,
    maximum=1.0,
    step=0.1,
    value=0.5,
    label='Temperature',
    # help="Set the temperature to get accurate or random result"
)

max_token_length = gr.Slider(
    minimum=32,
    maximum=2048,
    step=16,
    value=64,
    label="Token Length",
    # help="Set max tokens to generate maximum amount of text output"
)

model_kwargs = {
    "temperature": temperature,
    "max_new_tokens": max_token_length
}

def reponse(question):
    prompt = f"\nYou are an intelligent chatbot and expertise in everything.</s>\n\n{question}.\n"
    llm = HuggingFaceHub(
                repo_id=models,
                model_kwargs=model_kwargs
            )
    return llm(prompt)


with gr.Blocks() as app:
    with gr.Tab("LLM Inference"):
        model_input = gr.Textbox(
            label="Question",
            value="What is Machine Learning",
            interactive=True
        )
        predict_button = gr.Button("Submit")
        model_output = gr.Textbox(
            label="Answer",
            interactive=True,

        )
    predict_button.click(
        reponse,
        inputs=[model_input],
        outputs=[model_output]
    )

app.launch()