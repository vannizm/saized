# core/brain.py
import ollama


class Brain:
    def __init__(self, model_name="gemma3:4b"):
        self.model = model_name
        self.system_prompt = (
    "Ты — Сэйзед, персональный голосовой ассистент. "
    "Отвечай кратко (одно-два предложения), дружелюбно, по делу. "
    "Всегда говори на русском языке."
)

    def think(self, user_input):
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_input},
        ]

        response = ollama.chat(
            model=self.model,
            messages=messages,
            keep_alive="10m",  # Держим модель в памяти 10 минут
            options={
                "num_ctx": 2048,
                "num_batch": 512,
                "num_predict": 150,
                "temperature": 0.7,
            },
        )

        content = response["message"]["content"]

        if not content or not content.strip():
            return "Извини, я не расслышал. Повтори, пожалуйста."

        return content.strip()