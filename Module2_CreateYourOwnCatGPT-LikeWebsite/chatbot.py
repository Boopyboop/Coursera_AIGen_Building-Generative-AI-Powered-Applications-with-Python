"""
chatbot.py

This module loads a pretrained conversational model (BlenderBot 400M) and provides
an interactive text interface for chatting with the model. It maintains a simple
conversation history to simulate continuity in dialogue.

Note:
This script is meant to be imported and executed from a main controller (e.g., app.py).
"""

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Define the model name (downloaded on first use and cached locally thereafter)
MODEL_NAME = "facebook/blenderbot-400M-distill"

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

# Initialize the conversation history
conversation_history = []

while True:
    # Combine past conversation turns into a single string
    history_string = "\n".join(conversation_history)

    # Prompt user for input
    input_text = input("> ")

    # Tokenize input along with conversation history
    inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")

    # Generate a response using the model
    outputs = model.generate(**inputs)

    # Decode the model output into a readable string
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # Display the chatbot's response
    print(response)

    # Update conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)
