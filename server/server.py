"""
DOCSTRING:
    colors
    121212 - black - 18,18,18
    145c9e - blue - 20,92,158
    133758 - blue:hover - 19,55,88
    132535 - blue:pressed - 19,37,53
    e0e0e2 - white - 224,224,226

"""

# Importing the libraries
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup

from datetime import datetime
import logging

# Importing UI
from ui.screen_server import Ui_ServerScreen

# Import the modules
from module.log import LogScreen
from module.upload import UploadScreen
from module.backend import Server

# SERVER SCREEN
class ServerScreen(QMainWindow, Ui_ServerScreen):
    def __init__(self):
        super(ServerScreen, self).__init__()
        self.setupUi(self)
        self.log_file = 'logs/server_log.log'
        self.global_file = 'logs/global_chat.log'
        self.upload_file = 'logs/uploading.log'
        self.create_loggers()

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_chat.clicked.connect(self.toggle_chat)
        self.btn_download.clicked.connect(self.toggle_download)
        self.btn_logs.clicked.connect(self.server_logs)
        self.btn_start.clicked.connect(self.server_start)
        self.btn_restart.clicked.connect(self.server_restart)
        self.btn_shutdown.clicked.connect(self.server_shutdown)

        self.btn_global.clicked.connect(self.global_chat)
        self.btn_upload.clicked.connect(self.upload)
        self.btn_exit.clicked.connect(self.exit)
        self.click_time = get_time() + 1

        self.show()

        self.server = None
        self.check_buttons()


    def create_loggers(self):
        self.root_log = logging.getLogger('ROOT')
        self.root_log.setLevel(logging.INFO)
        handler = logging.FileHandler(self.log_file, 'a', 'utf-8')
        formatter = logging.Formatter('[ %(asctime)s ] %(message)s', datefmt='%d.%m.%y. %H:%M:%S')
        handler.setFormatter(formatter)
        self.root_log.addHandler(handler)
        
        self.upload_log = logging.getLogger('UPLOAD')
        self.upload_log.setLevel(logging.INFO)
        handler = logging.FileHandler(self.upload_file, 'a', 'utf-8')
        formatter = logging.Formatter('[ %(asctime)s ] %(message)s', datefmt='%d.%m.%y. %H:%M:%S')
        handler.setFormatter(formatter)
        self.upload_log.addHandler(handler)

        self.global_log = logging.getLogger('GLOBAL')
        self.global_log.setLevel(logging.INFO)
        handler = logging.FileHandler(self.global_file, 'w', 'utf-8')
        formatter = logging.Formatter('[ %(asctime)s ] %(message)s', datefmt='%d.%m.%y. %H:%M:%S')
        handler.setFormatter(formatter)
        self.global_log.addHandler(handler)


    def toggle_chat(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1
        
        self.button_anim(self.btn_chat)


    def toggle_download(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1

        self.button_anim(self.btn_download)


    def server_logs(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1

        if self.server is not None:
            self.logs = LogScreen(self, self.log_file)
            self.close()


    def server_start(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1

        if self.server is None:
            self.server = Server(self.root_log, self.global_log)
            self.server.start()

            self.check_buttons()


    def server_restart(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1

        if self.server is not None:
            self.server.restart()

            self.check_buttons()


    def server_shutdown(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1
        
        if self.server is not None:
            self.server.shutdown()
            del self.server
            self.server = None

            self.check_buttons()


    def check_buttons(self):
        if self.server is None:
            self.btn_restart.hide()
            self.btn_shutdown.hide()
            self.btn_start.show()

            self.label_shutdown.hide()
            self.label_restart.setText('Упали')
        else:
            self.btn_start.hide()
            self.btn_restart.show()
            self.btn_shutdown.show()

            self.label_shutdown.show()
            self.label_restart.setText('Рестарт')


    def global_chat(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1

        if self.server is not None:
            self.chat = LogScreen(self, self.global_file)
            self.close()


    def upload(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1

        self.upload = UploadScreen(self, self.upload_log)
        self.close()


    def exit(self):
        if self.server is None:
            self.close()
            sys.exit()


    def button_anim(self, btn):
        x = btn.pos().x()
        y = btn.pos().y()
        width = btn.width()
        height = btn.height()

        self.anim_1 = QPropertyAnimation(btn, b"geometry")
        self.anim_1.setDuration(150)
        self.anim_1.setStartValue(QtCore.QRect(x, y, width, height))
        self.anim_1.setEndValue(QtCore.QRect(x-20, y-20, width+40, height+40))
        self.anim_1.setEasingCurve(QtCore.QEasingCurve.Linear)

        self.anim_2 = QPropertyAnimation(btn, b"geometry")
        self.anim_2.setDuration(150)
        self.anim_2.setStartValue(QtCore.QRect(x-20, y-20, width+40, height+40))
        self.anim_2.setEndValue(QtCore.QRect(x, y, width, height))
        self.anim_2.setEasingCurve(QtCore.QEasingCurve.Linear)

        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.start()


def get_time():
    return datetime.now().timestamp()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ServerScreen()
    sys.exit(app.exec_())
