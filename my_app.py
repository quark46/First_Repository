from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from instr import *
from second_win import *
class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.hello_text.setFont(QFont("Times", 26))
        self.instruction = QLabel(txt_instruction)
        self.instruction.setFont(QFont("Times", 15))
        self.button = QPushButton(txt_next)
        self.button.setFont(QFont("Times", 15))
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.button, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)
    def connects(self):
        self.button.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = TestWin()
app = QApplication([])
window1 = MainWidget()
app.exec_()