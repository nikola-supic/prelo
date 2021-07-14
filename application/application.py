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
from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup

# Importing UI
from ui.screen_loading import Ui_LoadingScreen
from ui.screen_welcome import Ui_WelcomeScreen

# Import the modules
from module.main_menu import MenuScreen
from module.popup import PopupError

# Import database functions
import database as db

# Import network
from network import Network

# Importing libraries for social media buttons
import webbrowser
from social_media import links

# Global variables
counter = 0
db_conn = False
db_user = None
network_conn = None

# Welcome screen (login/register)
class WelcomeScreen(QMainWindow, Ui_WelcomeScreen):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        self.setupUi(self)
        self.frame_border.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.frame.setGeometry(QtCore.QRect(10, 10, 0, 0))
        self.login_username.setText('dzast_nikola')
        self.login_pw.setText('123456789')

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.login_form = True
        self.btn_login.clicked.connect(self.login)
        self.btn_to_register.clicked.connect(lambda: self.stacked_pages.setCurrentWidget(self.page_register))
        self.btn_register.clicked.connect(self.register)
        self.btn_to_login.clicked.connect(lambda: self.stacked_pages.setCurrentWidget(self.page_login))

        self.btn_fb.clicked.connect(lambda: webbrowser.open(links['fb']))
        self.btn_ig.clicked.connect(lambda: webbrowser.open(links['ig']))
        self.btn_yt.clicked.connect(lambda: webbrowser.open(links['yt']))
        self.btn_in.clicked.connect(lambda: webbrowser.open(links['in']))
        self.btn_git.clicked.connect(lambda: webbrowser.open(links['git']))

        self.show()
        self.widget.hide()

        # Opening animation
        anim_time = 1000
        self.anim_1 = QPropertyAnimation(self.frame_border, b"geometry")
        self.anim_1.setDuration(anim_time)
        self.anim_1.setStartValue(QtCore.QRect(0, 300, 490, 0))
        self.anim_1.setEndValue(QtCore.QRect(0, 0, 490, 600))
        self.anim_1.setEasingCurve(QtCore.QEasingCurve.OutQuad)
        self.anim_1.start()

        self.anim_2 = QPropertyAnimation(self.frame, b"geometry")
        self.anim_2.setDuration(anim_time)
        self.anim_2.setStartValue(QtCore.QRect(10, 10, 470, 0))
        self.anim_2.setEndValue(QtCore.QRect(10, 10, 470, 580))
        self.anim_2.setEasingCurve(QtCore.QEasingCurve.OutQuad)
        self.anim_2.start()

        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.start()

        QtCore.QTimer.singleShot(anim_time, lambda: self.widget.show())


    def register(self):
        first_name = self.reg_first.text()
        last_name = self.reg_last.text()
        username = self.reg_username.text()
        email = self.reg_email.text()
        password = self.reg_pw.text()
        confirm_pw = self.reg_pw_2.text()

        registered = db.check_register(first_name, last_name, username, email, password, confirm_pw)
        if not registered:
            self.popup = PopupError(self, 'Неку од информација сте унијели погрешно.', 'Неуспјешна регистрација')
            self.close()
        else:
            global db_user
            user = db.check_login(username, password)
            db_user = user
            self.menu = MenuScreen(user, True)
            self.close()


    def login(self):
        username = self.login_username.text()
        password = self.login_pw.text()

        user = db.check_login(username, password)
        if not user:
            self.popup = PopupError(self, 'Погрешно корисничко име или лозинка.', 'Неуспјешна пријава')
            self.close()
        else:
            global db_user
            db_user = user
            self.menu = MenuScreen(user, True)
            self.close()


# Loading screen
class LoadingScreen(QMainWindow, Ui_LoadingScreen):
    def __init__(self):
        super(LoadingScreen, self).__init__()
        self.setupUi(self)

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Loading timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(20)

        # Change Texts
        self.label_description.setText("<strong>ДОБРОДОШЛИ</strong> НА <strong>ПРЕЛО</strong>")
        QtCore.QTimer.singleShot(1000, lambda: self.label_description.setText("<strong>УЧИТАВАЊЕ</strong> БАЗЕ ПОДАТАКА"))
        QtCore.QTimer.singleShot(2000, lambda: self.label_description.setText("<strong>УЧИТАВАЊЕ</strong> ИНТЕРФЕЈСА"))
        QtCore.QTimer.singleShot(3000, lambda: self.label_description.setText("РАДИО <strong>СНАГА КРАЈИНЕ</strong>"))

        self.show()


    def progress(self):
        global counter, db_conn, db_user, network_conn
        self.progressBar.setValue(counter)

        # Connect to db
        if counter == 30:
            db_conn = db.connect(database='prelo')
            if not db_conn:
                self.timer.stop()

                self.menu = MenuScreen(db_user, False)
                self.popup = PopupError(None, 'Неуспјешно повезивање са базом података.\nАпликацију можете користити у офлајн режиму рада.', 'Провјерите конекцију')
                self.close()

        if counter == 60:
            
            network_conn.connect()
            if not network_conn.connected:
                self.timer.stop()

                self.menu = MenuScreen(db_user, False)
                self.popup = PopupError(None, 'Неуспјешно повезивање са сервером.\nАпликацију можете користити у офлајн режиму рада.', 'Провјерите конекцију')
                self.close()

        # Close loading screen and open welcome screen
        if counter > 100:
            self.timer.stop()
            self.welcome = WelcomeScreen()
            self.close()

        counter += 1


if __name__ == '__main__':
    network_conn = Network('localhost', 5555)
    
    app = QtWidgets.QApplication(sys.argv)
    window = LoadingScreen()
    app.exec_()
    if db_user is not None:
        db_user.user_quit()
    sys.exit()
