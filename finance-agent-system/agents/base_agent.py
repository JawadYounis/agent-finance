import json
from abc import ABC, abstractmethod
from utils.llm_client import LLMClient

class BaseAgent(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.llm = LLMClient()

    @property
    @abstractmethod
    def system_prompt(self):
        pass

    def run(self, task):
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": task}
        ]
        response_text = self.llm.chat(messages)
        return self._parse_json(response_text)

    def _parse_json(self, text):
        try:
            clean_text = text.strip()
            if clean_text.startswith("```json"):
                clean_text = clean_text[7:]
            if clean_text.endswith("```"):
                clean_text = clean_text[:-3]
            return json.loads(clean_text.strip())
        except json.JSONDecodeError:
            return {"error": "Failed to parse JSON", "raw_response": text}
