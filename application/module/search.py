# Importing the libraries
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup
from ui.screen_search import Ui_SearchScreen
from datetime import datetime

import database as db
from module.popup import PopupWarning

# SEARCH SCREEN
class SearchScreen(QMainWindow, Ui_SearchScreen):
    def __init__(self, last_screen):
        super(SearchScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.user = last_screen.user
        self.network = last_screen.network

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_back.clicked.connect(self.exit)
        self.btn_search.clicked.connect(self.search_song)
        self.btn_add.clicked.connect(self.add_song)
        self.btn_download.clicked.connect(self.download_song)
        self.click_time = get_time() + 2

        self.show()


    def search_song(self):
        song = self.input_search.text()
        if song:
            self.input_search.setText('')
            self.list_search.clear()

            result = db.search_song(song)
            for item in result:
                song_id = item[0]
                artist_name = db.get_artist_name(item[1])
                name = item[2] 

                item = QtWidgets.QListWidgetItem(f'#{song_id} // {artist_name} - {name}')
                self.list_search.addItem(item)


    def add_song(self):
        selected = self.list_friends.selectedItems()
        if selected:
            song_id = selected[0].text()[1:]
            song_id = song_id.split('-')[0]

            db.add_user_song(self.user.id, song_id)


    def download_song(self):
        pass


    def exit(self):
        self.back.show()
        self.close()


def get_time():
    return datetime.now().timestamp()