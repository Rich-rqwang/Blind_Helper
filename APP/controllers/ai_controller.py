from APP.models.ai_model import AIModel
<<<<<<< Updated upstream

class AIController:
    def __init__(self):
        self.model = AIModel()

    def get_response(self, prompt):
        return self.model.respond(prompt)
=======
from APP.models.camera_model import CameraModel   #这个类实现的是虚假的摄像机类，仅仅有图像处理的类
from APP.models.speech_model import SpeechModel
from APP.models.true_camera_model import FakeCameraModel

class ModelManager:
    def __init__(self):
        self.text_model = AIModel()
        self.speech_model = SpeechModel()
        self.image_model = CameraModel()
        self.true_camera_model = FakeCameraModel()

    # 文字问答
    def process_text_quary(self, prompt):
        return self.text_model.respond(prompt)


    def process_voice_query(self, voice_input):
        pass

    def process_image_query(self, image_input):
        """
        :param image_input: 处理图片
        :return: 返回的是图片的描述
        """
        return self.image_model.respond(image_input)

    def process_cimera_query(self):
        """
        处理摄像机
        :return: 返回的是摄像机的描述
        """
        return self.true_camera_model.respond()
>>>>>>> Stashed changes
