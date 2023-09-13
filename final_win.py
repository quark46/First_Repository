from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit
from instr import *
class FinalWindow(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()
        self.results
    def results(self):
        self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200 / 10)
        if int(self.exp.age) >= 15:
            if self.index >= 15:
                return txt_res1
            if 11 <= self.index <= 14.9:
                return txt_tes2
            if 6 <= self.index <= 10.9:
                return txt_res3
            if 0.5 <= self.index <= 5.9:
                return txt_res4
            if self.index <= 0.4:
                return txt_res5
        if 13 <= int(self.exp.age) <= 14:
            if self.index >= 16.5:
                return txt_res1
            if 12.5 <= self.index <= 16.4:
                return txt_tes2
            if 7.5 <= self.index <= 12.4:
                return txt_res3
            if 2 <= self.index <= 7.4:
                return txt_res4
            if self.index <= 1.9:
                return txt_res5
        if 11 <= int(self.exp.age) <= 12:
            if self.index >= 18:
                return txt_res1
            if 14 <= self.index <= 17.9:
                return txt_tes2
            if 9 <= self.index <= 13.9:
                return txt_res3
            if 3.5 <= self.index <= 8.9:
                return txt_res4
            if self.index <= 3.4:
                return txt_res5
        if 9 <=int(self.exp.age) <= 10:
            if self.index >= 19.5:
                return txt_res1
            if 15.5 <= self.index <= 19.4:
                return txt_tes2
            if 10.5 <= self.index <= 15.4:
                return txt_res3
            if 5 <= self.index <= 10.4:
                return txt_res4
            if self.index <= 4.9:
                return txt_res5
        if int(self.exp.age) <= 8:
            if self.index >= 21:
                return txt_res1
            if 17 <= self.index <= 20.9:
                return txt_tes2
            if 12 <= self.index <= 6.9:
                return txt_res3
            if 6.5 <= self.index <= 11.9:
                return txt_res4
            if self.index <= 6.4:
                return txt_res5
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.label1 = QLabel(txt_index + self.results())
        self.label2 = QLabel(txt_workheart + str(self.index))
        self.label1.setFont(QFont("Times", 36))
        self.label2.setFont(QFont("Times", 24))
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.label1, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.label2, alignment = Qt.AlignCenter)
        self.setLayout(self.v_line)