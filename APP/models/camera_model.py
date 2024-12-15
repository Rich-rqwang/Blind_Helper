import cv2
import time

class CameraModel:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def capture_image(self):
        ret, frame = self.cap.read()
        if ret:
            filename = f"image_{int(time.time())}.jpg"
            cv2.imwrite(filename, frame)
            return filename
        return None

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
