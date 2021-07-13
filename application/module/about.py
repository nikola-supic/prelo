# Importing the libraries
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup
from ui.screen_about import Ui_AboutScreen

from datetime import datetime


# ABOUT SCREEN
class AboutScreen(QMainWindow, Ui_AboutScreen):
    def __init__(self, last_screen, user):
        super(AboutScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.user = user

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_back.clicked.connect(self.exit)
        self.click_time = get_time() + 2

        self.show()


    def exit(self):
        self.back.show()
        self.close()


def get_time():
    return datetime.now().timestamp()