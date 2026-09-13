from core.tts import TTS
import os

if __name__ == "__main__":
    tts = TTS(voice="ru-RU-DmitryNeural")
    path = tts.speak("Привет, я Сайзед. Я готов помогать тебе с задачами системного и бизнес анализа.")
    full_path = os.path.abspath(path)
    print(f"Открываю: {full_path}")
    os.startfile(full_path)