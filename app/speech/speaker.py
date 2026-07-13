import asyncio
import edge_tts
import pygame
import os
import uuid


class Speaker:

    async def speak_async(self, text):

        filename = f"{uuid.uuid4()}.mp3"

        communicate = edge_tts.Communicate(
            text=text,
            voice="en-US-GuyNeural"
        )

        await communicate.save(filename)

        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            await asyncio.sleep(0.1)

        pygame.mixer.music.stop()
        pygame.mixer.quit()

        os.remove(filename)

    def speak(self, text):
        asyncio.run(self.speak_async(text))