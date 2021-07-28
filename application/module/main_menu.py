# Importing the libraries
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup
from ui.screen_menu import Ui_MenuScreen

from datetime import datetime

# Import the modules
from module.play import PlayScreen
from module.search import SearchScreen
from module.friend import FriendScreen
from module.chat import ChatScreen
from module.settings import SettingsScreen
from module.about import AboutScreen
from module.popup import PopupWarning
from module.party import PartyScreen
from module.admin import AdminScreen


# MAIN SCREEN
class MenuScreen(QMainWindow, Ui_MenuScreen):
    def __init__(self, user=None, network=None, online=False):
        super(MenuScreen, self).__init__()
        self.setupUi(self)
        self.user = user
        self.network = network
        self.online = online

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_play.clicked.connect(self.play)
        self.btn_search.clicked.connect(self.search)
        self.btn_friends.clicked.connect(self.friends)
        self.btn_chat.clicked.connect(self.chat)
        self.btn_settings.clicked.connect(self.settings)
        self.btn_about.clicked.connect(self.about)
        self.btn_admin.clicked.connect(self.admin)
        self.btn_shutdown.clicked.connect(self.shutdown)
        self.btn_party.clicked.connect(self.party)
        self.click_time = get_time()

        self.show()
        if not self.user.admin:
            self.btn_admin.hide()


    def play(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1

        self.play = PlayScreen(self)
        self.close()


    def search(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1

        if self.online:
            self.search = SearchScreen(self)
            self.close()
        else:
            self.popup = PopupWarning(self, 'Апликацију користите у офлајн режиму.\nОву опцију можете користити само док сте онлајн.', 'Офлајн режим')
            self.close()


    def friends(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1

        if self.online:
            self.friend = FriendScreen(self)
            self.close()
        else:
            self.popup = PopupWarning(self, 'Апликацију користите у офлајн режиму.\nОву опцију можете користити само док сте онлајн.', 'Офлајн режим')
            self.close()


    def chat(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1

        if self.online:
            self.chat = ChatScreen(self)
            self.close()
        else:
            self.popup = PopupWarning(self, 'Апликацију користите у офлајн режиму.\nОву опцију можете користити само док сте онлајн.', 'Офлајн режим')
            self.close()


    def settings(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1

        if self.online:
            self.settings = SettingsScreen(self)
            self.close()
        else:
            self.popup = PopupWarning(self, 'Апликацију користите у офлајн режиму.\nОву опцију можете користити само док сте онлајн.', 'Офлајн режим')
            self.close()


    def about(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1

        if self.online:
            self.about = AboutScreen(self)
            self.close()
        else:
            self.popup = PopupWarning(self, 'Апликацију користите у офлајн режиму.\nОву опцију можете користити само док сте онлајн.', 'Офлајн режим')
            self.close()


    def admin(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1

        if self.online:
            self.admin = AdminScreen(self)
            self.close()
        else:
            self.popup = PopupWarning(self, 'Апликацију користите у офлајн режиму.\nОву опцију можете користити само док сте онлајн.', 'Офлајн режим')
            self.close()


    def party(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1

        if self.online:
            self.about = PartyScreen(self)
            self.close()
        else:
            self.popup = PopupWarning(self, 'Апликацију користите у офлајн режиму.\nОву опцију можете користити само док сте онлајн.', 'Офлајн режим')
            self.close()


    def shutdown(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1

        if self.online:
            self.user.user_quit()
        sys.exit()


def get_time():
    return datetime.now().timestamp()