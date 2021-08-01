# Importing the libraries
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup
from ui.screen_settings import Ui_SettingsScreen
from datetime import datetime, date

import database as db
from download import download_playlist, download_single
from module.popup import PopupWarning

# SETTINGS SCREEN
class SettingsScreen(QMainWindow, Ui_SettingsScreen):
    def __init__(self, last_screen):
        super(SettingsScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.user = last_screen.user
        self.network = last_screen.network
        self.stacked_pages.setCurrentWidget(self.page_info)

        self.song_list = {}
        self.playlist_list = []
        self.active_song = None
        self.active_playlist = None
        self.playlist_songs_list = []
        self.search_songs = []

        self.update_user()
        self.update_recent()
        self.update_playlist()
        self.update_song()

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_back.clicked.connect(self.exit)
        self.btn_page_info.clicked.connect(lambda: self.stacked_pages.setCurrentWidget(self.page_info))
        self.btn_page_acc.clicked.connect(lambda: self.stacked_pages.setCurrentWidget(self.page_acc))
        self.btn_page_security.clicked.connect(lambda: self.stacked_pages.setCurrentWidget(self.page_security))
        self.btn_page_song.clicked.connect(lambda: self.stacked_pages.setCurrentWidget(self.page_song))
        self.list_playlist.itemDoubleClicked.connect(self.choose_playlist)
        
        self.btn_acc_save.clicked.connect(self.save_acc)
        self.btn_security_save.clicked.connect(self.save_security)

        self.list_song.itemDoubleClicked.connect(self.choose_song)
        self.btn_remove.clicked.connect(self.remove_song)
        self.btn_download.clicked.connect(self.download_song)

        self.btn_playlist_remove.clicked.connect(self.playlist_remove)
        self.btn_playlist_download.clicked.connect(self.playlist_download)
        self.btn_search.clicked.connect(self.search_song)
        self.btn_save.clicked.connect(self.playlist_save)
        self.playlist_songs.itemDoubleClicked.connect(self.remove_playlist_song)
        self.list_search.itemDoubleClicked.connect(self.add_playlist_song)

        self.click_time = get_time() + 1

        self.show()
        self.widget_song.hide()
        self.widget_edit.hide()

    # # # # # # # # #
    # INFO
    # # # # # # # # #

    def update_user(self):
        name = db.get_name(self.user.id)
        username = db.get_username(self.user.id)
        art_id = db.get_user_art(self.user.id)
        art_path = db.get_art_path(art_id)
        self.user_name.setText(name)
        self.user_username.setText(username)
        self.user_art.setStyleSheet(f"border-image: url({art_path});")

        if self.user.admin:
            admin = 'ДА'
        else:
            admin = 'НЕ'

        self.info.setPlainText(f'Рођендан: {self.user.birthday:%d.%m.%Y.}\nВаш мејл: {self.user.email}\nАдмин: {admin}\nДатум регистрације: {self.user.register_date:%d.%m.%Y. %H:%M:%S}')


    def update_recent(self):
        recent = db.get_user_recent(self.user.id)

        self.list_recent.clear()
        for item in recent:
            song = db.Song(item[0])
            artist = db.get_artist_name(song.artist_id)

            item = QtWidgets.QListWidgetItem(f'{artist} - {song.name}')
            self.list_recent.addItem(item)


    def update_playlist(self):
        self.playlist_list = []
        self.list_playlist.clear()
        result = db.get_user_playlist(self.user.id)
        for idx, item in enumerate(result):
            name = db.get_playlist_name(item[0])

            self.playlist_list.append(item[0])
            item = QtWidgets.QListWidgetItem(name)
            self.list_playlist.addItem(item)


    def update_song(self):
        self.song_list = {}
        result = db.get_user_songs(self.user.id)

        self.list_song.clear()
        for idx, item in enumerate(result):
            song = db.Song(item[0])
            artist = db.get_artist_name(song.artist_id)

            self.song_list[idx] = song
            item = QtWidgets.QListWidgetItem(f'{artist} - {song.name}')
            self.list_song.addItem(item)

    # # # # # # # # #
    # ACCOUNT
    # # # # # # # # #

    def save_acc(self):
        first_name = self.input_first.text()
        last_name = self.input_last.text()
        username = self.input_username.text()

        try:
            day = int(self.input_day.text())
            month = int(self.input_month.text())
            year = int(self.input_year.text())
        except ValueError:
            day = False
            month = False
            year = False


        if len(first_name) >= 4:
            self.user.first_name = first_name
            self.user.update_sql('first_name', first_name)
        elif first_name:
            self.popup = PopupWarning(self, 'Ваше име мора имати најмање 4 карактера.', 'Погреашна лозинка.')
            self.close()

        if len(last_name) >= 4:
            self.user.last_name = last_name
            self.user.update_sql('last_name', last_name)
        elif last_name:
            self.popup = PopupWarning(self, 'Ваше презиме мора имати најмање 4 карактера.', 'Погреашна лозинка.')
            self.close()

        if len(username) >= 4:
            self.user.username = username
            self.user.update_sql('username', username)
        elif username:
            self.popup = PopupWarning(self, 'Ваше корисничко име мора имати најмање 4 карактера.', 'Погреашна лозинка.')
            self.close()

        if all([day, month, year]):
            try:
                birthday = date(year, month, day)
                self.user.birthday = birthday
                self.user.update_sql('birthday', birthday)

            except TypeError:
                self.popup = PopupWarning(self, 'Дан, мјесец или годину сте унијели погрешно.', 'Неуспјешна промјена датума рођења.')
                self.close()

        self.update_user()
        self.input_first.setText('')
        self.input_last.setText('')
        self.input_username.setText('')
        self.input_day.setText('')
        self.input_month.setText('')
        self.input_year.setText('')

    # # # # # # # # #
    # SECURITY
    # # # # # # # # #

    def save_security(self):
        password = self.input_pw.text()
        confirm_pw = self.input_pw_2.text()
        email = self.input_email.text()

        if password == confirm_pw:
            changed = db.update_password(self.user.id, password)
            if not changed:
                self.popup = PopupWarning(self, 'Ваша лозинка мора имати између 8 и 32 карактера.', 'Погреашна лозинка.')
                self.close()

        if len(email) >= 8:
            self.user.email = email
            self.user.update_sql('email', email)
        elif email:
            self.popup = PopupWarning(self, 'Ваш мејл мора имати најмање 8 карактера.', 'Погреашан мејл.')
            self.close()

        self.update_user()
        self.input_pw.setText('')
        self.input_pw_2.setText('')
        self.input_email.setText('')

    # # # # # # # # #
    # SONG
    # # # # # # # # #

    def choose_song(self):
        selected = self.list_song.currentRow()
        if not self.widget_song.isVisible():
            self.widget_song.show()

        song = self.song_list[selected]
        artist = db.get_artist_name(song.artist_id)
        art_path = db.get_art_path(song.art)

        self.active_song = song
        self.song_name.setText(song.name)
        self.song_artist.setText(artist)
        self.song_art.setStyleSheet(f"border-image: url({art_path});")

    def remove_song(self):
        db.remove_user_song(self.user.id, self.active_song.song_id)
        self.update_song()
        self.widget_song.hide()

    def download_song(self):
        start_new_thread(download_single, (self.user.id, self.active_song, self.network, ))

    # # # # # # # # #
    # PLAYLIST
    # # # # # # # # #

    def choose_playlist(self):
        self.stacked_pages.setCurrentWidget(self.page_playlist)

        selected = self.list_playlist.currentRow()
        playlist_id = self.playlist_list[selected]
        playlist = db.get_playlist(playlist_id)
        playlist_creator = playlist[1]
        playlist_name = playlist[2]
        playlist_desc = playlist[3]
        playlist_public = playlist[4]

        if playlist_creator == self.user.id:
            self.widget_edit.show()
        else:
            self.widget_edit.hide()

        self.active_playlist = playlist_id
        self.playlist_name.setText(playlist_name)
        self.playlist_desc.setText(playlist_desc)
        self.check_public.setChecked(playlist_public)

        self.update_playlist_song(playlist_id)

    def update_playlist_song(self, playlist_id):
        result = db.get_playlist_songs(playlist_id)
        
        self.playlist_songs_list = []
        self.playlist_songs.clear()
        for item in result:
            song = db.Song(item[0])
            artist_name = db.get_artist_name(song.artist_id)

            self.playlist_songs_list.append(item[0])
            item = QtWidgets.QListWidgetItem(f'{artist_name} - {song.name}')
            self.playlist_songs.addItem(item)

    def playlist_remove(self):
        playlist_id = self.active_playlist
        playlist = db.get_playlist(playlist_id)

        if playlist_creator == self.user.id:
            db.delete_playlist(playlist_id)
        else:
            db.remove_user_playlist(self.user.id, playlist_id)

    def playlist_download(self):
        playlist_id = self.active_playlist
        result = db.get_playlist_songs(playlist_id)

        song_list = []
        for item in result:
            song_list.append(db.Song(item[0]))

        download_playlist(self.user.id, song_list, self.network)

    def search_song(self):
        song = self.input_search.text()
        result = db.search_song(song)

        self.search_songs = []
        self.input_search.setText('')
        for item in result:
            song_id = item[0]
            artist_name = db.get_artist_name(item[1])
            name = item[2] 

            self.search_songs.append(song_id)
            item = QtWidgets.QListWidgetItem(f'{artist_name} - {name}')
            self.list_search.addItem(item)

    def add_playlist_song(self):
        index = self.list_search.currentRow()
        song_id = self.search_songs[index]

        db.add_playlist_song(self.active_playlist, song_id)
        self.list_search.clear()
        self.update_playlist_song(self.active_playlist)

    def remove_playlist_song(self):
        index = self.list_search.currentRow()
        song_id = self.playlist_songs_list[index]

        db.remove_playlist_song(self.active_playlist, song_id)
        self.update_playlist_song(self.active_playlist)

    def playlist_save(self):
        playlist_id = self.active_playlist
        public = self.check_public.isChecked()

        db.update_public(playlist_id, public)

    def exit(self):
        self.back.show()
        self.close()


def get_time():
    return datetime.now().timestamp()