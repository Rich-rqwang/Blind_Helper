<<<<<<< Updated upstream
import sys
from PySide6.QtWidgets import QApplication, QSpacerItem, QSizePolicy, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, \
    QWidget, QMainWindow, QStackedWidget, QGraphicsDropShadowEffect, QTextEdit, QLineEdit, QFileDialog
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

# HomeView class to display the main interface
class HomeView(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        # Set background image for the entire QWidget
        self.setStyleSheet("""
            QWidget {
                background-image: url('D:\作业及任务\Blind_Helper-main\Blind_Helper-main\APP\views\p1.png');  /* Add your image path */
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }
        """)

        # Add a spacer to move content down
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Title Label
        title = QLabel("基于大模型的智能对话系统")
        title_font = QFont("黑体", 54, QFont.Bold)
        title_font.setItalic(True)  # Set italic font
        title.setFont(title_font)
        title.setStyleSheet("""
                    color: #000000;  /* Set title color */
                    font-size: 50px;
                    font-weight: bold;
                    padding: 10px;
                """)
        layout.addWidget(title)

        # Add spacing between buttons
        layout.addSpacing(60)

        # Horizontal layout for buttons
        button_layout = QHBoxLayout()

        # Start Prediction Button
        start_button = QPushButton("开始对话")
        start_button.setFixedWidth(500)
        self.add_button_effect(start_button)
        start_button.clicked.connect(self.main_window.show_prediction)
        layout.addWidget(start_button, alignment=Qt.AlignCenter)

        layout.addLayout(button_layout)  # Add the horizontal layout for buttons

        # Add spacing between buttons
        layout.addSpacing(20)

        # Another button layout
        button_layout2 = QHBoxLayout()

        # Instructions Button
        instructions_button = QPushButton("使用说明")
        instructions_button.setFixedWidth(500)
        self.add_button_effect(instructions_button)
        instructions_button.clicked.connect(self.main_window.show_instruction)
        layout.addWidget(instructions_button, alignment=Qt.AlignCenter)

        # Add a spacer to the bottom for space between buttons and the bottom
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        layout.addLayout(button_layout2)  # Add the second horizontal layout for instructions button

    # Define button style for consistent look
    def button_style(self):
        return """
            background-color: #4CAF50;  /* Green background */
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 15px;
            border-radius: 5px;
            border: none;
            margin: 10px;
            text-align: center;
            cursor: pointer;
        """

    # Add a 3D effect to the button
    def add_button_effect(self, button):
        # Create a shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(3, 3)
        shadow.setColor(Qt.black)
        button.setGraphicsEffect(shadow)

        # Set normal style
        button.setStyleSheet(self.button_style())

        # Button click effect: darker when pressed
        button.pressed.connect(lambda: button.setStyleSheet(""" 
            background-color: #3e8e41;  /* Darker green when pressed */
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 15px;
            border-radius: 5px;
            border: none;
            margin: 10px;
            text-align: center;
            cursor: pointer;
        """))

        # Reset style after release
        button.released.connect(lambda: button.setStyleSheet(self.button_style()))

=======
from PySide6.QtWidgets import QMainWindow, QStackedWidget
from PySide6.QtCore import Qt
from APP.views.home_view import HomeView
from APP.views.prediction_view import PredictionView
from APP.views.instruction_view import InstructionView
>>>>>>> Stashed changes


# PredictionView class to display prediction page
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QLineEdit, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class PredictionView(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout(self)

        # Chat display area (takes up most of the space)
        self.chat_display = QTextEdit(self)
        self.chat_display.setReadOnly(True)
        self.chat_display.setFont(QFont("Microsoft YaHei", 12))
        self.chat_display.setStyleSheet("""
            background-color: rgba(250, 250, 250, 153);  /* Semi-transparent light grey */
            color: #333333;  /* Dark grey text for contrast */
            border: 1px solid #E0E0E0;
            border-radius: 8px;
            padding: 10px;
        """)
        layout.addWidget(self.chat_display, stretch=1)

        # Create a horizontal layout for the input field and buttons
        input_layout = QHBoxLayout()

        # Left circular button for toggling between voice/text input
        self.toggle_button = QPushButton("🎤", self)  # Default icon for voice
        self.toggle_button.setFixedSize(40, 40)
        self.toggle_button.setStyleSheet("""
            background-color: #FFEB3B;  /* Yellow background */
            color: black;
            font-size: 20px;
            border-radius: 20px;
            border: none;
            cursor: pointer;
        """)
        self.toggle_button.clicked.connect(self.toggle_input_mode)
        input_layout.addWidget(self.toggle_button)

        # Create a QStackedWidget to toggle between text and voice input
        self.input_stack = QStackedWidget(self)

        # Input field for text messages
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
        self.input_area.returnPressed.connect(self.send_text_message)  # Send message on Enter key press
        self.input_stack.addWidget(self.input_area)

        # Voice input button (for "Hold to Speak")
        self.voice_button = QPushButton("按住 说话", self)
        self.voice_button.setStyleSheet("""
            background-color: #FF7043;  /* 按钮的背景颜色 */
            color: white;  /* 按钮文字颜色 */
            font-size: 18px;  /* 设置字体大小 */
            padding: 12px 20px;  /* 调整按钮内部的边距，增加宽度和高度 */
            border-radius: 12px;  /* 圆角的大小 */
            border: none;  /* 去除边框 */
            cursor: pointer;  /* 鼠标悬停时显示手型光标 */
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);  /* 添加阴影效果，增加立体感 */
        """)
        self.voice_button.setFixedSize(250, 60)  # 增加按钮的宽度和高度，使其更显眼
        self.voice_button.setFlat(True)
        self.voice_button.setFixedSize(250, 50)  # Increased width to make the button longer
        self.voice_button.setFlat(True)
        self.input_stack.addWidget(self.voice_button)

        input_layout.addWidget(self.input_stack)

        # Right camera button for uploading images
        camera_button = QPushButton("📷", self)
        camera_button.setFixedSize(40, 40)
        camera_button.setStyleSheet("""
            background-color: #2196F3;  /* Blue background */
            color: white;
            font-size: 20px;
            border-radius: 20px;
            border: none;
            cursor: pointer;
        """)
        camera_button.clicked.connect(self.upload_image)
        input_layout.addWidget(camera_button)

        # Add the input layout to the main layout at the bottom
        layout.addLayout(input_layout)

        # Set the overall layout alignment
        layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)

    def toggle_input_mode(self):
        """Switch between voice input and text input."""
        if self.input_stack.currentWidget() == self.input_area:
            # Switch to voice input
            self.input_area.setVisible(False)
            self.toggle_button.setText("✏️")  # Switch to text mode icon
            self.activate_voice_input()
        else:
            # Switch to text input
            self.input_area.setVisible(True)
            self.toggle_button.setText("🎤")  # Switch to voice mode icon
            self.deactivate_voice_input()

        # Switch between the widgets in the stacked widget
        self.input_stack.setCurrentWidget(self.voice_button if self.input_stack.currentWidget() == self.input_area else self.input_area)

    def activate_voice_input(self):
        """Enable voice input mode."""
        self.voice_button.pressed.connect(self.start_voice_recording)
        self.voice_button.released.connect(self.stop_voice_recording)
        self.chat_display.append("<b>系统:</b> 请长按说话...")

    def deactivate_voice_input(self):
        """Return to normal text input mode."""
        self.input_area.setVisible(True)
        self.input_area.setPlaceholderText("请输入文字...")
        self.voice_button.pressed.disconnect(self.start_voice_recording)
        self.voice_button.released.disconnect(self.stop_voice_recording)

    def start_voice_recording(self):
        """Simulate voice recording started."""
        self.chat_display.append("<b>系统:</b> 正在录音...")

    def stop_voice_recording(self):
        """Simulate voice recording stopped and send the message."""
        voice_input = self.voice_to_text()  # Simulate voice input
        self.chat_display.append(f"<b>你:</b> {voice_input}")
        response = self.send_to_backend("text", voice_input)
        self.chat_display.append(f"<b>系统:</b> {response}")

    def voice_to_text(self):
        return "你好，我想问一下天气"

    def send_text_message(self):
        """Send text message when the Enter key is pressed."""
        text = self.input_area.text()
        if text.strip():
            self.chat_display.append(f"<b>你:</b> {text}")
            response = self.send_to_backend("text", text)
            self.chat_display.append(f"<b>系统:</b> {response}")
            self.input_area.clear()  # Clear the input field after sending

    def upload_image(self):
        file, _ = QFileDialog.getOpenFileName(self, "选择图片文件", "", "Image Files (*.png *.jpg *.bmp)")
        if file:
            self.chat_display.append(f"<b>你上传了图片：</b>{file}")
            response = self.send_to_backend("image", file)
            self.chat_display.append(f"<b>系统:</b> {response}")

    def send_to_backend(self, request_type, data):
        if request_type == "text":
            return f"处理文本：{data}"
        elif request_type == "image":
            return f"图片识别结果：{data}"
        return "无法处理请求"




class InstructionView(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout(self)

        # Back button
        back_button = QPushButton("返回主界面")
        back_button.setFixedWidth(200)
        back_button.setStyleSheet("""
            background-color: #FF7043;  /* Warm red background */
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

        # Instruction title
        title = QLabel("使用说明")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Microsoft YaHei", 20, QFont.Bold))
        title.setStyleSheet("color: #2E86C1;")  # Blue color for the title
        layout.addWidget(title)

        # Instruction text with HTML formatting
        instruction_text = """
        <p><b>本应用是一个基于大模型的智能对话系统，具有以下基本功能：</b></p>
        <ul>
            <li><b>文本输入：</b> 用户可以通过输入文字进行对话。输入框下方的“发送”按钮将会发送文本到系统，系统会返回对应的回答。</li>
            <li><b>语音输入：</b> 点击“语音输入”按钮后，应用会开始监听用户的语音并将其转化为文字。转换后的文本将会被发送给系统进行处理，返回回答。</li>
            <li><b>图片识别：</b> 点击“上传图片”按钮后，用户可以选择图片文件，系统会对图片进行处理并返回识别结果。</li>
            <li><b>多功能对话界面：</b> 系统同时支持文本、语音、图片三种输入方式，用户可以根据需要选择相应的输入方式与系统进行互动。</li>
        </ul>

        <p><b>使用步骤：</b></p>
        <ol>
            <li>启动应用，点击“开始对话”进入对话界面。</li>
            <li>在对话框中输入文本内容，并点击“发送”按钮。系统会根据输入的内容进行回答。</li>
            <li>点击“语音输入”按钮，开始录音并转换为文本，系统会进行自动回复。</li>
            <li>点击“上传图片”按钮，选择图片，系统会对图片进行识别并返回结果。</li>
            <li>随时点击“返回主界面”返回主界面，重新开始使用应用。</li>
        </ol>
        """

        instruction_label = QLabel(instruction_text)
        instruction_label.setAlignment(Qt.AlignLeft)
        instruction_label.setWordWrap(True)
        instruction_label.setFont(QFont("Microsoft YaHei", 12))
        instruction_label.setStyleSheet("""
            color: #333333;
            padding: 10px;
            font-size: 14px;
        """)
        layout.addWidget(instruction_label)

        self.setLayout(layout)



# Main window class to set up the entire application
class MainWindow(QMainWindow):
    def __init__(self, camera_controller, speech_controller, ai_controller):
        super().__init__()
<<<<<<< Updated upstream
        self.setWindowTitle("Blind_helper")
        self.setGeometry(100, 100, 200, 850)  # Set window size

        # Set the background for the entire window and scale the image to 30%
        self.setStyleSheet("""
            QMainWindow {
                background-image: url('D:/作业及任务/Blind_Helper-main/Blind_Helper-main/APP/views/p2.jpg');
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-size: 30%;  /* Scale the background image to 30% */
            }
        """)

        # Set up the StackedWidget to switch between views
        self.stacked_widget = QStackedWidget()

        # Create Home, Prediction, and Instruction views
        self.home_view = HomeView(self)
        self.prediction_view = PredictionView(self)
        self.instruction_view = InstructionView(self)
=======
        self.setWindowTitle("基于大模型的智能对话系统")
        self.setGeometry(100, 100, 1000, 700)  # 设置窗口大小

        self.camera_controller = camera_controller
        self.speech_controller = speech_controller
        self.ai_controller = ai_controller

        # 设置堆叠窗口以切换视图
        self.stacked_widget = QStackedWidget()
>>>>>>> Stashed changes

        # 创建主页、对话页和使用说明页
        self.home_view = HomeView(self)
        self.prediction_view = PredictionView(self, camera_controller, speech_controller, ai_controller)
        self.instruction_view = InstructionView(self)

        # 将视图添加到堆叠窗口
        self.stacked_widget.addWidget(self.home_view)
        self.stacked_widget.addWidget(self.prediction_view)
        self.stacked_widget.addWidget(self.instruction_view)

        self.setCentralWidget(self.stacked_widget)

    def show_home(self):
        self.stacked_widget.setCurrentWidget(self.home_view)

    def show_prediction(self):
        self.stacked_widget.setCurrentWidget(self.prediction_view)

    def show_instruction(self):
        self.stacked_widget.setCurrentWidget(self.instruction_view)


<<<<<<< Updated upstream
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
=======
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main = MainWindow()
#     main.show()
#     sys.exit(app.exec_())
>>>>>>> Stashed changes

