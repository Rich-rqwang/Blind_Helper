from APP.models.camera_model import CameraModel

class CameraController:
    def __init__(self):
        self.model = CameraModel()

    def capture_image(self):
        return self.model.capture_image()
