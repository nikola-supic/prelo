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
from module.effect import Effect

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
        self.search_songs = []
        self.effects = []
        self.likes = {}
        self.dislikes = {}
        self.reacted = False

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
        self.btn_like.clicked.connect(self.song_like)
        self.btn_dislike.clicked.connect(self.song_dislike)

        self.btn_send.clicked.connect(self.send_message)

        self.btn_search.clicked.connect(self.search_song)
        self.btn_join.clicked.connect(self.join_queue)

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
        self.widget_head.hide()
        self.widget_arms.hide()

    # # # # # # # # # # # #
    # PARTY THREAD SIGNALS
    # # # # # # # # # # # #

    def on_party_left(self):
        self.thread.quit()

    def on_party_get(self, party):
        if party is None:
            return True

        # Basic info
        self.label_listeners.setText(f'Слушаоци: {len(party.users)}')
        self.label_like.setText(str(len(party.likes)))
        self.label_dislike.setText(str(len(party.dislikes)))

        # Getting characters
        self.party = party
        for user_id in party.users:
            if user_id not in self.characters:
                user = party.users[user_id]
                char = Character(self.page_party, user.username, user.pos, user.size, user.body, user.head, user.arms)
                self.characters[user_id] = char

        # Drawing characters
        remove_list = []
        for user_id in self.characters:
            char = self.characters[user_id]
            if user_id not in party.users:
                char.hide()
                remove_list.append(user_id)
            else:
                user = party.users[user_id]

                if user.anim_head:
                    char.start_head_anim(int(user.anim_head_time))
                else:
                    char.stop_head_anim()

                if user.anim_arms:
                    char.start_arms_anim(int(user.anim_arms_time))
                else:
                    char.stop_arms_anim()

                char.show()

        # Removing characters
        for user_id in remove_list:
            self.characters.pop(user_id)

        # Updating queue
        self.update_queue()

        # Update effects
        self.update_effects()

    def on_get_chat(self, chat):
        if not self.chat_history.isVisible():
            return False

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

    def check_sliders(self):
        if self.party is None:
            return False

        user = self.party.users[str(self.user.id)]

        if user.anim_head:
            self.widget_head.hide()
        else:
            self.slider_head.setValue(int(user.anim_head_time))
            self.widget_head.show()

        if user.anim_arms:
            self.widget_arms.hide()
        else:
            self.slider_arms.setValue(int(user.anim_arms_time))
            self.widget_arms.show()

    # # # # # # # # # #
    # PARTY FUNCTIONS
    # # # # # # # # # #
    def animation_head(self):
        value = self.slider_head.value()
        self.party = self.network.send(f'toggle_head {self.user.id} {value}')
        self.check_sliders()  

    def animation_arms(self):
        value = self.slider_arms.value()
        self.party = self.network.send(f'toggle_arms {self.user.id} {value}')
        self.check_sliders()  

    def song_add(self):
        pass

    def song_download(self):
        pass

    def song_like(self):
        if self.reacted:
            like = Effect(self.page_party, self.user.id, 'images\\party\\effect_like.png')
            self.effects.append(like)
            return False

        if (self.user.id in self.party.likes) or (self.user.id in self.party.dislikes):
            return False

        likes = self.network.send(f'send_like {self.user.id}')
        self.reacted = True

    def song_dislike(self):
        if self.reacted:
            dislike = Effect(self.page_party, self.user.id, 'images\\party\\effect_dislike.png')
            self.effects.append(dislike)
            return False

        if (self.user.id in self.party.likes) or (self.user.id in self.party.dislikes):
            return False

        dislikes = self.network.send(f'send_dislike {self.user.id}')
        self.reacted = True

    def update_effects(self):
        for user in self.party.likes:
            if user not in self.likes:
                like = Effect(self.page_party, user, 'images\\party\\effect_like.png')
                self.likes[user] = like

        for user in self.party.dislikes:
            if user not in self.dislikes:
                dislike = Effect(self.page_party, user, 'images\\party\\effect_dislike.png')
                self.dislikes[user] = dislike

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
    def search_song(self):
        song_name = self.input_search.text()
        if song_name:
            result = db.search_song(song_name)

            self.input_search.setText('')
            self.list_search.clear()
            self.search_songs = []
            for item in result:
                song_id = item[0]
                artist_name = db.get_artist_name(item[1])
                name = item[2] 

                self.search_songs.append(song_id)
                item = QtWidgets.QListWidgetItem(f'{artist_name} - {name}')
                self.list_search.addItem(item)

    def join_queue(self):
        selected = self.list_search.currentRow()
        if selected != -1:
            song_id = self.search_songs[selected] 
            queue = self.network.send(f'join_queue {self.user.id} {song_id}')

    def update_queue(self):
        if not self.list_queue.isVisible():
            return False

        self.list_queue.clear()
        for idx, user in enumerate(self.party.queue.values()):
            item = QtWidgets.QListWidgetItem(f'#{idx} // {user.username}')
            self.list_queue.addItem(item)


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