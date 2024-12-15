
from APP.models.camera_model import CameraModel
from threading import Thread

class CameraController:
    def __init__(self):
        # 初始化摄像头模型
        self.camera_model = CameraModel()
        self.is_running = False

    def start_camera(self, ui_callback):
        """
        启动摄像头并将图像传递给视图进行显示。
        ui_callback: 视图中的回调函数，用于更新显示帧。
        """
        self.is_running = True

        def update_frames():
            while self.is_running:
                # 从摄像头读取帧
                frame = self.camera_model.get_frame()
                if frame is not None:
                    # 通过回调函数传递图像帧到视图
                    ui_callback(frame)
                else:
                    break
        # 启动线程来处理图像捕获
        Thread(target=update_frames, daemon=True).start()

    def capture_image(self):
        """
        捕获当前帧并保存为图片。
        """
        filename = self.camera_model.capture_image()
        return filename

    def stop_camera(self):
        """
        停止摄像头预览。
        """
        self.is_running = False
        self.camera_model.release_camera()

    def get_frame(self):
        """
        获取当前摄像头帧
        """
        return self.camera_model.get_frame()
