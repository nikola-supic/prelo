# Importing the libraries
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup
from ui.screen_friend import Ui_FriendScreen
from datetime import datetime

import database as db
from module.popup import PopupWarning

# FRIEND SCREEN
class FriendScreen(QMainWindow, Ui_FriendScreen):
    def __init__(self, last_screen):
        super(FriendScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.user = last_screen.user
        self.friend_id = None
        self.stacked_pages.setCurrentWidget(self.page_add)
        self.update_friend()

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_back.clicked.connect(self.exit)
        self.btn_page_add.clicked.connect(lambda: self.stacked_pages.setCurrentWidget(self.page_add))
        self.btn_page_request.clicked.connect(self.request)
        self.list_friends.itemDoubleClicked.connect(self.choose_friend)

        self.btn_search.clicked.connect(self.search_user)
        self.btn_add.clicked.connect(self.send_request)
        self.req_delete.clicked.connect(self.delete_request)
        self.req_accept.clicked.connect(self.accept_request)
        self.req_refuse.clicked.connect(self.refuse_request)

        self.btn_delete.clicked.connect(self.delete_friend)
        self.btn_send.clicked.connect(self.message_friend)

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


    def request(self):
        self.stacked_pages.setCurrentWidget(self.page_request)
        self.update_request()


    def search_user(self):
        name = self.input_name.text()
        if name:
            self.input_name.setText('')
            self.list_search.clear()

            result = db.search_user(name)
            for item in result:
                user_id = item[0]
                name = f'{item[1]} {item[2]}'
                username = item[3] 

                item = QtWidgets.QListWidgetItem(f'#{user_id} // {name} // @{username}')
                self.list_search.addItem(item)


    def send_request(self):
        selected = self.list_search.selectedItems()
        if selected:
            friend_id = selected[0].text()[1:]
            friend_id = friend_id.split()[0]

            if int(self.user.id) != int(friend_id):
                db.add_friend(self.user.id, friend_id)
            else:
                self.popup = PopupWarning(self, 'Не можете додати себе за пријатеља.\nНе покушавајте опет.', 'Стварно мислите додати себе заа пријатеља?')
                self.close()

            self.list_search.clear()


    def delete_request(self):
        selected = self.list_sent.selectedItems()
        if selected:
            request_id = selected[0].text()[1:]
            request_id = request_id.split()[0]

            db.delete_request(request_id)
            self.update_request()


    def accept_request(self):
        selected = self.list_received.selectedItems()
        if selected:
            request_id = selected[0].text()[1:]
            request_id = request_id.split()[0]

            db.accept_request(request_id)
            self.update_request()


    def refuse_request(self):
        selected = self.list_received.selectedItems()
        if selected:
            request_id = selected[0].text()[1:]
            request_id = request_id.split()[0]

            db.delete_request(request_id)
            self.update_request()


    def delete_friend(self):
        db.delete_friend(self.user.id, self.friend_id)
        self.stacked_pages.setCurrentWidget(self.page_add)
        self.update_friend()


    def message_friend(self):
        msg = self.input_msg.toPlainText()
        if msg:
            db.send_message(self.user.id, self.friend_id, msg)
            self.input_msg.setPlainText('')


    def update_request(self):
        self.list_sent.clear()
        requests = db.get_sent_requests(self.user.id)
        for req in requests:
            request_id = req[0]
            username = db.get_username(req[1])
            item = QtWidgets.QListWidgetItem(f'#{request_id} // @{username}')
            self.list_sent.addItem(item)

        self.list_received.clear()
        requests = db.get_requests(self.user.id)
        for req in requests:
            request_id = req[0]
            username = db.get_username(req[1])
            item = QtWidgets.QListWidgetItem(f'#{request_id} // @{username}')
            self.list_received.addItem(item)


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