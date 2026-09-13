from core.mic import Recorder
from core.stt import STT
from core.tts import TTS
from core.brain import Brain
from core.memory import Memory
import os

class Saized:
    def __init__(self):
        print("Инициализация Сайзеда...")
        self.stt = STT(model_size="small", device="cpu")
        self.tts = TTS(voice_id="1e4176b1-3db9-44d6-a601-4fe68b041942")
        self.brain = Brain()
        self.memory = Memory()
        self.recorder = Recorder()
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
        self.tts.speak(response)

        # 4. Запоминаем
        self.memory.save(user_text, response)

if __name__ == "__main__":
    agent = Saized()
    print("Говори в микрофон. Ctrl+C — выход.\n")
    while True:
        try:
            path = agent.recorder.record_until_enter()
            agent.process_audio(path)
            print()
        except KeyboardInterrupt:
            print("\nПока!")
            break
