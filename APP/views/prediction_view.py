from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QLineEdit, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from threading import Thread


class PredictionView(QWidget):
    def __init__(self, main_window, camera_controller, speech_controller, ai_controller):
        super().__init__()
        self.main_window = main_window
        self.camera_controller = camera_controller
        self.speech_controller = speech_controller
        self.ai_controller = ai_controller
        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout(self)

        # 返回主界面按钮
        back_button = QPushButton("返回主界面")
        back_button.setFixedWidth(200)
        back_button.setStyleSheet("""
            background-color: #FF7043;  /* 暖红色背景 */
            color: white;
            font-size: 14px;
            font-weight: bold;
            padding: 10px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
        """)
        back_button.clicked.connect(self.main_window.show_home)
        layout.addWidget(back_button, alignment=Qt.AlignLeft)

        # 聊天显示区域
        self.chat_display = QTextEdit(self)
        self.chat_display.setReadOnly(True)
        self.chat_display.setFont(QFont("Microsoft YaHei", 12))
        self.chat_display.setStyleSheet("""
            background-color: #FAFAFA;  /* 浅灰色背景 */
            color: #333333;  /* 深灰色文字 */
            border: 1px solid #E0E0E0;
            border-radius: 8px;
            padding: 10px;
        """)
        layout.addWidget(self.chat_display)

        # 输入区域
        self.input_area = QLineEdit(self)
        self.input_area.setPlaceholderText("请输入文字...")
        self.input_area.setFont(QFont("Microsoft YaHei", 12))
        self.input_area.setStyleSheet("""
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #B0B0B0;
            margin-top: 10px;
            background-color: #FFFFFF;
            color: #333333;
        """)
        layout.addWidget(self.input_area)

        # 按钮布局
        button_layout = QHBoxLayout()

        # 发送按钮
        send_button = QPushButton("发送", self)
        send_button.setStyleSheet("""
            background-color: #4CAF50;  /* 绿色背景 */
            color: white;
            font-size: 14px;
            padding: 10px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
        """)
        send_button.clicked.connect(self.send_message)
        button_layout.addWidget(send_button)

        # 语音输入按钮
        voice_button = QPushButton("语音输入", self)
        voice_button.setStyleSheet("""
            background-color: #FFEB3B;  /* 黄色背景 */
            color: black;
            font-size: 14px;
            padding: 10px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
        """)
        voice_button.clicked.connect(self.start_voice_input)
        button_layout.addWidget(voice_button)

        # 上传图片按钮
        image_button = QPushButton("上传图片", self)
        image_button.setStyleSheet("""
            background-color: #2196F3;  /* 蓝色背景 */
            color: white;
            font-size: 14px;
            padding: 10px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
        """)
        image_button.clicked.connect(self.upload_image)
        button_layout.addWidget(image_button)

        # 将按钮布局添加到主布局
        layout.addLayout(button_layout)

        # 设置整体布局对齐方式
        layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)

    def send_message(self):
        user_input = self.input_area.text()
        if user_input:
            self.chat_display.append(f"<b>你:</b> {user_input}")
            self.input_area.clear()

            print("having received message")
            # 使用线程获取AI回复，避免阻塞UI

            Thread(target=self.get_ai_response, args=(user_input,), daemon=True).start()




    def get_ai_response(self, prompt):
        response = self.ai_controller.process_text_quary(prompt)
        self.chat_display.append(f"<b>系统:</b> {response}")

    def start_voice_input(self):
        self.chat_display.append("<b>系统:</b> 正在听取语音...")
        # 使用线程处理语音输入和AI回复
        Thread(target=self.handle_voice_input, daemon=True).start()

    def handle_voice_input(self):
        voice_input = self.speech_controller.recognize_command()
        if voice_input:
            self.chat_display.append(f"<b>你:</b> {voice_input}")
            response = self.ai_controller.process_voice_query(voice_input)
            self.chat_display.append(f"<b>系统:</b> {response}")

    def upload_image(self):
        file, _ = QFileDialog.getOpenFileName(self, "选择图片文件", "", "Image Files (*.png *.jpg *.bmp)")
        if file:
            self.chat_display.append(f"<b>你上传了图片：</b>{file}")
            # 使用线程处理图片上传和识别
            Thread(target=self.handle_image_upload, args=(file,), daemon=True).start()

    def handle_image_upload(self, file_path):
        response = self.ai_controller.process_image_query(file_path)
        self.chat_display.append(f"<b>系统:</b> {response}")