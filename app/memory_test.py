from memory.database import *
from memory.memory import Memory

memory = Memory()

memory.save("name", "Sarwar")

print(memory.get("name"))