import sys
##前端界面

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QSpacerItem, QSizePolicy, QComboBox, QHBoxLayout, QMainWindow, QWidget, QVBoxLayout, \
    QLineEdit, QFileDialog, QGraphicsDropShadowEffect

from PySide6.QtGui import QIcon, QColor, QFont, QPixmap, QPainter
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QStackedWidget
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel
from PySide6.QtGui import QFont
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
