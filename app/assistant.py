class Assistant:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("=" * 50)
        print(f"Hello! I am {self.name}")
        print("Your Personal AI Assistant")
        print("=" * 50)

    def listen(self):
        command = input(f"{self.name} > ")
        return command.lower()