from voice.listener import Listener

listener = Listener()

while True:

    command = listener.listen()

    if command == "exit":
        break