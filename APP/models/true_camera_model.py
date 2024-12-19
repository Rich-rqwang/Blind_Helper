"""
@Project :Blind_Helper
@File    :true_camera_model.py
@IDE     :PyCharm
@Author  :22gcdu 
@Date    :2024/12/18 下午9:31
"""

import cv2
from PIL import Image , ImageTk
import time
import base64
import pyttsx3
import base64
import urllib
import requests
import os
import json
from zhipuai import ZhipuAI

'''
使用这个类可以自动用摄像头，捕捉图片
'''


class FakeCameraModel :
    def __init__(self) :
        self.cap = cv2.VideoCapture(0)
        self.conversation = []  # 用于存储对话上下文

        self.url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/image-understanding/request" + self.get_access_token()
        self.url_1 = "https://aip.baidubce.com/rest/2.0/image-classify/v1/image-understanding/request?access_token=24.94c61bfbba3a02d7ebce8aa13c292e03.2592000.1736994196.282335-116707290"

        self.frame = None
        self.is_running = False
        self.api_key = "4a7b81a3b5b9d4761cfef9a330a438c6.RAZJtvyVkcALAHyB"

        self.engine = pyttsx3.init()
        self.engine.setProperty('rate' , 150)  # 设置语速
        self.engine.setProperty('volume' , 1.0)  # 设置音量
        self.engine.setProperty('voice' , self.get_chinese_voice())  # 设置中文语音

    def get_chinese_voice(self) :
        """
        获取支持中文的语音（如果有多个语音引擎）。
        """
        voices = self.engine.getProperty('voices')
        for voice in voices :
            if "zh" in voice.languages or "Chinese" in voice.name :
                return voice.id
        return voices[0].id  # 如果未找到中文语音，则返回默认语音

    def encode_image_for_api(self , image) :
        """
        Encode image as base64 for API transmission.
        """
        _ , buffer = cv2.imencode('.jpg' , image)
        return base64.b64encode(buffer).decode('utf-8')

    def get_access_token(self) :
        """
        使用 AK，SK 生成鉴权签名（Access Token）
        :return: access_token，或是None(如果错误)
        """
        API_KEY = "RyDKwjd6WRSnkHSbgPRCYsoR"
        SECRET_KEY = "ojEMkI5lP8Tvv9zVUj2UuJnGpkskMUb2"
        url = "https://aip.baidubce.com/oauth/2.0/token"
        params = {"grant_type" : "client_credentials" , "client_id" : API_KEY , "client_secret" : SECRET_KEY}
        return str(requests.post(url , params = params).json().get("access_token"))

    def process_image(self , image_path) :
        """
        处理上传的图片文件。
        :param image_path: 图片文件路径
        :return: base64编码的图片
        """

        if not os.path.exists(image_path) :
            print(f"给定的图像路径不存在：{image_path}")
            return None
        frame = cv2.imread(image_path)
        if frame is not None :
            rgb_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
            jpeg_frame = cv2.imencode('.jpg' , rgb_frame)[1]
            base64_encoded_frame = base64.b64encode(jpeg_frame).decode('utf-8')
            return base64_encoded_frame
        else :
            print("未能读取到图像")
            return None

    def get_result(self , taskid) :
        # 构建UR
        url_2 = "https://aip.baidubce.com/rest/2.0/image-classify/v1/image-understanding/get-result?access_token=24.94c61bfbba3a02d7ebce8aa13c292e03.2592000.1736994196.282335-116707290"
        # 构建payload，使用提取到的task_id

        payload = json.dumps({
            "task_id" : str(taskid)
        })

        headers = {
            'Content-Type' : 'application/json'
        }

        response1 = requests.request("POST" , url_2 , headers = headers , data = payload)

        response_json1 = response1.json()  # 将响应文本解析为JSON对象

        # 提取字段的值

        # subject_result = response_json.get('result' , {}).get('subject_result' , [])
        description1 = None

        description1 = response_json1.get("result" , {}).get('description' , [])

        response2 = requests.request("POST" , url_2 , headers = headers , data = payload)

        response_json2 = response2.json()  # 将响应文本解析为JSON对象

        # 提取字段的

        # subject_result = response_json.get('result' , {}).get('subject_result' , [])

        description2 = response_json2.get("result" , {}).get('description' , [])

        description = None

        if description1 == None and description2 == None :
            description = None
        if description1 != None :
            description = description1

        if description1 == None and description2 != None :
            description = description2

        return description

    def  show_cam_image(self):
        try:
            # 尝试打开摄像头
            stream = cv2.VideoCapture(0)

            # 检查是否成功打开
            if not stream.isOpened():
                print("未成功打开摄像头")
                return

            # 读取一帧图像
            ret, frame = stream.read()

            # 如果成功读取帧
            if ret:

                # 保存图片
                image_path = "./camera.jpeg"
                cv2.imwrite(image_path, frame)

                # 将帧从BGR转换为RGB
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # 将帧编码为JPEG格式
                jpeg_frame = cv2.imencode('.jpg', rgb_frame)[1]

                # 将JPEG格式的帧转换为Base64编码
                base64_encoded_frame = base64.b64encode(jpeg_frame).decode('utf-8')

                return base64_encoded_frame
            else:
                print("未能读取到图像帧")

        except Exception as e:
            print(f"摄像头操作出错：{e}")
        finally:
            # 确保释放摄像头资源
            stream.release()

    def respond(self) :



        # # print("r" + str("'") + str(f"{image_input}") +str("'"))
        # image_input = str("r" + str("'") + str(f"{image_input}") +str("'"))
        # image_input = image_input.replace("\\","/")
        # print(image_input)
        #
        image_data = self.show_cam_image()

        # 初始化模型 question 参数可以修改
        payload = json.dumps({
            "image" : image_data ,
            "question" : "图像中有什么" ,
            "output_CHN" : True
        })
        headers = {
            'Content-Type' : 'application/json'
        }
        response = requests.request("POST" , self.url_1 , headers = headers , data = payload)
        response_json = response.json()  # 将响应文本解析为JSON对象
        result = response_json.get("result")['task_id']  # 提取result字段,'task_id'里面的值

        time.sleep(8)

        description = self.get_result(taskid = result)

        if description == None :
            print("对不起，系统调佣过快，请再试一次")  # 前段应该显示

        print(description)  # 前段应该显示

        self.conversation.append({"role" : "assistant" , "content" : description})

        self.speak(answer = description)

        self.conversation.append({"role" : "assistant" , "content" : description})

        return description

    def speak(self , answer) :

        try :
            self.engine.say(answer)  # 将文本加入语音队列
            self.engine.runAndWait()  # 播放语音
        except Exception as e :
            print(f"语音播报失败：{e}")

    def get_frame(self) :
        """
        获取摄像头的当前帧。
        返回帧以供更新视图。
        """
        ret , frame = self.cap.read()
        if ret :
            self.frame = frame
            return self.frame
        return None

    def capture_image(self) :
        """
        捕获当前帧并保存为图片文件。
        """
        if self.frame is not None :
            filename = f"image_{int(time.time())}.jpg"
            cv2.imwrite(filename , self.frame)
            return filename
        else :
            return None

    def start(self) :
        """
        启动摄像头。
        """
        if not self.is_running :
            self.is_running = True
            self.cap.open(0)

    def release_camera(self) :
        """
        释放摄像头资源。
        """
        if self.cap.isOpened() :
            self.cap.release()
        self.frame = None
        self.is_running = False


def process_image(image_path) :
    """
    处理上传的图片文件。
    :param image_path: 图片文件路径
    :return: base64编码的图片
    """

    if not os.path.exists(image_path) :
        print(f"给定的图像路径不存在：{image_path}")
        return None
    frame = cv2.imread(image_path)
    if frame is not None :
        rgb_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
        jpeg_frame = cv2.imencode('.jpg' , rgb_frame)[1]
        base64_encoded_frame = base64.b64encode(jpeg_frame).decode('utf-8')
        return base64_encoded_frame
    else :
        print("未能读取到图像")
        return None


def get_result(taskid) :
    # 构建UR
    url_2 = "https://aip.baidubce.com/rest/2.0/image-classify/v1/image-understanding/get-result?access_token=24.94c61bfbba3a02d7ebce8aa13c292e03.2592000.1736994196.282335-116707290"
    # 构建payload，使用提取到的task_id

    payload = json.dumps({
        "task_id" : str(taskid)
    })

    headers = {
        'Content-Type' : 'application/json'
    }

    response1 = requests.request("POST" , url_2 , headers = headers , data = payload)

    response_json1 = response1.json()  # 将响应文本解析为JSON对象

    # 提取字段的值

    # subject_result = response_json.get('result' , {}).get('subject_result' , [])
    description1 = None

    description1 = response_json1.get("result" , {}).get('description' , [])

    response2 = requests.request("POST" , url_2 , headers = headers , data = payload)

    response_json2 = response2.json()  # 将响应文本解析为JSON对象

    # 提取字段的

    # subject_result = response_json.get('result' , {}).get('subject_result' , [])

    description2 = response_json2.get("result" , {}).get('description' , [])

    description = None

    if description1 == None and description2 == None :
        description = None
    if description1 != None :
        description = description1

    if description1 == None and description2 != None :
        description = description2

    return description


### 测试功能

#使用案例
if __name__ == "__main__":
    model = FakeCameraModel()
    output = model.respond()
    print(output)


