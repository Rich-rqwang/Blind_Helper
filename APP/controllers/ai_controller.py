from APP.models.ai_model import AIModel

class AIController:
    def __init__(self):
        self.model = AIModel()

    def get_response(self, prompt):
        return self.model.respond(prompt)
