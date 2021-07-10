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
from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup, QSequentialAnimationGroup

from datetime import datetime

# Importing UI
from ui.screen_server import Ui_ServerScreen
from ui.screen_logs import Ui_LogScreen

# Global variables
log_msgs = []

# Log screen
class LogScreen(QMainWindow, Ui_LogScreen):
    def __init__(self):
        super(LogScreen, self).__init__()
        self.setupUi(self)
        self.frame_border.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.frame.setGeometry(QtCore.QRect(10, 10, 0, 0))

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_back.clicked.connect(self.back)

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
        output = ''
        for msg in log_msgs:
            output += f'{msg}\n'
        self.log.setPlainText(output)


    def back(self):
        self.server = ServerScreen()
        self.close()


# Server screen
class ServerScreen(QMainWindow, Ui_ServerScreen):
    def __init__(self):
        super(ServerScreen, self).__init__()
        self.setupUi(self)

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_chat.clicked.connect(self.toggle_chat)
        self.btn_download.clicked.connect(self.toggle_download)
        self.btn_logs.clicked.connect(self.server_logs)
        self.btn_restart.clicked.connect(self.server_restart)
        self.btn_shutdown.clicked.connect(self.server_shutdown)
        self.click_time = get_time() + 2

        self.show()

    def toggle_chat(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1
        
        self.button_anim(self.btn_chat)
        add_log('Toggle chat system.')


    def toggle_download(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1

        self.button_anim(self.btn_download)
        add_log('Toggle download music system.')


    def server_logs(self):
        self.logs = LogScreen()
        self.close()

    def server_restart(self):
        pass


    def server_shutdown(self):
        add_log('Shutting server down...')

        if len(log_msgs):
            time = datetime.now()
            time_str = f'{time.day:02d}_{time.month:02d}_{time.year} {time.hour:02d}_{time.minute:02d}_{time.second:02d}'
            filename = f'logs/log_{time_str}.txt'

            with open(filename, 'w') as file:
                for msg in log_msgs:
                    file.write(f'{msg}\n')


        self.close()


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


def add_log(msg):
    global log_msgs
    time = datetime.now()
    time_str = f'[ {time.hour:02d}:{time.minute:02d}:{time.second:02d} ]'
    msg = f'{time_str} {msg}'
    log_msgs.append(msg)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ServerScreen()
    add_log('Starting server up...')
    sys.exit(app.exec_())