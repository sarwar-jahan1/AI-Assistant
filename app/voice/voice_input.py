import sounddevice as sd
import soundfile as sf
from faster_whisper import WhisperModel
import os


class VoiceInput:

    def __init__(self):

        print("Loading Whisper Model...")

        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )

    def listen(self):

        filename = "voice.wav"

        samplerate = 16000
        duration = 5

        print("\n🎤 Speak now...")

        audio = sd.rec(
            int(duration * samplerate),
            samplerate=samplerate,
            channels=1,
            dtype="float32"
        )

        sd.wait()

        sf.write(filename, audio, samplerate)

        segments, info = self.model.transcribe(
            filename,
            language="en",
            beam_size=5
        )

        text = ""

        for segment in segments:
            text += segment.text + " "

        os.remove(filename)

        return text.strip().lower()