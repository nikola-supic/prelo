# Importing the libraries
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup
from ui.screen_search import Ui_SearchScreen

from datetime import datetime


# SEARCH SCREEN
class SearchScreen(QMainWindow, Ui_SearchScreen):
    def __init__(self, last_screen):
        super(SearchScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.user = last_screen.user

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