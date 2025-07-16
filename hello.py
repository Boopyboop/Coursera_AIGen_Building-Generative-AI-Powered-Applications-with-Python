import gradio as gr


def greet(name: str) -> str:
    """
    Returns a greeting message for the given name.

    Args:
        name (str): The name to greet.

    Returns:
        str: Greeting message.
    """
    return "Hello " + name + "!"


# Create Gradio interface wrapping the greet function
demo = gr.Interface(fn=greet, inputs="text", outputs="text")

# Launch the app on all available interfaces and port 7860
if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860, share=True)
