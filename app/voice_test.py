from voice.voice_input import VoiceInput

voice = VoiceInput()

command = voice.listen()

print("\nYou said:", command)