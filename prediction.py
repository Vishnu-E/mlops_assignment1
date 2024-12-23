from model import pipe


# Input text for prediction
texts = [
    "I love using Hugging Face models!",
    "This is a terrible experience.",
    "I am so happy right now."
]

# Make predictions
predictions = pipe(texts)

# Output predictions
for text, prediction in zip(texts, predictions):
    print(f"Text: {text}")
    print(f"Label: {prediction['label']}, Confidence: {prediction['score']:.2f}\n")