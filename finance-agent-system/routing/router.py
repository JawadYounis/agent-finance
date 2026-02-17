from utils.embeddings import EmbeddingEngine

class TaskRouter:
    def __init__(self, agents_config):
        self.engine = EmbeddingEngine()
        self.agents_config = agents_config  
        self.agent_embeddings = {
            name: self.engine.get_embedding(desc)
            for name, desc in agents_config.items()
        }

    def route_task(self, task_text):
        task_embedding = self.engine.get_embedding(task_text)
        
        best_agent = None
        highest_similarity = -1.0

        for name, agent_emb in self.agent_embeddings.items():
            similarity = self.engine.cosine_similarity(task_embedding, agent_emb)
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_agent = name
        
        return best_agent
