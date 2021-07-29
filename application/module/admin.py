# Importing the libraries
import sys, time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from ui.screen_admin import Ui_AdminScreen
from _thread import start_new_thread
from datetime import datetime, timedelta

import database as db

# ADMIN SCREEN
class AdminScreen(QMainWindow, Ui_AdminScreen):
    def __init__(self, last_screen):
        super(AdminScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.user = last_screen.user
        self.network = last_screen.network
        self.stacked_pages.setCurrentWidget(self.page_user)

        self.online_thread = None
        self.chosen_user = None
        self.chosen_song = None

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_back.clicked.connect(self.exit)
        self.btn_page_user.clicked.connect(self.switch_to_user)
        self.btn_page_online.clicked.connect(self.switch_to_online)
        self.btn_page_song.clicked.connect(self.switch_to_song)
        self.btn_page_artist.clicked.connect(self.switch_to_artist)
        self.btn_page_playlist.clicked.connect(self.switch_to_playlist)
        self.btn_page_art.clicked.connect(self.switch_to_art)

        # User
        self.btn_search_user.clicked.connect(self.search_user)
        self.btn_ban.clicked.connect(self.ban_user)
        self.btn_delete.clicked.connect(self.delete_user)
        self.btn_admin.clicked.connect(self.admin_user)

        # Song
        self.btn_search_song.clicked.connect(self.search_song)
        self.btn_song_delete.clicked.connect(self.delete_song)
        self.btn_song_save.clicked.connect(self.save_song)

        # Artist
        self.btn_search_artist.clicked.connect(self.search_artist)
        self.btn_artist_delete.clicked.connect(self.delete_artist)
        self.btn_artist_save.clicked.connect(self.save_artist)

        # Playlist
        self.btn_search_playlist.clicked.connect(self.search_playlist)
        self.btn_playlist_delete.clicked.connect(self.delete_playlist)
        self.btn_playlist_save.clicked.connect(self.save_playlist)

        # Search
        self.btn_search_art.clicked.connect(self.search_art)
        self.btn_art_delete.clicked.connect(self.delete_art)
        self.btn_art_save.clicked.connect(self.save_art)

        self.click_time = get_time() + 1

        self.show()
        self.widget_user.hide()

    # # # # # # # # # #
    # SWITCH FUNCTIONS
    # # # # # # # # # #

    def switch_to_user(self):
        self.online_thread = None
        self.stacked_pages.setCurrentWidget(self.page_user)
        self.widget_user.hide()

    def switch_to_online(self):
        self.stacked_pages.setCurrentWidget(self.page_online)
        if self.online_thread is None:
            self.online_thread = start_new_thread(self.refresh_online, ())

    def switch_to_song(self):
        self.online_thread = None
        self.stacked_pages.setCurrentWidget(self.page_song)
        self.widget_song.hide()

    def switch_to_artist(self):
        self.online_thread = None
        self.stacked_pages.setCurrentWidget(self.page_artist)
        self.widget_artist.hide()

    def switch_to_playlist(self):
        self.online_thread = None
        self.stacked_pages.setCurrentWidget(self.page_playlist)
        self.widget_playlist.hide()

    def switch_to_art(self):
        self.online_thread = None
        self.stacked_pages.setCurrentWidget(self.page_art)
        self.widget_art.hide()

    # # # # # # # # #
    # USER FUNCTIONS
    # # # # # # # # #
    def search_user(self):
        username = self.input_user.text()
        if username:
            user_id = db.search_user(username)
            if not user_id:
                return False
             
            self.input_user.setText('')
            user_id = user_id[0][0]
            user = db.get_user(user_id)
            user = db.User(user)
            art_path = db.get_art_path(user.art)

            if user.admin:
                admin = 'ДА'
            else:
                admin = 'НЕ'

            if user.ban:
                ban = 'ДА'
            else:
                ban = 'НЕ'

            self.user_name.setText(f'{user.first_name} {user.last_name}')
            self.user_username.setText(user.username)
            self.user_art.setStyleSheet(f"border-image: url({art_path});")
            self.info_user.setPlainText(f'Бан: {ban}\nРођендан: {self.user.birthday:%d.%m.%Y.}\nМејл: {self.user.email}\nАдмин: {admin}\nДатум регистрације: {self.user.register_date:%d.%m.%Y. %H:%M:%S}')

            result = db.get_user_songs(user.id)
            self.list_song.clear()
            for idx, item in enumerate(result):
                song = db.Song(item[0])
                artist = db.get_artist_name(song.artist_id)

                item = QtWidgets.QListWidgetItem(f'{song.name} - {artist}')
                self.list_song.addItem(item)

            if not self.widget_user.isVisible():
                self.widget_user.show()

            self.chosen_user = user

    def ban_user(self):
        db.toggle_user_ban(self.chosen_user.id, self.chosen_user.ban)
        self.widget_user.hide()

    def delete_user(self):
        db.delete_user(self.chosen_user.id)
        self.widget_user.hide()

    def admin_user(self):
        db.toggle_user_admin(self.chosen_user.id, self.chosen_user.admin)
        self.widget_user.hide()

    # # # # # # # # # #
    # ONLINE FUNCTIONS
    # # # # # # # # # #
    def refresh_online(self):
        while self.online_thread is not None:
            result = db.get_online()
            self.list_online.clear()

            for idx, user in enumerate(result):
                item = QtWidgets.QListWidgetItem(f'#{idx+1} // @{user[1]} (ID: {user[0]})')
                self.list_online.addItem(item)
            time.sleep(1)

    # # # # # # # # #
    # SONG FUNCTIONS
    # # # # # # # # #
    def search_song(self):
        song_name = self.input_song.text()
        if song_name:
            song_id = db.search_song(song_name)
            if not song_id:
                return False

            self.input_song.setText('')
            song_id = song_id[0][0]
            song = db.Song(song_id)
            artist = db.get_artist_name(song.artist_id)
            art_path = db.get_art_path(song.art)

            self.song_name.setText(song.name)
            self.song_artist.setText(artist)
            self.song_art.setStyleSheet(f"border-image: url({art_path});")
            self.info_song.setPlainText(f'Дужина: {timedelta(seconds=song.length)}\nБитрате: {song.bitrate}\nДодао: {song.added_by}\nДатум додавања: {song.date_added:%d.%m.%Y.}')

            if not self.widget_song.isVisible():
                self.widget_song.show()

            self.chosen_song = song

    def delete_song(self):
        db.delete_song(self.chosen_song.song_id)
        self.widget_song.hide()

    def save_song(self):
        song_name = self.input_song_name.text()
        self.input_song_name.setText('')
        if song_name:
            db.update_song_name(self.chosen_song.song_id, song_name)

        song_artist = self.input_song_artist.text()
        self.input_song_artist.setText('')
        if song_artist:
            db.update_song_artist(self.chosen_song.song_id, song_artist)

        song_art = self.input_song_art.text()
        self.input_song_art.setText('')
        if song_art:
            db.update_song_art(self.chosen_song.song_id, song_art)

        self.widget_song.hide()

    # # # # # # # # # #
    # ARTIST FUNCTIONS
    # # # # # # # # # #
    def search_artist(self):
        pass

    def delete_artist(self):
        pass

    def save_artist(self):
        pass

    # # # # # # # # # # #
    # PLAYLIST FUNCTIONS
    # # # # # # # # # # #
    def search_playlist(self):
        pass

    def delete_playlist(self):
        pass

    def save_playlist(self):
        pass

    # # # # # # # # #
    # ART FUNCTIONS
    # # # # # # # # #
    def search_art(self):
        pass

    def delete_art(self):
        pass

    def save_art(self):
        pass

    # # # # # # # # #
    # EXIT
    # # # # # # # # #
    def exit(self):
        self.close()

    def closeEvent(self, event):
        self.online_thread = None
        self.back.show()
        event.accept()


def get_time():
    return datetime.now().timestamp()