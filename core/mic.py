# core/mic.py
import os
import sounddevice as sd
import numpy as np
import soundfile as sf


class Recorder:
    def __init__(self, samplerate=16000):
        # Whisper ждёт 16 кГц — обязательно
        self.samplerate = samplerate
        print(f"Микрофон готов (sample rate: {samplerate} Hz)")

    def record_until_enter(self, output_path="audio/input.wav"):
        """Запись с микрофона: Enter — старт, Enter — стоп."""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        input("Нажми Enter, чтобы начать запись...")
        print("🎤 Записываю... Нажми Enter, чтобы остановить.")

        frames = []

        def callback(indata, frame_count, time_info, status):
            if status:
                print(f"[mic] {status}")
            frames.append(indata.copy())

        with sd.InputStream(
            samplerate=self.samplerate,
            channels=1,
            dtype="int16",
            callback=callback,
        ):
            input()

        audio = np.concatenate(frames, axis=0)
        sf.write(output_path, audio, self.samplerate)
        duration = len(audio) / self.samplerate
        print(f"Записано: {output_path} ({duration:.1f} сек)")
        return output_path