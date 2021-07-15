# Importing the libraries
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup
from ui.screen_chat import Ui_ChatScreen
from datetime import datetime

import database as db
from module.popup import PopupWarning

# CHAT SCREEN
class ChatScreen(QMainWindow, Ui_ChatScreen):
    def __init__(self, last_screen):
        super(ChatScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.user = last_screen.user
        self.network = last_screen.network
        self.friend_id = None
        self.stacked_pages.setCurrentWidget(self.page_global)
        self.update_friend()
        self.refresh_global()

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_back.clicked.connect(self.exit)
        self.btn_global.clicked.connect(lambda: self.stacked_pages.setCurrentWidget(self.page_global))
        self.list_friends.itemDoubleClicked.connect(self.choose_friend)

        self.btn_send.clicked.connect(self.send_msg_global)
        self.btn_refresh.clicked.connect(self.refresh_global)
        self.btn_send_2.clicked.connect(self.send_msg_friend)
        self.click_time = get_time() + 1

        self.show()


    def choose_friend(self):
        selected = self.list_friends.selectedItems()
        if selected:
            friend_id = selected[0].text()[1:]
            friend_id = friend_id.split('-')[0]

            self.setup_friend(friend_id)


    def setup_friend(self, friend_id):
        self.friend_id = friend_id
        self.stacked_pages.setCurrentWidget(self.page_friend)

        name = db.get_name(friend_id)
        username = db.get_username(friend_id)
        self.label_name.setText(name)
        self.label_user.setText(username)


    def send_msg_global(self):
        msg = self.input_msg.text().replace(' ', '_')
        if msg:
            try:
                username = str(self.user.username)
                username.replace(' ', '_')
                global_chat = self.network.send(f'global {self.user.id} {username} {msg}')
                
                self.chat_global.setPlainText(global_chat)
                self.input_msg.setText('')
            except Exception:
                print('Error')


    def refresh_global(self):
        try:
            global_chat = self.network.send(f'get_global')
            self.chat_global.setPlainText(global_chat)
        except Exception:
            print('Error')


    def send_msg_friend(self):
        pass


    def update_friend(self):
        self.list_friends.clear()
        requests = db.get_friends(self.user.id)
        for req in requests:
            if self.user.id == req[0]:
                friend_id = req[1]
            else:
                friend_id = req[0]

            username = db.get_username(friend_id)
            item = QtWidgets.QListWidgetItem(f'#{friend_id}-@{username}')
            self.list_friends.addItem(item)


    def exit(self):
        self.back.show()
        self.close()


def get_time():
    return datetime.now().timestamp()