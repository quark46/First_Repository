from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit
from instr import *
class FinalWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.label1 = QLabel(txt_index)
        self.label2 = QLabel(txt_workheart)
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.label1, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.label2, alignment = Qt.AlignCenter)
        self.setLayout(self.v_line)