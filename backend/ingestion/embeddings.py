import torch
from transformers import AutoTokenizer, AutoModel

class EmbeddingGenerator:
    def __init__(self, model_name="BAAI/bge-large-en"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

    def generate_embeddings(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()  # Get mean pooling of the last hidden state

# Example usage:
# generator = EmbeddingGenerator()
# embeddings = generator.generate_embeddings("Your text here")
