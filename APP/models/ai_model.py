import openai
from config import Config

class AIModel:
    def __init__(self):
        openai.api_key = Config.API_KEY

    def respond(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
