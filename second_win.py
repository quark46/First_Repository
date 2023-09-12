from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit
from instr import *
from final_win import *
time1 = QTime(0, 0, 15)
time2 = QTime(0, 0, 45)
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
        self.label1.setFont(QFont("Times", 12))
        self.label2 = QLabel(txt_hintage)
        self.label2.setFont(QFont("Times", 12))
        self.label3 = QLabel(txt_test1)
        self.label3.setFont(QFont("Times", 12))
        self.label4 = QLabel(txt_test2)
        self.label4.setFont(QFont("Times", 12))
        self.label5 = QLabel(txt_test3)
        self.label5.setFont(QFont("Times", 12))
        self.text_timer = QLabel('00:00:15')
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.button1 = QPushButton(txt_starttest1)
        self.button1.setFont(QFont("Times", 12))
        self.button2 = QPushButton(txt_starttest2)
        self.button2.setFont(QFont("Times", 12))
        self.button3 = QPushButton(txt_starttest3)
        self.button3.setFont(QFont("Times", 12))
        self.button4 = QPushButton(next_c)
        self.button4.setFont(QFont("Times", 12))
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
        self.h_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)
        self.setLayout(self.h_line)
    def connects(self):
        self.button4.clicked.connect(self.next_click)
        self.button1.clicked.connect(self.timer_test)
        self.button2.clicked.connect(self.timer_sits)
    def timer_test(self):
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.timer1Event)
    def timer1Event(self):
        global time1
        time1 = time1.addSecs(-1)
        self.text_timer.setText(time1.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time1.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer_sits(self):
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.timer2Event)
    def timer2Event(self):
        global time2
        time2 = time2.addSecs(-1)
        self.text_timer.setText(time2.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time2.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def next_click(self):
        self.hide()
        self.fw = FinalWindow()