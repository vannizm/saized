import ollama

class Brain:
    def __init__(self, model_name="qwen2.5:7b"):
        self.model = model_name
        self.system_prompt = """
        Ты — Сайзед, мой персональный ассистент.
        Ты работаешь локально на моем компьютере и помогаешь мне с задачами системного и бизнес-анализа.
        Твой стиль общения: спокойный, уверенный, дружелюбный, но по делу.
        Отвечай кратко и структурированно, если я не попрошу подробностей.
        """

    def think(self, user_input):
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_input}
        ]
        response = ollama.chat(model=self.model, messages=messages)
        return response['message']['content']