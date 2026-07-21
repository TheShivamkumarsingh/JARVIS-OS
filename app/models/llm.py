from ollama import chat


class LLM:

    def __init__(self, model="llama3.2:3b"):
        self.model = model

    def generate(self, system_prompt, user_prompt):

        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        return response["message"]["content"]