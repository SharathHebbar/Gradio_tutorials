import gradio as gr
import os
from langchain.llms import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class UserInterface():

    def __init__(self):
        gr.Warning("Warning: Some models may not work and some models may require GPU to run")
        gr.Text("An Open Source Chat Application")
        # gr.header("Open LLMs")

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
        self.models = gr.Dropdown(
            choices=models_name,
            label="Choose your models",
            # help="Choose your model",
        )

        self.temperature = gr.Slider(
            minimum=0.1,
            maximum=1.0,
            step=0.1,
            value=0.5,
            label='Temperature',
            # help="Set the temperature to get accurate or random result"
        )

        self.max_token_length = gr.Slider(
            minimum=32,
            maximum=2048,
            step=16,
            value=64,
            label="Token Length",
            # help="Set max tokens to generate maximum amount of text output"
        )

        self.model_kwargs = {
            "temperature": self.temperature,
            "max_new_tokens": self.max_token_length
        }

        # os.environ['HUGGINGFACEHUB_API_TOKEN'] = os.getenv("HF_KEY")
        

    def chat_app(self, context, question):

        try:
            prompt = f"\nYou are an intelligent chatbot and expertise in {context}.</s>\n\n{question}.\n"
            # template = f"\nYou are an intelligent chatbot and expertise in {context}.</s>\n\n{question}.\n"
            # prompt = PromptTemplate(
            #     template=template,
            #     input_variables=[
            #         'question',
            #         'context'
            #     ]
            # )
            print("_"*200)
            print(prompt)
            llm = HuggingFaceHub(
                repo_id=self.models,
                model_kwargs=self.model_kwargs
            )
            return llm(prompt)
            # if question:
            #     llm_chain = LLMChain(
            #         prompt=prompt,
            #         llm=llm,
            #     )

            #     result = llm_chain.run({
            #         "question": question,
            #         "context": context
            #     })

            #     if "Out of Context" in result:
            #         result = "Out of Context"
                
            #     return result

        except Exception as e:
            return str(e)

model = UserInterface()

app = gr.Blocks()

with app:
    gr.Markdown(
        """
        # Open LLM
        """
    )
    context = gr.Textbox(value="Machine Learning", label="Context")
    input_text = gr.Textbox(value="What is Machine Learning", label="Question")
    output_text = gr.Textbox(label="Response")
    
    btn = gr.Button("Predict")
    btn.click(
        fn=model.chat_app,
        inputs=[context, input_text],
        outputs=[output_text]
    )
    # model.chat_app(input_text)

app.launch()

# iface = gr.Interface(
#     fn=model.chat_app,
#     inputs=[
#         gr.Textbox(value="Machine Learning", label="Context"),
#         gr.Textbox(value="What is Machine Learning", label="Question")
#     ],
#     outputs=gr.Textbox(label="Response"),
#     live=True
# )
# btn = gr.Button("Predict")
# # btn.click(fn=model.chat_app(inputs[0], question))
# iface.launch()
