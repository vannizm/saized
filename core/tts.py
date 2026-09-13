import edge_tts
import asyncio

class TTS:
    def __init__(self, voice="ru-RU-DmitryNeural", rate="+30%"):
        print("Инициализация Edge TTS...")
        self.voice = voice
        self.rate = rate  # "+30%" — ускорение на 30%
        print(f"Голос: {voice}, скорость: {rate}")

    async def _speak_async(self, text, output_path):
        communicate = edge_tts.Communicate(text, self.voice, rate=self.rate)
        await communicate.save(output_path)

    def speak(self, text, output_path="audio/output.mp3"):
        asyncio.run(self._speak_async(text, output_path))
        print(f"Аудио сохранено: {output_path}")
        return output_path