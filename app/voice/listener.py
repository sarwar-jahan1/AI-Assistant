import speech_recognition as sr


class Listener:

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):

        with sr.Microphone() as source:

            print("🎤 Speak now...")

            self.recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = self.recognizer.listen(source)

        try:

            command = self.recognizer.recognize_google(audio)

            print(f"You said: {command}")

            return command.lower()

        except sr.UnknownValueError:

            print("I couldn't understand.")

            return ""

        except sr.RequestError:

            print("No internet connection.")

            return ""