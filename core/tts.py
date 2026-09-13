# core/tts.py
import os
from cartesia import Cartesia


class TTS:
    def __init__(self, voice_id=None):
        """
        voice_id: ID голоса Сергея из консоли Cartesia.
        API-ключ берётся из переменной окружения CARTESIA_API_KEY.
        """
        api_key = os.getenv("CARTESIA_API_KEY")
        if not api_key:
            raise ValueError(
                "Не найдена переменная окружения CARTESIA_API_KEY. "
                "Проверь, что она задана, и перезапусти VS Code / терминал."
            )

        self.voice_id = voice_id
        if not self.voice_id:
            raise ValueError("Не задан voice_id голоса Сергея")

        self.client = Cartesia(api_key=api_key)
        print(f"Cartesia TTS инициализирован. Voice ID: {self.voice_id}")

    def speak(self, text, output_path="audio/output.mp3"):
        """Синтезирует речь голосом Сергея и сохраняет в mp3."""
        # Создаём папку audio, если её нет
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        audio_bytes = self.client.tts.bytes(
            model_id="sonic-2",
            transcript=text,
            voice={"mode": "id", "id": self.voice_id},
            language="ru",
            output_format={
                "container": "mp3",
                "sample_rate": 44100,
                "bit_rate": 128000,
            },
        )

        with open(output_path, "wb") as f:
            f.write(audio_bytes)

        print(f"Аудио сохранено: {output_path}")
        return output_path