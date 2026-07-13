from assistant import Assistant
from brain import Brain
from config import ASSISTANT_NAME

assistant = Assistant(ASSISTANT_NAME)
brain = Brain()

assistant.greet()

while True:

    command = assistant.listen()

    if command == "exit":
        print("Goodbye!")
        break

    response = brain.think(command)

    print()
    print(response)
    print()