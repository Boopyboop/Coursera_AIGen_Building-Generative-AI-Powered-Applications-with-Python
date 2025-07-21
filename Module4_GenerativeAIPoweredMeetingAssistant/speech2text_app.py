import torch
from transformers import pipeline
import gradio as gr
from pathlib import Path

# Load the model once at startup
pipe = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-tiny.en",
    chunk_length_s=30,
)

# Function to transcribe audio using Whisper
def transcript_audio(audio_file_path):
    # Check if the file path exists
    if not audio_file_path or not Path(audio_file_path).exists():
        return "Invalid or missing audio file."

    # Run transcription
    result = pipe(audio_file_path, batch_size=8)["text"]
    return result

# Define Gradio interface
audio_input = gr.Audio(sources="upload", type="filepath")  # Get uploaded file as path
output_text = gr.Textbox()

iface = gr.Interface(
    fn=transcript_audio,
    inputs=audio_input,
    outputs=output_text,
    title="Audio Transcription App",
    description="Upload an audio file to transcribe it with Whisper."
)

# Launch locally at http://127.0.0.1:7860
iface.launch(server_name="127.0.0.1", server_port=7860)
