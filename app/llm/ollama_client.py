import requests


class OllamaClient:
    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.model = "llama3.2"

    def ask(self, prompt):

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(self.url, json=payload)

        if response.status_code == 200:
            return response.json()["response"]

        return "Sorry, I couldn't connect to Ollama."