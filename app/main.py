from core.assistant import Assistant
from core.brain import Brain
from core.router import Router
from core.config import ASSISTANT_NAME
from core.parser import CommandParser
from core.planner import Planner

from commands import execute

assistant = Assistant(ASSISTANT_NAME)
brain = Brain()
router = Router()
parser = CommandParser()
planner = Planner()

assistant.greet()

while True:

    command = assistant.listen()

    command = parser.parse(command)

    if command == "exit":
        print("Goodbye!")
        break

    tasks = planner.split_tasks(command)

    for task in tasks:

        if router.is_automation(task):
            execute(task)

        else:
            response = brain.think(task)
            print("\n" + response + "\n")