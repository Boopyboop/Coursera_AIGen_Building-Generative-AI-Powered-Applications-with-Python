import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


def caption_image(input_image: np.ndarray) -> str:
    """
    Generate a caption from an image.

    Args:
        input_image (np.ndarray): Image input as NumPy array.

    Returns:
        str: Caption string.
    """
    try:
        raw_image = Image.fromarray(input_image).convert("RGB")
        inputs = processor(raw_image, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=50)
        caption = processor.decode(outputs[0], skip_special_tokens=True)
        return caption
    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks() as demo:
    image = gr.Image(type="numpy", label="Upload an image")
    output = gr.Textbox(label="Caption")
    image.change(fn=caption_image, inputs=image, outputs=output)

demo.launch()