<<<<<<< Updated upstream
import openai
from config import Config

class AIModel:
    def __init__(self):
        openai.api_key = Config.API_KEY

    def respond(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
=======
import pyttsx3
from zhipuai import ZhipuAI


class AIModel:
    def __init__(self):

        self.api_key = "4a7b81a3b5b9d4761cfef9a330a438c6.RAZJtvyVkcALAHyB"
        self.conversation = []  # 用于存储对话上下文
        # 初始化语音引擎
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # 设置语速
        self.engine.setProperty('volume', 1.0)  # 设置音量
        self.engine.setProperty('voice', self.get_chinese_voice())  # 设置中文语音

    def get_chinese_voice(self):
        """
        获取支持中文的语音（如果有多个语音引擎）。
        """
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if "zh" in voice.languages or "Chinese" in voice.name:
                return voice.id
        return voices[0].id  # 如果未找到中文语音，则返回默认语音

    def respond(self, prompt):

        # 将用户输入添加到对话上下文
        self.conversation.append({"role": "user", "content": prompt})
        try:
            # 初始化智谱AI客户端
            client = ZhipuAI(api_key=self.api_key)

            # 调用智谱AI的 chat.completions.create 方法
            response = client.chat.completions.create(
                model="glm-4v-plus",
                messages=self.conversation  # 使用对话上下文
            )

            # 检查返回结果是否有效
            if hasattr(response, "choices") and response.choices:
                # 从 choices 中提取回答内容
                answer = response.choices[0].message.content
                # 将 AI 回答添加到对话上下文
                self.conversation.append({"role": "assistant", "content": answer})
                # 语音播报回答
                self.speak(answer)
                return answer
            else:
                return "未找到有效的回答内容"

        except Exception as e:
            return f"智谱AI调用失败：{str(e)}"

    def speak(self, text):
        """
        使用 pyttsx3 直接语音播报。
        :param text: 要播报的文本内容
        """
        try:
            self.engine.say(text)  # 将文本加入语音队列
            self.engine.runAndWait()  # 播放语音
        except Exception as e:
            print(f"语音播报失败：{e}")
>>>>>>> Stashed changes
