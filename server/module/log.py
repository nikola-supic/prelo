# Importing the libraries
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup

# Importing UI
from ui.screen_logs import Ui_LogScreen

# LOG SCREEN
class LogScreen(QMainWindow, Ui_LogScreen):
    def __init__(self, last_screen, log_file):
        super(LogScreen, self).__init__()
        self.setupUi(self)
        self.frame_border.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.frame.setGeometry(QtCore.QRect(10, 10, 0, 0))
        self.back = last_screen

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_back.clicked.connect(self.exit)

        self.show()
        self.widget.hide()

        # Opening animation
        anim_time = 750
        self.anim_1 = QPropertyAnimation(self.frame_border, b"geometry")
        self.anim_1.setDuration(anim_time)
        self.anim_1.setStartValue(QtCore.QRect(0, 280, 700, 0))
        self.anim_1.setEndValue(QtCore.QRect(0, 0, 700, 560))
        self.anim_1.setEasingCurve(QtCore.QEasingCurve.OutQuad)
        self.anim_1.start()

        self.anim_2 = QPropertyAnimation(self.frame, b"geometry")
        self.anim_2.setDuration(anim_time)
        self.anim_2.setStartValue(QtCore.QRect(10, 10, 680, 0))
        self.anim_2.setEndValue(QtCore.QRect(10, 10, 680, 540))
        self.anim_2.setEasingCurve(QtCore.QEasingCurve.OutQuad)
        self.anim_2.start()

        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.start()

        QtCore.QTimer.singleShot(anim_time, lambda: self.widget.show())

        # Enter logs
        with open(log_file, 'r') as file:
            self.log.setPlainText(file.read())
        

    def exit(self):
        self.back.show()
        self.close()