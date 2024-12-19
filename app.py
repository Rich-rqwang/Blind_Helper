<<<<<<< Updated upstream
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
=======
import sys
from PySide6.QtWidgets import QApplication
from APP.controllers.camera_controller import CameraController
from APP.controllers.speech_controller import SpeechController
from APP.controllers.ai_controller import ModelManager
from APP.views.main_view import MainWindow

def main():
    app = QApplication(sys.argv)  # 必须有 QApplication

    # 初始化控制器
    camera_controller = CameraController()
    speech_controller = SpeechController()
    ai_controller = ModelManager()

    # 初始化主窗口
    main_window = MainWindow(camera_controller, speech_controller, ai_controller)
    main_window.show()  # 显示主窗口

    sys.exit(app.exec())  # 进入事件循环，确保程序持续运行
>>>>>>> Stashed changes

if __name__ == "__main__":
    main()
