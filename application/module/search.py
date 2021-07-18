# Importing the libraries
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup
from ui.screen_search import Ui_SearchScreen
from datetime import datetime
from _thread import start_new_thread

import database as db
from download import download_playlist, download_single

# Global variables
MODE_SONG = 1
MODE_ARTIST = 2
MODE_PLAYLIST = 3 

# SEARCH SCREEN
class SearchScreen(QMainWindow, Ui_SearchScreen):
    def __init__(self, last_screen):
        super(SearchScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.user = last_screen.user
        self.network = last_screen.network
        self.mode = MODE_SONG

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_back.clicked.connect(self.exit)
        self.btn_search.clicked.connect(self.search)
        self.btn_mode.clicked.connect(self.change_mode)
        self.btn_add.clicked.connect(lambda: self.add_button(False))
        self.btn_download.clicked.connect(lambda: self.add_button(True))
        self.list_search.itemDoubleClicked.connect(self.choose_artist)
        self.click_time = get_time() + 2

        self.show()
        self.downloading.hide()
        self.check_mode()


    def search(self):
        search_text = self.input_search.text()
        if search_text:
            self.input_search.setText('')
            self.list_search.clear()

            if self.mode == MODE_SONG:
                result = db.search_song(search_text)

                for item in result:
                    song_id = item[0]
                    artist_name = db.get_artist_name(item[1])
                    name = item[2] 

                    item = QtWidgets.QListWidgetItem(f'#{song_id} // {artist_name} - {name}')
                    self.list_search.addItem(item)

            elif self.mode == MODE_ARTIST:
                result = db.search_artist(search_text)

                for item in result:
                    artist_id = item[0]
                    artist_name = item[1]

                    item = QtWidgets.QListWidgetItem(f'#{artist_id} // {artist_name}')
                    self.list_search.addItem(item)

            elif self.mode == MODE_PLAYLIST:
                result = db.search_playlist(search_text)

                for item in result:
                    playlist_id = item[0]
                    playlist_name = item[1]

                    item = QtWidgets.QListWidgetItem(f'#{playlist_id} // {playlist_name}')
                    self.list_search.addItem(item)


    def check_mode(self):
        if self.mode == MODE_SONG:
            self.btn_mode.setText('Тражи пјесме')
            self.input_search.setPlaceholderText('Име пјесме')

        elif self.mode == MODE_ARTIST:
            self.btn_mode.setText('Тражи аутора')
            self.input_search.setPlaceholderText('Име аутора')

        elif self.mode == MODE_PLAYLIST:
            self.btn_mode.setText('Тражи алубма')
            self.input_search.setPlaceholderText('Име албума')


    def change_mode(self):
        if self.mode == MODE_SONG:
            self.mode = MODE_ARTIST

        elif self.mode == MODE_ARTIST:
            self.mode = MODE_PLAYLIST

        elif self.mode == MODE_PLAYLIST:
            self.mode = MODE_SONG

        self.check_mode()


    def choose_artist(self):
        if self.mode == MODE_ARTIST:
            selected = self.list_search.selectedItems()
            if selected:
                artist_id = selected[0].text()[1:]
                artist_id = artist_id.split(' ')[0]
                artist_songs = db.get_artist_songs(artist_id)

                self.list_search.clear()
                for item in artist_songs:
                    song_id = item[0]
                    artist = db.get_artist_name(artist_id)
                    song_name = item[1]

                    item = QtWidgets.QListWidgetItem(f'#{song_id} // {artist} - {song_name}')
                    self.list_search.addItem(item)

                self.mode = MODE_SONG
                self.check_mode()


    def add_button(self, download):
        selected = self.list_search.selectedItems()
        if selected:
            if self.mode == MODE_SONG:
                song_id = selected[0].text()[1:]
                song_id = song_id.split(' ')[0]

                db.add_user_song(self.user.id, song_id)
                if download:
                    start_new_thread(download_single, (self.user.id, db.Song(song_id), self.network, ))

            elif self.mode == MODE_PLAYLIST:
                playlist_id = selected[0].text()[1:]
                playlist_id = playlist_id.split(' ')[0]

                db.add_user_playlist(self.user.id, playlist_id)
                if download:
                    result = db.get_playlist_songs(playlist_id)

                    song_list = []
                    for item in result:
                        song_list.append(db.Song(item[0]))
                    
                    download_playlist(self.user.id, song_list, self.network)

    def exit(self):
        self.back.show()
        self.close()



def get_time():
    return datetime.now().timestamp()