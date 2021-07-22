# Importing the libraries
import sys, time, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QThread, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from ui.screen_party import Ui_PartyScreen
from datetime import datetime, timedelta
from _thread import start_new_thread

import database as db

from module.character import Character
from module.effect import Effect
from download import download_single

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
        self.active_song = None

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

        self.slider_volume.sliderMoved.connect(self.change_volume)

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
        self.slider_volume.setValue(75)
        self.label_volume.setText(str(75))

        # Create media player
        self.player = QMediaPlayer()
        self.player.setMuted(False)
        self.player.setVolume(75)
        self.player.positionChanged.connect(self.on_position_change)
        self.player.mediaStatusChanged.connect(self.on_status_change)

    # # # # # # # # # # # #
    # PARTY THREAD SIGNALS
    # # # # # # # # # # # #

    def on_party_left(self):
        self.thread.quit()

    def on_party_get(self, party):
        if party is None:
            return False

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

        # Check song
        self.check_song()

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
            return False

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
            return False

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

        user = self.party.users[self.user.id]

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

    # # # # # # # # # # # # #
    # ACTIVE SONG FUNCTIONS
    # # # # # # # # # # # # #
    def check_song(self):
        if self.active_song is not None:
            return False

        if not self.party.queue and self.party.active_song['song_id'] == None:
            self.toggle_song(False)
            return False

        self.toggle_song(True)
        if self.party.active_song['song_id'] == None:
            user_id = next(iter(self.party.queue))
            user = self.party.users[user_id]
            song_id = user.song_id
        else:
            user_id = self.party.active_song['queue_id']
            user = self.party.users[user_id]
            song_id = self.party.active_song['song_id']

        self.setup_song(user_id, user, song_id)

    def toggle_song(self, show):
        if not show:
            self.label_current.hide()
            self.label_name.hide()
            self.label_artist.hide()
            self.label_time.hide()
            self.label_length.hide()
            self.label_art.hide()
            self.song_status.hide()
        else:
            self.label_current.show()
            self.label_name.show()
            self.label_artist.show()
            self.label_time.show()
            self.label_length.show()
            self.label_art.show()
            self.song_status.show()

    def setup_song(self, queue_id, user, song_id):
        self.label_current.setText(f'Музику пушта: {user.username}')

        song = db.Song(song_id)
        artist = db.get_artist_name(song.song_id)
        art_path = db.get_art_path(song.art)

        self.label_name.setText(song.name)
        self.label_artist.setText(artist)
        self.label_time.setText(str(timedelta(seconds=0)))
        self.label_length.setText(str(timedelta(seconds=song.length)))
        self.label_art.setStyleSheet(f"border-image: url({art_path});")

        self.song_status.setValue(0)
        self.song_status.setMaximum(song.length)

        self.active_song = song
        db.add_user_recent(self.user.id, song.song_id)
        self.play_song(song, queue_id)

    def play_song(self, song, queue_id):
        if os.path.isfile(song.path):
            full_path = os.path.join(os.getcwd(), song.path)
        else:
            song_path = 'temp\\' + song.path[6:]
            full_path = os.path.join(os.getcwd(), song_path)

        url = QtCore.QUrl.fromLocalFile(full_path)
        content = QMediaContent(url)
        self.player.setMedia(content)

        if self.party.active_song['user_id'] == None:
            song = self.network.send(f'play_song {self.user.id} {queue_id} {song.song_id} {0}')
        else:
            self.player.setPosition(self.party.active_song['time'])

        self.player.play()

    def on_position_change(self):
        ms = self.player.position()
        seconds = int(ms / 1000)

        self.label_time.setText(str(timedelta(seconds=seconds)))
        self.song_status.setValue(seconds)

        if self.party.active_song['user_id'] == self.user.id:
            song = self.network.send(f'update_song_time {self.user.id} {ms}')
        elif self.party.active_song['user_id'] == None:
            song = self.network.send(f'update_song_time {self.user.id} {ms}')

    def on_status_change(self):
        status = self.player.mediaStatus()
        if status == QMediaPlayer.EndOfMedia:
            self.toggle_song(False)

            if self.party.active_song['user_id'] == self.user.id:
                song = self.network.send(f'finish_song {self.user.id}')

            self.effects = []
            self.likes = {}
            self.dislikes = {}
            self.reacted = False
            self.active_song = None
            self.player.stop()

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
        if self.active_song == None:
            return False

        db.add_user_song(self.user.id, self.active_song.song_id)

    def song_download(self):
        if self.active_song == None:
            return False

        start_new_thread(download_single, (self.user.id, self.active_song, self.network, ))

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

    def change_volume(self):
        volume = self.slider_volume.value()
        self.player.setVolume(volume)
        self.label_volume.setText(str(volume))

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
        self.close()

    def closeEvent(self, event):
        del self.player
        self.worker.leave_party()
        self.back.show()
        QtCore.QTimer.singleShot(1500, lambda: event.accept())

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

            time.sleep(1)

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