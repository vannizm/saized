from core.stt import STT

if __name__ == "__main__":
    stt = STT(model_size="small", device="cpu")
    text = stt.transcribe("audio/test_audio.ogg")
    print("Распознанный текст:")
    print(text)