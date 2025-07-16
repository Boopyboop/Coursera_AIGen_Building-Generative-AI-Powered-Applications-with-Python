import os
import glob
from PIL import Image
from transformers import Blip2Processor, Blip2ForConditionalGeneration


def generate_caption(image_path: str, processor, model, max_tokens: int = 50) -> str:
    """
    Generate a caption for a given image using the BLIP-2 model.

    Args:
        image_path (str): Path to the input image file.
        processor: Hugging Face processor for image preprocessing.
        model: Hugging Face model for caption generation.
        max_tokens (int): Maximum number of tokens in the generated caption.

    Returns:
        str: Generated caption text.
    """
    try:
        raw_image = Image.open(image_path).convert("RGB")
        inputs = processor(raw_image, return_tensors="pt")
        output = model.generate(**inputs, max_new_tokens=max_tokens)
        caption = processor.decode(output[0], skip_special_tokens=True)
        return caption
    except Exception as e:
        return f"Error processing {os.path.basename(image_path)}: {e}"


def process_image_directory(
    image_dir: str,
    image_extensions: list[str],
    output_file: str,
    processor,
    model
) -> None:
    """
    Generate captions for all images in a directory and save results to a file.

    Args:
        image_dir (str): Directory containing the images.
        image_extensions (list[str]): List of allowed image file extensions.
        output_file (str): Path to the output text file for storing captions.
        processor: Pretrained image processor.
        model: Pretrained BLIP-2 model.
    """
    with open(output_file, "w", encoding="utf-8") as f:
        for ext in image_extensions:
            pattern = os.path.join(image_dir, f"*.{ext}")
            for image_path in glob.glob(pattern):
                caption = generate_caption(image_path, processor, model)
                f.write(f"{os.path.basename(image_path)}: {caption}\n")


if __name__ == "__main__":
    # Define the image directory and output file
    image_directory = "/path/to/your/images"  # <-- Replace with your actual path
    valid_extensions = ["jpg", "jpeg", "png"]
    output_filename = "captions.txt"

    # Load the pretrained processor and model
    processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b")
    model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b")

    # Generate captions
    process_image_directory(
        image_dir=image_directory,
        image_extensions=valid_extensions,
        output_file=output_filename,
        processor=processor,
        model=model
    )
