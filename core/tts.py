# core/tts.py
import os
import io
import queue
import threading
import sounddevice as sd
import soundfile as sf
from cartesia import Cartesia


class TTS:
    def __init__(self, voice_id=None):
        api_key = os.getenv("CARTESIA_API_KEY")
        if not api_key:
            raise ValueError("Не найдена CARTESIA_API_KEY")

        self.voice_id = voice_id
        if not self.voice_id:
            raise ValueError("Не задан voice_id голоса Сергея")

        self.client = Cartesia(api_key=api_key)
        print(f"Cartesia TTS инициализирован. Voice ID: {self.voice_id}")

    def speak(self, text):
        """Синтезирует речь и воспроизводит сразу, без файла."""
        if not text or not text.strip():
            return

        # Получаем mp3 байты от Cartesia
        response = self.client.tts.bytes(
            model_id="sonic-latest",
            transcript=text,
            voice=self.voice_id,
            language="ru",
            output_format={
                "container": "mp3",
                "sample_rate": 44100,
                "bit_rate": 128000,
            },
        )

        # Собираем все чанки в один байтовый поток
        audio_bytes = b"".join(response)

        # Декодируем mp3 в numpy-массив и играем через sounddevice
        data, samplerate = sf.read(io.BytesIO(audio_bytes), dtype="float32")
        sd.play(data, samplerate)
        sd.wait()  # ждём окончания воспроизведения
        print("🔊 Ответ воспроизведён.")