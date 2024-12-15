from APP.controllers.camera_controller import CameraController
from APP.controllers.speech_controller import SpeechController
from APP.controllers.ai_controller import AIController
from APP.views.main_view import MainWindow

def main():
    # 初始化控制器
    camera_controller = CameraController()
    speech_controller = SpeechController()
    ai_controller = AIController()

    # 初始化视图
    view = MainWindow(camera_controller, speech_controller, ai_controller)
    view.run()

if __name__ == "__main__":
    main()
