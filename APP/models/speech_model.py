import speech_recognition as sr
<<<<<<< Updated upstream
=======
from gtts import gTTS
import os

>>>>>>> Stashed changes

class SpeechModel:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

<<<<<<< Updated upstream
    def recognize_speech(self):
        with self.microphone as source:
            print("Listening for command...")
            audio = self.recognizer.listen(source)
            try:
                command = self.recognizer.recognize_google(audio)
=======

    def recognize_speech(self):
        """
        从麦克风捕获语音并转换为文本。
        """
        with self.microphone as source:
            print("Listening for command...")
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                command = self.recognizer.recognize_google(audio, language="zh-CN")
>>>>>>> Stashed changes
                return command.lower()
            except sr.UnknownValueError:
                return "Could not understand audio."
            except sr.RequestError as e:
                return f"Speech recognition error: {e}"
<<<<<<< Updated upstream
=======
            except Exception as e:
                return f"An error occurred: {str(e)}"

    def synthesize_speech(self, text):
        """
        使用 gTTS 将文本转换为语音并播放。
        """
        try:
            tts = gTTS(text=text, lang='zh')  # 'zh' for Chinese, 'en' for English
            filename = "response.mp3"
            tts.save(filename)
            os.system(f"start {filename}" if os.name == "nt" else f"mpg123 {filename}")  # Windows/Unix 播放
        except Exception as e:
            print(f"Speech synthesis error: {e}")

>>>>>>> Stashed changes
