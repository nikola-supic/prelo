# Importing the libraries
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup
from ui.screen_chat import Ui_ChatScreen

from datetime import datetime


# CHAT SCREEN
class ChatScreen(QMainWindow, Ui_ChatScreen):
    def __init__(self, last_screen, user):
        super(ChatScreen, self).__init__()
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