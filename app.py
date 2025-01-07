import gradio as gr

def predict(text):
    return f"Hello, {text}!"

iface = gr.Interface(fn=predict, inputs="text", outputs="text")
iface.launch()
