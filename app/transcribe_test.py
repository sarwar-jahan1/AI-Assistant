from voice.transcriber import Transcriber

transcriber = Transcriber()

text = transcriber.transcribe("voice.wav")

print("\nYou said:")
print(text)