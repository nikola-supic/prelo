# Importing the libraries
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup
from ui.screen_play import Ui_PlayScreen
from datetime import datetime, timedelta
from _thread import start_new_thread
from random import choice

import database as db
from module.popup import PopupWarning

# Global Variables
SONG = 1
ARTIST = 2
LOCAL = 3
RECENT = 4
PLAYLIST = 5
ARTIST_LIST = 6

REPEAT_ALL = 1
REPEAT_ONE = 2

STATUS_PAUSED = 1
STATUS_STARTED = 2

# PLAY SCREEN
class PlayScreen(QMainWindow, Ui_PlayScreen):
    def __init__(self, last_screen):
        super(PlayScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.user = last_screen.user
        self.network = last_screen.network
        self.online = last_screen.online
        self.stacked_pages.setCurrentWidget(self.page_songs)

        self.playmode = SONG
        self.playlist_list = []
        self.song_list = {}
        self.new_list = set()
        self.active_list = {}
        self.previous_song = None
        self.active_song = None
        self.active_idx = None
        self.shuffle = True
        self.repeat = REPEAT_ALL
        self.status = STATUS_PAUSED
 
        if self.online:
            self.setup_songs()
            self.update_playlist()
        else:
            self.setup_local()

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_back.clicked.connect(self.exit)
        self.btn_song.clicked.connect(self.setup_songs)
        self.btn_artist.clicked.connect(self.setup_artist)
        self.btn_local.clicked.connect(self.setup_local)
        self.btn_recent.clicked.connect(self.setup_recent)
        self.list_songs.itemDoubleClicked.connect(self.choose_song)
        self.list_playlist.itemDoubleClicked.connect(self.choose_playlist)

        self.btn_new.clicked.connect(self.new_playlist)
        self.btn_search.clicked.connect(self.search_song)
        self.list_search.itemDoubleClicked.connect(self.add_song)
        self.list_added.itemDoubleClicked.connect(self.delete_song)
        self.btn_create.clicked.connect(self.create_playlist)

        self.btn_download.clicked.connect(lambda: self.download_song(False))
        self.btn_add.clicked.connect(self.add_song)
        self.btn_share.clicked.connect(self.share_song)

        self.btn_shuffle.clicked.connect(self.check_shuffle)
        self.btn_shuffle_off.clicked.connect(self.check_shuffle)
        self.btn_previous.clicked.connect(self.previous)
        self.btn_play.clicked.connect(self.check_status)
        self.btn_pause.clicked.connect(self.check_status)
        self.btn_next.clicked.connect(self.next)
        self.btn_repeat_all.clicked.connect(self.check_repeat)
        self.btn_repeat_one.clicked.connect(self.check_repeat)

        self.click_time = get_time() + 2

        self.show()
        self.widget_current.hide()
        self.check_buttons()

    # # # # # # # # #
    # SETUP FOR SONG
    # # # # # # # # #

    def update_playlist(self):
        self.playlist_list = []
        self.list_playlist.clear()
        result = db.get_user_playlist(self.user.id)
        for idx, item in enumerate(result):
            name = db.get_playlist_name(item[0])

            self.playlist_list.append(item[0])
            item = QtWidgets.QListWidgetItem(name)
            self.list_playlist.addItem(item)


    def setup_songs(self):
        if self.online:
            self.stacked_pages.setCurrentWidget(self.page_songs)
            self.playmode = SONG
            self.song_list = {}
            songs = db.get_user_songs(self.user.id)

            self.list_songs.clear()
            for idx, item in enumerate(songs):
                song = db.Song(item[0])
                artist = db.get_artist_name(song.artist_id)

                self.song_list[idx] = song
                item = QtWidgets.QListWidgetItem(f'{artist} - {song.name}')
                self.list_songs.addItem(item)
        else:
            self.popup = PopupWarning(self, 'Апликацију користите у офлајн режиму.\nОву опцију можете користити само док сте онлајн.', 'Офлајн режим')
            self.close()


    def setup_artist(self):
        if self.online:
            self.stacked_pages.setCurrentWidget(self.page_songs)
            self.playmode = ARTIST
            self.song_list = {}
            artists = db.get_user_artist(self.user.id)

            self.list_songs.clear()
            for idx, item in enumerate(artists):
                artist = db.get_artist_name(item[0])
                artist_count = db.get_artist_count(item[0])

                self.song_list[idx] = item[0]
                item = QtWidgets.QListWidgetItem(f'{artist} // Пјесамe ({artist_count})')
                self.list_songs.addItem(item)
        else:
            self.popup = PopupWarning(self, 'Апликацију користите у офлајн режиму.\nОву опцију можете користити само док сте онлајн.', 'Офлајн режим')
            self.close()


    def setup_local(self):
        self.stacked_pages.setCurrentWidget(self.page_songs)
        self.playmode = LOCAL
        self.song_list = {}

        songs = []
        os.chdir('songs')
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for mp3 in files:
            if mp3.endswith('.mp3'):
                songs.append(mp3)  
        os.chdir('..')

        self.list_songs.clear()
        for idx, item in enumerate(songs):
            self.song_list[idx] = item
            item = QtWidgets.QListWidgetItem(f'{item}')
            self.list_songs.addItem(item)


    def setup_recent(self):
        if self.online:
            self.stacked_pages.setCurrentWidget(self.page_songs)
            self.playmode = RECENT
            self.song_list = {}
            recent = db.get_user_recent(self.user.id)

            self.list_songs.clear()
            for idx, item in enumerate(recent):
                song = db.Song(item[0])
                artist = db.get_artist_name(song.artist_id)

                self.song_list[idx] = song
                item = QtWidgets.QListWidgetItem(f'{artist} - {song.name}')
                self.list_songs.addItem(item)
        else:
            self.popup = PopupWarning(self, 'Апликацију користите у офлајн режиму.\nОву опцију можете користити само док сте онлајн.', 'Офлајн режим')
            self.close()


    def choose_playlist(self):
        if self.online:
            self.stacked_pages.setCurrentWidget(self.page_songs)
            self.playmode = PLAYLIST
            self.song_list = {}
            selected = self.list_playlist.currentRow()
            playlist_id = self.playlist_list[selected] 
            playlist = db.get_playlist_songs(playlist_id)

            self.list_songs.clear()
            for idx, item in enumerate(playlist):
                song = db.Song(item[0])
                artist = db.get_artist_name(song.artist_id)

                self.song_list[idx] = song
                item = QtWidgets.QListWidgetItem(f'{artist} - {song.name}')
                self.list_songs.addItem(item)
        else:
            self.popup = PopupWarning(self, 'Апликацију користите у офлајн режиму.\nОву опцију можете користити само док сте онлајн.', 'Офлајн режим')
            self.close()


    def choose_song(self):
        selected = self.list_songs.currentRow()
        if self.playmode == ARTIST:
            artist_id = self.song_list[selected]

            self.playmode = ARTIST_LIST
            self.song_list = {}
            artist_songs = db.get_artist_songs(artist_id)

            self.list_songs.clear()
            for idx, item in enumerate(artist_songs):
                song = db.Song(item[0])
                artist = db.get_artist_name(artist_id)

                self.song_list[idx] = song
                item = QtWidgets.QListWidgetItem(f'{artist} - {song.name}')
                self.list_songs.addItem(item)
        
        elif self.playmode == LOCAL:
            pass
        
        else:
            self.active_list = []
            for song in self.song_list.values():
                self.active_list.append(song)

            self.setup_song(self.song_list[selected])

    # # # # # # # #
    # NEW PLAYLIST
    # # # # # # # #

    def new_playlist(self):
        if self.online:
            self.stacked_pages.setCurrentWidget(self.page_new)
        else:
            self.popup = PopupWarning(self, 'Апликацију користите у офлајн режиму.\nОву опцију можете користити само док сте онлајн.', 'Офлајн режим')
            self.close()


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
        selected = self.list_search.selectedItems()
        if selected:
            song_id = selected[0].text()[1:]
            song_id = song_id.split(' ')[0]
            
            self.new_list.add(song_id)
            self.refresh_added()


    def delete_song(self):
        selected = self.list_added.selectedItems()
        if selected:
            song_id = selected[0].text()[1:]
            song_id = song_id.split(' ')[0]
        
            self.new_list.remove(song_id)
            self.refresh_added()


    def refresh_added(self):
        self.list_added.clear()
        for song in self.new_list:
            song = db.Song(song)
            artist_name = db.get_artist_name(song.artist_id)

            item = QtWidgets.QListWidgetItem(f'#{song.song_id} // {artist_name} - {song.name}')
            self.list_added.addItem(item)


    def create_playlist(self):
        name = self.input_name.text()
        desc = self.input_desc.text()
        public = self.check_public.isChecked()

        if name and desc and self.new_list:
            playlist_id = db.create_playlist(self.user.id, name, desc, public)
            for song in self.new_list:
                db.add_playlist_song(playlist_id, song)

            db.add_user_playlist(self.user.id, playlist_id)
            self.update_playlist()

            self.list_search.clear()
            self.list_added.clear()
            self.input_search.setText('')
            self.input_name.setText('')
            self.input_desc.setText('')
            self.check_public.setChecked(False)
            self.new_list = set()
        else:
            self.popup = PopupWarning(self, 'Нисте унијели име или опис плејлисте или је ваша листа празна.', 'Неуспјешно креирање')
            self.close()

    # # # # # # # # # # # #
    # ACTIVE SONG BUTTONS
    # # # # # # # # # # # #

    def check_buttons(self):
        if self.shuffle:
            self.btn_shuffle_off.hide()
            self.btn_shuffle.show()
        else:
            self.btn_shuffle.hide()
            self.btn_shuffle_off.show()

        if self.repeat == REPEAT_ALL:
            self.btn_repeat_one.hide()
            self.btn_repeat_all.show()
        else:
            self.btn_repeat_one.show()
            self.btn_repeat_all.hide()

        if self.status == STATUS_PAUSED:
            self.btn_pause.hide()
            self.btn_play.show()
        else:
            self.btn_play.hide()
            self.btn_pause.show()


    def setup_song(self, song):
        if self.playmode == LOCAL:
            pass
        else:
            if not self.widget_current.isVisible():
                self.widget_current.show()
            artist = db.get_artist_name(song.song_id)

            self.label_name.setText(song.name)
            self.label_artist.setText(artist)
            self.label_time.setText(str(timedelta(seconds=0)))
            self.label_length.setText(str(timedelta(seconds=song.length)))

            self.song_status.setValue(0)
            self.song_status.setMaximum(song.length)

            self.active_song = song


    def download_song(self, temp):
        start_new_thread(self.download_thread, (self.active_song, temp, ))


    def download_thread(self, song, temp):
        try:
            old_text = self.label.text()
            self.label.setText('Преузимање у току...')
            file_path, song_size = self.network.download_song(self.user.id, song.song_id, song.path, temp)
            self.label.setText(old_text)

        except Exception as e:
            print(str(e))
            print('Error')


    def add_song(self):
        db.add_user_song(self.user.id, self.active_song.song_id)


    def share_song(self):
        pass


    def check_shuffle(self):
        self.shuffle = False if self.shuffle else True
        self.check_buttons()


    def previous(self):
        if len(self.active_list) == 1:
            return False

        if self.previous_song is None:
            if self.shuffle:
                random = choice(self.active_list)
                self.setup_song(random)
            else:
                index = self.active_list.index(self.active_song)
                if index == 0:
                    index = len(self.active_list)
                self.setup_song(self.active_list[index - 1])

        else:
            self.setup_song(self.previous_song)
            self.previous_song = self.active_song


    def check_status(self):
        self.status = STATUS_STARTED if self.status == STATUS_PAUSED else STATUS_PAUSED
        self.check_buttons()

        if self.status == STATUS_STARTED:
            song = self.active_song
            artist = db.get_artist_name(song.artist_id)

            if os.path.isfile(song.path):
                current_path = os.getcwd()
                full_path = current_path + '\\' + song.path

                url = QtCore.QUrl.fromLocalFile(full_path)
                content = QtMultimedia.QMediaContent(url)
                player = QtMultimedia.QMediaPlayer()
                player.setMedia(content)
                player.setMuted(False)
                player.setVolume(100)
                player.play()

            else:
                self.download_song(True)


    def next(self):
        if len(self.active_list) == 1:
            return False

        self.previous_song = self.active_song

        if self.shuffle:
            random = choice(self.active_list)
            while random == self.active_song:
                random = choice(self.active_list)

            self.setup_song(random)
        else:
            index = self.active_list.index(self.active_song)
            if (index+1) == len(self.active_list):
                index = -1
            self.setup_song(self.active_list[index + 1])


    def check_repeat(self):
        self.repeat = REPEAT_ONE if self.repeat == REPEAT_ALL else REPEAT_ALL
        self.check_buttons()


    def exit(self):
        self.back.show()
        self.close()


def get_time():
    return datetime.now().timestamp()