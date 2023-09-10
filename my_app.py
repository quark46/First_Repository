from PyQt5.QtCore import Core
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from instr import *
app = QApplication([])
class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_height, win_width)
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.button, alignment = Qt.AlignCenter)
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
app.exec_()