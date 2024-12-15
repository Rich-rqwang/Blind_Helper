from APP.models.speech_model import SpeechModel

class SpeechController:
    def __init__(self):
        self.model = SpeechModel()

    def recognize_command(self):
        return self.model.recognize_speech()
