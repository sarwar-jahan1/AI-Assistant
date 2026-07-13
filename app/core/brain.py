from llm.ollama_client import OllamaClient
from memory.memory import Memory


class Brain:

    def __init__(self):
        self.ai = OllamaClient()
        self.memory = Memory()

    def think(self, command):

        command = command.lower()

        if command.startswith("my name is"):

            name = command.replace("my name is", "").strip()

            self.memory.save("name", name)

            return f"Nice to meet you, {name}. I will remember your name."

        if "what is my name" in command:

            name = self.memory.get("name")

            if name:

                return f"Your name is {name}."

            return "I don't know your name yet."

        return self.ai.ask(command)