from sentence_transformers import SentenceTransformer
import numpy as np

class EmbeddingEngine:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        # Load the model locally
        self.model = SentenceTransformer(model_name)

    def get_embedding(self, text):
        embedding = self.model.encode(text)
        return embedding

    @staticmethod
    def cosine_similarity(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
