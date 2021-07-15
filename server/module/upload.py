# Importing the libraries
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup

from mutagen.mp3 import MP3
from datetime import datetime, timedelta
from shutil import move
import db_server as db

# Importing UI
from ui.screen_upload import Ui_UploadScreen

# UPLOAD SCREEN
class UploadScreen(QMainWindow, Ui_UploadScreen):
    def __init__(self, last_screen, upload_log):
        super(UploadScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.old_path = os.getcwd()
        self.songs = []
        self.folder_path = None
        self.upload_log = upload_log

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_back.clicked.connect(self.exit)
        self.btn_open.clicked.connect(self.open)
        self.btn_delete.clicked.connect(self.delete)
        self.btn_upload.clicked.connect(self.upload)
        self.click_time = get_time() + 1

        db.connect(database='prelo')
        self.show()


    def open(self):
        new_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Изаберите фолдер')
        if not new_path:
            return False
        os.chdir(new_path)

        self.songs = []
        self.folder_path = new_path

        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for mp3 in files:
            if mp3.endswith('.mp3'):
                self.songs.append(mp3)  

        if self.songs:
            self.refresh_songs()
        else:
            self.list_files.clear()

        os.chdir(self.old_path)


    def delete(self):
        selected = self.list_files.selectedItems()
        if selected:
            index = selected[0].text()[1:]
            index = int(index.split()[0])

            self.songs.pop(index)
            self.refresh_songs()


    def upload(self):
        if self.songs:
            os.chdir(self.folder_path)

            for song in self.songs:
                print(f'[ + ] Uploading song... (( {song} ))')
                server_path = 'songs\\' + song
                original = self.folder_path + '\\' + song
                target = self.old_path + '\\' + server_path

                audio = MP3(song)
                length = audio.info.length
                song = song.split(' - ')
                artist = song[0]
                name = song[1][:-4]

                move(original, target)
                song_id = db.add_song(artist, name, server_path, length, 'Server Admin')

                time = datetime.now()
                self.upload_log.info(f'[ {time:%d.%m.%y. %H:%M:%S} ] Added song... (ID: {song_id}) ({artist} - {name})')

            os.chdir(self.old_path)
            self.list_files.clear()


    def refresh_songs(self):
        self.list_files.clear()
        os.chdir(self.folder_path)
        for idx, song in enumerate(self.songs):
            audio = MP3(song)
            length = audio.info.length

            song = song.split(' - ')
            artist = song[0]
            name = song[1][:-4]

            item = QtWidgets.QListWidgetItem(f'#{idx} // {artist} // {name} // {timedelta(seconds=length)}s')
            self.list_files.addItem(item)

        os.chdir(self.old_path)

    def exit(self):
        self.back.show()
        self.close()


def get_time():
    return datetime.now().timestamp()