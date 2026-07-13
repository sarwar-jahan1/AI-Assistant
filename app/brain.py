from llm.ollama_client import OllamaClient


class Brain:

    def __init__(self):
        self.ai = OllamaClient()

    def think(self, command):

        return self.ai.ask(command)