import cv2
from PIL import Image, ImageTk
import time

class CameraModel:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.frame = None
        self.is_running = False

    def get_frame(self):
        """
        获取摄像头的当前帧。
        返回帧以供更新视图。
        """
        ret, frame = self.cap.read()
        if ret:
            self.frame = frame
            return self.frame
        return None

    def capture_image(self):
        """
        捕获当前帧并保存为图片文件。
        """
        if self.frame is not None:
            filename = f"image_{int(time.time())}.jpg"
            cv2.imwrite(filename, self.frame)
            return filename
        else:
            return None

    def start(self):
        """
        启动摄像头。
        """
        if not self.is_running:
            self.is_running = True
            self.cap.open(0)

    def release_camera(self):
        """
        释放摄像头资源。
        """
        if self.cap.isOpened():
            self.cap.release()
        self.frame = None
        self.is_running = False
