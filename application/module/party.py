# Importing the libraries
import sys, time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QThread, QObject, pyqtSignal, pyqtSlot
from ui.screen_party import Ui_PartyScreen
from datetime import datetime
from _thread import start_new_thread

import database as db

from module.character import Character

# PARTY SCREEN
class PartyScreen(QMainWindow, Ui_PartyScreen):
    def __init__(self, last_screen):
        super(PartyScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.user = last_screen.user
        self.network = last_screen.network
        self.stacked_pages.setCurrentWidget(self.page_party)

        self.party = None
        self.characters = {}

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_back.clicked.connect(self.exit)
        
        self.btn_chat.clicked.connect(self.switch_to_chat)
        self.btn_queue.clicked.connect(self.switch_to_queue)
        self.btn_hide.clicked.connect(self.switch_to_party)
        self.btn_hide_2.clicked.connect(self.switch_to_party)

        self.btn_head.clicked.connect(self.animation_head)
        self.btn_arms.clicked.connect(self.animation_arms)
        self.btn_add.clicked.connect(self.song_add)
        self.btn_download.clicked.connect(self.song_download)

        self.btn_send.clicked.connect(self.send_message)

        self.click_time = get_time() + 1
        self.anim_time = 750

        # Threading
        self.thread = QThread()
        self.worker = PartyThread(self.user, self.network)
        self.worker.moveToThread(self.thread)
 
        self.worker.party_left.connect(self.on_party_left)
        self.worker.party_get.connect(self.on_party_get)
        self.worker.chat_get.connect(self.on_get_chat)
 
        self.thread.started.connect(self.worker.join_party)
        self.thread.start()

        self.show()

    # # # # # # # # # # # #
    # PARTY THREAD SIGNALS
    # # # # # # # # # # # #

    def on_party_left(self):
        self.thread.quit()

    def on_party_get(self, party):
        if party is None:
            return True

        self.label_listeners.setText(f'Слушаоци: {len(party.users)}')

        self.party = party
        for user_id in party.users:
            if user_id not in self.characters:
                user = party.users[user_id]
                char = Character(self.page_party, user.username, user.pos, user.size, user.body, user.head, user.arms)
                self.characters[user_id] = char

        remove_list = []
        for user_id in self.characters:
            char = self.characters[user_id]
            if user_id not in party.users:
                char.hide()
                remove_list.append(user_id)
            else:
                user = party.users[user_id]

                if user.anim_head:
                    char.start_head_anim()
                else:
                    char.stop_head_anim()

                if user.anim_arms:
                    char.start_arms_anim()
                else:
                    char.stop_arms_anim()

                char.show()

        for user_id in remove_list:
            self.characters.pop(user_id)

    def on_get_chat(self, chat):
        self.chat_history.setPlainText(chat)

    # # # # # # # # # # #
    # SWITCH ANIMATIONS
    # # # # # # # # # # #

    def switch_to_chat(self):
        # Opening animation
        current_widget = self.stacked_pages.currentWidget()
        if current_widget != self.page_party:
            return True

        self.stacked_pages.setCurrentWidget(self.page_chat)

        self.anim = QPropertyAnimation(self.frame_chat, b"geometry")
        self.anim.setDuration(self.anim_time)
        self.anim.setStartValue(QtCore.QRect(0, 420, 470, 0))
        self.anim.setEndValue(QtCore.QRect(0, 0, 470, 420))
        self.anim.setEasingCurve(QtCore.QEasingCurve.OutQuad)
        self.anim.start()

    def switch_to_queue(self):
        current_widget = self.stacked_pages.currentWidget()
        if current_widget != self.page_party:
            return True

        self.stacked_pages.setCurrentWidget(self.page_queue)

        self.anim = QPropertyAnimation(self.frame_queue, b"geometry")
        self.anim.setDuration(self.anim_time)
        self.anim.setStartValue(QtCore.QRect(0, 420, 470, 0))
        self.anim.setEndValue(QtCore.QRect(0, 0, 470, 420))
        self.anim.setEasingCurve(QtCore.QEasingCurve.OutQuad)
        self.anim.start()

    def switch_to_party(self):
        current_widget = self.stacked_pages.currentWidget()
        if current_widget == self.page_chat:
            self.anim = QPropertyAnimation(self.frame_chat, b"geometry")
            self.anim.setDuration(self.anim_time)
            self.anim.setStartValue(QtCore.QRect(0, 0, 470, 420))
            self.anim.setEndValue(QtCore.QRect(0, 420, 470, 0))
            self.anim.setEasingCurve(QtCore.QEasingCurve.OutQuad)
            self.anim.start()

        if current_widget == self.page_queue:
            self.anim = QPropertyAnimation(self.frame_queue, b"geometry")
            self.anim.setDuration(self.anim_time)
            self.anim.setStartValue(QtCore.QRect(0, 0, 470, 420))
            self.anim.setEndValue(QtCore.QRect(0, 420, 470, 0))
            self.anim.setEasingCurve(QtCore.QEasingCurve.OutQuad)
            self.anim.start()

        QtCore.QTimer.singleShot(self.anim_time, lambda: self.stacked_pages.setCurrentWidget(self.page_party))

    # # # # # # # # # #
    # PARTY FUNCTIONS
    # # # # # # # # # #
    def animation_head(self):
        self.network.send(f'toggle_head {self.user.id}')

    def animation_arms(self):
        self.network.send(f'toggle_arms {self.user.id}')

    def song_add(self):
        pass

    def song_download(self):
        pass

    # # # # # # # # #
    # CHAT FUNCTIONS
    # # # # # # # # #
    def send_message(self):
        msg = self.input_msg.text()
        if msg:
            try:
                username = str(self.user.username)
                username.replace(' ', '_')
                chat = self.network.send(f'send_message {self.user.id} {username} {msg}')

                self.input_msg.setText('')
                self.chat_history.setPlainText(chat)
            except Exception as e:
                print('Error while trying to send message.')
                print(str(e))

    # # # # # # # # # #
    # QUEUE FUNCTIONS
    # # # # # # # # # #

    def exit(self):
        self.worker.leave_party()
        self.back.show()
        self.close()

# # # # # # # # # # # #
# COMMUNICATION THREAD
# # # # # # # # # # # #
class PartyThread(QObject):
    party_get = pyqtSignal(object)
    party_left = pyqtSignal()
    chat_get = pyqtSignal(str)

    def __init__(self, user, network):
        super(PartyThread, self).__init__()
        self.user = user
        self.network = network
        self.running = True

    @pyqtSlot()
    def join_party(self):
        party = self.network.send(f'join_party {self.user.id}')

        while self.running:
            try:
                party = self.network.send('get_party')
                self.party_get.emit(party)

            except Exception as e:
                print('Error while trying to get party')
                print(str(e))

            try:
                chat = self.network.send('get_chat')
                self.chat_get.emit(chat)

            except Exception as e:
                print('Error while trying to get chat')
                print(str(e))

            time.sleep(1)

        self.party_left.emit()

    @pyqtSlot()
    def leave_party(self):
        self.running = False
        party = self.network.send(f'leave_party {self.user.id}')

def get_time():
    return datetime.now().timestamp()