# core/stt.py
from faster_whisper import WhisperModel

class STT:
    def __init__(self, model_size="small", device="cpu"):
        # device="cuda" если хочешь использовать GPU (но на ноутбуке может не хватить памяти)
        print(f"Загрузка модели Whisper ({model_size})...")
        self.model = WhisperModel(model_size, device=device, compute_type="int8")
        print("Модель Whisper загружена.")

    def transcribe(self, audio_path):
        segments, info = self.model.transcribe(audio_path, beam_size=5, language="ru")
        text = " ".join([segment.text for segment in segments])
        return text.strip()
    