# Importing the libraries
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from ui.screen_play import Ui_PlayScreen
from datetime import datetime, timedelta
from _thread import start_new_thread
from random import choice

import database as db
from download import download_playlist, download_single
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
        self.active_song = None
        self.shuffle = True
        self.repeat = REPEAT_ALL
        self.friend_list = []
 
        if self.online:
            self.setup_songs()
            self.update_playlist()
            self.update_friend_list()
        else:
            self.setup_local()

        # Create media player
        self.player = QMediaPlayer()
        self.player.setMuted(False)
        self.player.setVolume(100)

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

        self.btn_download.clicked.connect(lambda: self.download_song(self.active_song))
        self.btn_add.clicked.connect(self.add_song)
        self.btn_share.clicked.connect(self.share_song)
        self.list_friends.itemDoubleClicked.connect(self.send_song)

        self.btn_shuffle.clicked.connect(self.check_shuffle)
        self.btn_shuffle_off.clicked.connect(self.check_shuffle)
        self.btn_previous.clicked.connect(lambda: self.player_playlist.previous())
        self.btn_play.clicked.connect(self.check_status)
        self.btn_pause.clicked.connect(self.check_status)
        self.btn_next.clicked.connect(lambda: self.player_playlist.next())
        self.btn_repeat_all.clicked.connect(self.check_repeat)
        self.btn_repeat_one.clicked.connect(self.check_repeat)

        self.btn_down.clicked.connect(self.volume_down)
        self.btn_mute.clicked.connect(self.check_volume)
        self.btn_unmute.clicked.connect(self.check_volume)
        self.btn_up.clicked.connect(self.volume_up)

        self.song_status.sliderMoved.connect(self.slider_position)
        self.player.positionChanged.connect(self.song_position)

        self.click_time = get_time() + 2

        self.show()
        self.list_friends.hide()
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

    def update_friend_list(self):
        self.friend_list = []
        self.list_friends.clear()
        result = db.get_friends(self.user.id)
        for idx, item in enumerate(result):
            if self.user.id == item[0]:
                friend_id = item[1]
            else:
                friend_id = item[0]

            self.friend_list.append(friend_id)
            username = db.get_username(friend_id)
            item = QtWidgets.QListWidgetItem(f'#{idx+1} // @{username}')
            self.list_friends.addItem(item)

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

            self.setup_playlist(selected)
            self.check_buttons()

    # # # # # # # # # # # #
    # ACTIVE SONG BUTTONS
    # # # # # # # # # # # #

    def setup_playlist(self, start_index):
        if self.playmode == LOCAL:
            pass
        else:
            if not self.widget_current.isVisible():
                self.widget_current.show()

            if self.list_friends.isVisible():
                self.list_friends.hide()
                self.list_songs.show()

            self.player_playlist = QMediaPlaylist()
            self.player_playlist.currentIndexChanged.connect(self.setup_song)
            self.check_mode()

            download_playlist(self.user.id, self.active_list, self.network, temporary = True)

            for song in self.active_list:
                if os.path.isfile(song.path):
                    full_path = os.path.join(os.getcwd(), song.path)
                else:
                    song_path = 'temp\\' + song.path[6:]
                    full_path = os.path.join(os.getcwd(), song_path)

                url = QtCore.QUrl.fromLocalFile(full_path)
                content = QMediaContent(url)
                self.player_playlist.addMedia(content)

            self.player.setPlaylist(self.player_playlist)
            self.player_playlist.setCurrentIndex(start_index)
            self.player.play()


    def setup_song(self):
        current_index = self.player_playlist.currentIndex()
        song = self.active_list[current_index]
        artist = db.get_artist_name(song.song_id)

        self.label_name.setText(song.name)
        self.label_artist.setText(artist)
        self.label_time.setText(str(timedelta(seconds=0)))
        self.label_length.setText(str(timedelta(seconds=song.length)))

        self.song_status.setValue(0)
        self.song_status.setMaximum(song.length)

        self.active_song = song
        if self.playmode != RECENT:
            db.add_user_recent(self.user.id, song.song_id)


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

        if self.player.state() == QMediaPlayer.PlayingState:
            self.btn_play.hide()
            self.btn_pause.show()
        else:
            self.btn_pause.hide()
            self.btn_play.show()

        if self.player.isMuted():
            self.btn_mute.hide()
            self.btn_unmute.show()
        else:
            self.btn_unmute.hide()
            self.btn_mute.show()


    def check_shuffle(self):
        self.shuffle = False if self.shuffle else True

        self.check_mode()
        self.check_buttons()


    def check_status(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            self.player.play()

        self.check_buttons()


    def check_repeat(self):
        self.repeat = REPEAT_ONE if self.repeat == REPEAT_ALL else REPEAT_ALL

        self.check_mode()
        self.check_buttons()


    def check_mode(self):
        if self.repeat == REPEAT_ONE:
            self.player_playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
        else:
            if self.shuffle:
                self.player_playlist.setPlaybackMode(QMediaPlaylist.Random)
            else:
                self.player_playlist.setPlaybackMode(QMediaPlaylist.Loop)

    # # # # # # # # # # # #
    # VOLUME BUTTONS
    # # # # # # # # # # # #

    def volume_down(self):
        volume = self.player.volume()
        self.player.setVolume(volume - 10)


    def check_volume(self):
        if self.player.isMuted():
            self.player.setMuted(False)
        else:
            self.player.setMuted(True)

        self.check_buttons()


    def volume_up(self):
        volume = self.player.volume()
        self.player.setVolume(volume + 10)

    # # # # # # # # # # # #
    # MEDIA PLAYER FUNCTIONS
    # # # # # # # # # # # #

    def slider_position(self):
        seconds = self.song_status.value()
        ms = seconds * 1000
        self.player.setPosition(ms)


    def song_position(self):
        seconds = int(self.player.position() / 1000)

        self.label_time.setText(str(timedelta(seconds=seconds)))
        self.song_status.setValue(seconds)

    # # # # # # # # # # # #
    # MORE BUTTONS
    # # # # # # # # # # # #

    def download_song(self, song):
        if self.online:
            start_new_thread(download_single, (self.user.id, song, self.network, ))
        else:
            self.popup = PopupWarning(self, 'Апликацију користите у офлајн режиму.\nОву опцију можете користити само док сте онлајн.', 'Офлајн режим')
            self.close()


    def add_song(self):
        if self.online:
            db.add_user_song(self.user.id, self.active_song.song_id)
        else:
            self.popup = PopupWarning(self, 'Апликацију користите у офлајн режиму.\nОву опцију можете користити само док сте онлајн.', 'Офлајн режим')
            self.close()


    def share_song(self):
        if self.online:
            if self.list_songs.isVisible():
                self.list_songs.hide()
                self.list_friends.show()
            else:
                self.list_friends.hide()
                self.list_songs.show()
        else:
            self.popup = PopupWarning(self, 'Апликацију користите у офлајн режиму.\nОву опцију можете користити само док сте онлајн.', 'Офлајн режим')
            self.close()


    def send_song(self):
        selected = self.list_friends.currentRow()
        friend_id = self.friend_list[selected]

        song = self.active_song
        artist = db.get_artist_name(song.artist_id)
        message = f'Тренутно слушам {artist} - {song.name}'

        db.send_message(self.user.id, friend_id, message)

        self.list_friends.hide()
        self.list_songs.show()

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


    def exit(self):
        del self.player

        self.back.show()
        self.close()


def get_time():
    return datetime.now().timestamp()