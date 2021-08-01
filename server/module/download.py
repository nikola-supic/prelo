# Importing the libraries
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from youtube_dl import YoutubeDL

# Importing UI
from ui.screen_download import Ui_DownloadScreen

# DOWNLOAD SCREEN
class DownloadScreen(QMainWindow, Ui_DownloadScreen):
    def __init__(self, last_screen, upload_log):
        super(DownloadScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.old_path = os.getcwd()
        self.folder_path = None
        self.upload_log = upload_log

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_back.clicked.connect(self.exit)
        self.btn_download.clicked.connect(self.download)

        self.show()

    def download(self):
        url = self.input_url.text()
        name = self.input_name.text()
        author = self.input_author.text()
        
        if url and name and author:
            self.input_url.setText('')
            self.input_author.setText('')
            self.input_name.setText('')

            path = f'{os.getcwd()}\\download\\{author} - {name}'
            opts = {
                'verbose': True,
                'fixup': 'detect_or_warn',              # Correct known faults of the file.
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'extractaudio' : True,                  # Only keep the audio.
                'outtmpl': path + '.%(ext)s',           # Save path
                'noplaylist' : False,                   # Only download single song, not playlist
            }
            yt_dl = YoutubeDL(opts)
            yt_dl.download([url])



    def exit(self):
        self.back.show()
        self.close()
