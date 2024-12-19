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

# 主界面
class HomeView(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        # # 在顶部添加一个弹簧间隔，用于向下移动内容
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Title Label
        title = QLabel("Handwriting Multi-Digit Recognition System")
        title_font = QFont("Times New Roman", 54, QFont.Bold)
        title_font.setItalic(True)  # 设置斜体
        title.setFont(title_font)
        title.setStyleSheet("""
                    color: #000000;  /* 设置标题颜色 */
                    font-size: 50px;
                    font-weight: bold;
                    padding: 10px;

                """)
        layout.addWidget(title)
        # 增加按钮之间的间距
        layout.addSpacing(60)

        button_layout = QHBoxLayout()

        # Start Prediction Button
        start_button = QPushButton("Start Prediction")
        start_button.setFixedWidth(500)
        start_button.setStyleSheet(self.button_style())
        start_button.clicked.connect(self.main_window.show_prediction)
        layout.addWidget(start_button, alignment=Qt.AlignCenter)

        layout.addLayout(button_layout)  # 将水平布局添加到主布局

        # 增加按钮之间的间距
        layout.addSpacing(20)

        button_layout2 = QHBoxLayout()

        # Instructions Button
        instructions_button = QPushButton("Instructions")
        instructions_button.setFixedWidth(500)
        instructions_button.setStyleSheet(self.button_style())
        instructions_button.clicked.connect(self.main_window.show_instruction)
        layout.addWidget(instructions_button, alignment=Qt.AlignCenter)

        # 在底部添加一个弹簧间隔，使按钮和底部有空间
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        layout.addLayout(button_layout2)  # 将水平布局添加到主布局

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