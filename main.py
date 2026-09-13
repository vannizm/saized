from core.stt import STT
from core.tts import TTS
from core.brain import Brain
from core.memory import Memory
import os

class Saized:
    def __init__(self):
        print("Инициализация Сайзеда...")
        self.stt = STT(model_size="small", device="cpu")
        self.tts = TTS(voice="ru-RU-DmitryNeural", rate="+30%")
        self.brain = Brain(model_name="qwen2.5:7b")
        self.memory = Memory()
        print("Сайзед готов.")

    def process_audio(self, audio_path):
        # 1. Слушаем
        print("Распознаю речь...")
        user_text = self.stt.transcribe(audio_path)
        print(f"Ты: {user_text}")

        # 2. Думаем
        print("Думаю...")
        response = self.brain.think(user_text)
        print(f"Сайзед: {response}")

        # 3. Говорим
        path = self.tts.speak(response)
        full_path = os.path.abspath(path)
        print(f"Воспроизвожу: {full_path}")
        os.startfile(full_path)  # откроет плеер

        # 4. Запоминаем
        self.memory.save(user_text, response)

if __name__ == "__main__":
    agent = Saized()
    agent.process_audio("audio/test_audio.ogg")
