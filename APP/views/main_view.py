import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QSpacerItem, QSizePolicy, QComboBox, QHBoxLayout, QMainWindow, QWidget, QVBoxLayout, \
    QLineEdit, QFileDialog, QGraphicsDropShadowEffect

from PySide6.QtGui import QIcon, QColor, QFont, QPixmap, QPainter
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QStackedWidget
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel
from PySide6.QtGui import QFont


##主界面
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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blind_helper")
        self.setGeometry(100, 100, 1000, 700)  # size
        # self.setWindowIcon(QIcon('icon.png'))

        # Set up the StackedWidget for switching between Home and Prediction views
        self.stacked_widget = QStackedWidget()
        self.home_view = HomeView(self)

        # Add views to the stacked widget
        self.stacked_widget.addWidget(self.home_view)

        self.setCentralWidget(self.stacked_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())