# Importing the libraries
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup
from ui.screen_tutorial import Ui_TutorialScreen
from module.main_menu import MenuScreen

# TUTORIAL SCREEN
class TutorialScreen(QMainWindow, Ui_TutorialScreen):
    def __init__(self, user=None, network=None, online=False):
        super(TutorialScreen, self).__init__()
        self.setupUi(self)
        self.user = user
        self.network = network
        self.online = online

        self.tutorial_step = 0
        self.arrows = [
            self.step_1,
            self.step_2,
            self.step_3,
            self.step_4,
            self.step_5,
            self.step_6,
            self.step_7,
        ]
        self.texts = [
            self.text_1,
            self.text_2,
            self.text_3,
            self.text_4,
            self.text_5,
            self.text_6,
            self.text_7,
        ] 
        self.buttons = [
            self.btn_play,
            self.btn_search,
            self.btn_friends,
            self.btn_chat,
            self.btn_settings,
            self.btn_about,
            self.btn_party,
        ]

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_next.clicked.connect(lambda: self.setup_tutorial(self.tutorial_step + 1))

        self.show()
        for step, text, button in zip(self.arrows, self.texts, self.buttons):
            step.hide()
            text.hide()
            button.hide()

        self.setup_tutorial(0)

    def setup_tutorial(self, step):
        if step == len(self.texts):
            self.menu = MenuScreen(self.user, self.network, self.online)
            self.close()
            return True

        self.arrows[step].show()
        self.texts[step].show()
        self.buttons[step].show()
        self.btn_next.setText(f'Следећи корак ({step + 1} / {len(self.texts)})')

        if step > 0:
            self.arrows[step - 1].hide()
            self.texts[step - 1].hide()
            self.buttons[step - 1].hide()
        else:
            self.btn_next.show()

        self.tutorial_step = step





