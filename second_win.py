from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit
from instr import *
from final_win import *
class TestWin(QWidget):
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
        self.h_line = QHBoxLayout()
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.label1 = QLabel(txt_name)
        self.label2 = QLabel(txt_hintage)
        self.label3 = QLabel(txt_test1)
        self.label4 = QLabel(txt_test2)
        self.label5 = QLabel(txt_test3)
        self.label6 = QLabel('00:00:15')
        self.button1 = QPushButton(txt_starttest1)
        self.button2 = QPushButton(txt_starttest2)
        self.button3 = QPushButton(txt_starttest3)
        self.button4 = QPushButton(next_c)
        self.edit1 = QLineEdit(txt_hintname)
        self.edit2 = QLineEdit(txt_hinttest1)
        self.edit3 = QLineEdit(txt_hinttest2)
        self.edit4 = QLineEdit(txt_hinttest3)
        self.edit5 = QLineEdit('0')
        #Layouts
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.l_line.addWidget(self.label1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.edit1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.label2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.edit2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.label3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.edit3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.label4, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.label5, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.edit4, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.edit5, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button4, alignment = Qt.AlignRight)
        self.h_line.addWidget(self.label6, alignment = Qt.AlignCenter)
        self.setLayout(self.h_line)
    def connects(self):
        self.button4.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.fw = FinalWindow()