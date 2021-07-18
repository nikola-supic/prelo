# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsScreen(object):
    def setupUi(self, SettingsScreen):
        SettingsScreen.setObjectName("SettingsScreen")
        SettingsScreen.setWindowModality(QtCore.Qt.NonModal)
        SettingsScreen.resize(490, 600)
        SettingsScreen.setWindowOpacity(1.0)
        SettingsScreen.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(SettingsScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_border = QtWidgets.QFrame(self.centralwidget)
        self.frame_border.setGeometry(QtCore.QRect(0, 0, 490, 601))
        self.frame_border.setStyleSheet("QFrame {    \n"
"    background-color: rgba(18, 18, 18, 175);\n"
"}\n"
"QLabel {\n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.frame_border.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_border.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_border.setObjectName("frame_border")
        self.frame = QtWidgets.QFrame(self.frame_border)
        self.frame.setGeometry(QtCore.QRect(10, 10, 470, 580))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(0, 0, 471, 580))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.app_name = QtWidgets.QLabel(self.widget)
        self.app_name.setGeometry(QtCore.QRect(130, 0, 190, 60))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(42)
        font.setBold(True)
        font.setWeight(75)
        self.app_name.setFont(font)
        self.app_name.setStyleSheet("color: rgb(20, 92, 158);")
        self.app_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.app_name.setAlignment(QtCore.Qt.AlignCenter)
        self.app_name.setObjectName("app_name")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(195, 35, 115, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(224,224,226);")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.btn_back = QtWidgets.QPushButton(self.widget)
        self.btn_back.setGeometry(QtCore.QRect(430, 10, 30, 30))
        self.btn_back.setStyleSheet("QPushButton#btn_back {\n"
"    border-image: url(:/menu/images/menu/exit.png);\n"
"}\n"
"QPushButton#btn_back:hover {\n"
"    border-image: url(:/menu/images/menu/hover_exit.png);\n"
"}")
        self.btn_back.setText("")
        self.btn_back.setObjectName("btn_back")
        self.frame_left = QtWidgets.QFrame(self.widget)
        self.frame_left.setGeometry(QtCore.QRect(0, 0, 130, 580))
        self.frame_left.setStyleSheet("QPushButton {\n"
"    background-color: rgb(20, 92, 158);\n"
"    color: rgb(224, 224, 226);\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(19, 55, 88);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(19, 37, 53);\n"
"}")
        self.frame_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left.setObjectName("frame_left")
        self.btn_page_acc = QtWidgets.QPushButton(self.frame_left)
        self.btn_page_acc.setGeometry(QtCore.QRect(0, 80, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_page_acc.setFont(font)
        self.btn_page_acc.setStyleSheet("")
        self.btn_page_acc.setObjectName("btn_page_acc")
        self.options = QtWidgets.QLabel(self.frame_left)
        self.options.setGeometry(QtCore.QRect(0, 0, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.options.setFont(font)
        self.options.setStyleSheet("color: rgb(224, 224, 226);")
        self.options.setAlignment(QtCore.Qt.AlignCenter)
        self.options.setObjectName("options")
        self.btn_page_security = QtWidgets.QPushButton(self.frame_left)
        self.btn_page_security.setGeometry(QtCore.QRect(0, 120, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_page_security.setFont(font)
        self.btn_page_security.setStyleSheet("")
        self.btn_page_security.setObjectName("btn_page_security")
        self.btn_page_info = QtWidgets.QPushButton(self.frame_left)
        self.btn_page_info.setGeometry(QtCore.QRect(0, 40, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_page_info.setFont(font)
        self.btn_page_info.setStyleSheet("")
        self.btn_page_info.setObjectName("btn_page_info")
        self.btn_page_song = QtWidgets.QPushButton(self.frame_left)
        self.btn_page_song.setGeometry(QtCore.QRect(0, 160, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_page_song.setFont(font)
        self.btn_page_song.setStyleSheet("")
        self.btn_page_song.setObjectName("btn_page_song")
        self.playlist = QtWidgets.QLabel(self.frame_left)
        self.playlist.setGeometry(QtCore.QRect(0, 200, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.playlist.setFont(font)
        self.playlist.setStyleSheet("color: rgb(224, 224, 226);")
        self.playlist.setAlignment(QtCore.Qt.AlignCenter)
        self.playlist.setObjectName("playlist")
        self.list_playlist = QtWidgets.QListWidget(self.frame_left)
        self.list_playlist.setGeometry(QtCore.QRect(0, 240, 130, 340))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(8)
        self.list_playlist.setFont(font)
        self.list_playlist.setStyleSheet("QListWidget#list_playlist {\n"
"    color: rgb(224,224,226);\n"
"    background-color:rgba(0,0,0,0);\n"
"    border-radius: 0px;\n"
"}\n"
"QListWidget::item:hover {\n"
"    background-color: rgb(20,92,158);\n"
"}\n"
"QListWidget::item:selected {\n"
"    background-color: rgb(19,55,88);\n"
"}")
        self.list_playlist.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_playlist.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_playlist.setObjectName("list_playlist")
        self.stacked_pages = QtWidgets.QStackedWidget(self.widget)
        self.stacked_pages.setGeometry(QtCore.QRect(130, 70, 340, 510))
        self.stacked_pages.setStyleSheet("QStackedWidget#stacked_pages {\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"QPushButton#btn_acc_save, #btn_security_save{\n"
"    background-color: rgb(20, 92, 158);\n"
"    color: rgb(224, 224, 226);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_save:hover, #btn_save_2:hover {\n"
"    background-color: rgb(19, 55, 88);\n"
"}\n"
"QPushButton#btn_save:pressed, #btn_save_2:pressed {\n"
"    background-color: rgb(19, 37, 53);\n"
"}\n"
"QLineEdit {\n"
"    background-color: rgba(0,0,0,0);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(20, 92, 158);\n"
"    color: rgb(224, 224, 226);\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QListWidget#list_search, #playlist_songs, #list_recent, #list_song {\n"
"    color: rgb(224,224,226);\n"
"    background-color:rgba(0,0,0,0);\n"
"    border: 2px solid rgb(20,92,158);\n"
"    border-radius: 5px;\n"
"}\n"
"QListWidget::item:hover {\n"
"    background-color: rgb(20,92,158);\n"
"}\n"
"QListWidget::item:selected {\n"
"    background-color: rgb(19,55,88);\n"
"}\n"
"")
        self.stacked_pages.setObjectName("stacked_pages")
        self.page_info = QtWidgets.QWidget()
        self.page_info.setStyleSheet("QPlainTextEdit#info, #info_2 {\n"
"    color: rgb(224,224,226);\n"
"    background-color:rgba(0,0,0,0);\n"
"    border: 2px solid rgb(20,92,158);\n"
"    border-radius: 5px;\n"
"    padding-left: 2px;\n"
"}")
        self.page_info.setObjectName("page_info")
        self.info = QtWidgets.QPlainTextEdit(self.page_info)
        self.info.setGeometry(QtCore.QRect(10, 100, 320, 100))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.info.setFont(font)
        self.info.setStyleSheet("QPlainTextEdit#input_msg{\n"
"    color: rgb(224,224,226);\n"
"    background-color:rgba(0,0,0,0);\n"
"    border: 2px solid rgb(20,92,158);\n"
"    border-radius: 5px;\n"
"    padding-left: 2px;\n"
"}")
        self.info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.info.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.info.setReadOnly(True)
        self.info.setObjectName("info")
        self.settings_5 = QtWidgets.QLabel(self.page_info)
        self.settings_5.setGeometry(QtCore.QRect(12, 70, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.settings_5.setFont(font)
        self.settings_5.setStyleSheet("color: rgb(224, 224, 226);")
        self.settings_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.settings_5.setObjectName("settings_5")
        self.user_name = QtWidgets.QLabel(self.page_info)
        self.user_name.setGeometry(QtCore.QRect(80, 10, 170, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.user_name.setFont(font)
        self.user_name.setStyleSheet("color: rgb(224, 224, 226);")
        self.user_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.user_name.setObjectName("user_name")
        self.user_username = QtWidgets.QLabel(self.page_info)
        self.user_username.setGeometry(QtCore.QRect(80, 30, 170, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.user_username.setFont(font)
        self.user_username.setStyleSheet("color: rgb(224, 224, 226);")
        self.user_username.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.user_username.setObjectName("user_username")
        self.user_art = QtWidgets.QLabel(self.page_info)
        self.user_art.setGeometry(QtCore.QRect(10, 10, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.user_art.setFont(font)
        self.user_art.setStyleSheet("border-image: url(:/art/images/art/art_1.png);")
        self.user_art.setText("")
        self.user_art.setAlignment(QtCore.Qt.AlignCenter)
        self.user_art.setObjectName("user_art")
        self.list_recent = QtWidgets.QListWidget(self.page_info)
        self.list_recent.setGeometry(QtCore.QRect(10, 230, 320, 271))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.list_recent.setFont(font)
        self.list_recent.setStyleSheet("")
        self.list_recent.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_recent.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_recent.setObjectName("list_recent")
        self.settings_6 = QtWidgets.QLabel(self.page_info)
        self.settings_6.setGeometry(QtCore.QRect(12, 200, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.settings_6.setFont(font)
        self.settings_6.setStyleSheet("color: rgb(224, 224, 226);")
        self.settings_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.settings_6.setObjectName("settings_6")
        self.stacked_pages.addWidget(self.page_info)
        self.page_acc = QtWidgets.QWidget()
        self.page_acc.setStyleSheet("")
        self.page_acc.setObjectName("page_acc")
        self.input_first = QtWidgets.QLineEdit(self.page_acc)
        self.input_first.setGeometry(QtCore.QRect(10, 30, 155, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.input_first.setFont(font)
        self.input_first.setStyleSheet("")
        self.input_first.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_first.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_first.setClearButtonEnabled(True)
        self.input_first.setObjectName("input_first")
        self.btn_acc_save = QtWidgets.QPushButton(self.page_acc)
        self.btn_acc_save.setGeometry(QtCore.QRect(10, 460, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_acc_save.setFont(font)
        self.btn_acc_save.setStyleSheet("")
        self.btn_acc_save.setObjectName("btn_acc_save")
        self.input_last = QtWidgets.QLineEdit(self.page_acc)
        self.input_last.setGeometry(QtCore.QRect(175, 30, 155, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.input_last.setFont(font)
        self.input_last.setStyleSheet("")
        self.input_last.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_last.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_last.setClearButtonEnabled(True)
        self.input_last.setObjectName("input_last")
        self.input_username = QtWidgets.QLineEdit(self.page_acc)
        self.input_username.setGeometry(QtCore.QRect(10, 80, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.input_username.setFont(font)
        self.input_username.setStyleSheet("")
        self.input_username.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_username.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_username.setClearButtonEnabled(True)
        self.input_username.setObjectName("input_username")
        self.input_day = QtWidgets.QLineEdit(self.page_acc)
        self.input_day.setGeometry(QtCore.QRect(10, 150, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.input_day.setFont(font)
        self.input_day.setStyleSheet("")
        self.input_day.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_day.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_day.setClearButtonEnabled(True)
        self.input_day.setObjectName("input_day")
        self.input_month = QtWidgets.QLineEdit(self.page_acc)
        self.input_month.setGeometry(QtCore.QRect(120, 150, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.input_month.setFont(font)
        self.input_month.setStyleSheet("")
        self.input_month.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_month.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_month.setClearButtonEnabled(True)
        self.input_month.setObjectName("input_month")
        self.input_year = QtWidgets.QLineEdit(self.page_acc)
        self.input_year.setGeometry(QtCore.QRect(230, 150, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.input_year.setFont(font)
        self.input_year.setStyleSheet("")
        self.input_year.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_year.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_year.setClearButtonEnabled(True)
        self.input_year.setObjectName("input_year")
        self.settings = QtWidgets.QLabel(self.page_acc)
        self.settings.setGeometry(QtCore.QRect(12, 0, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.settings.setFont(font)
        self.settings.setStyleSheet("color: rgb(224, 224, 226);")
        self.settings.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.settings.setObjectName("settings")
        self.settings_2 = QtWidgets.QLabel(self.page_acc)
        self.settings_2.setGeometry(QtCore.QRect(12, 120, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.settings_2.setFont(font)
        self.settings_2.setStyleSheet("color: rgb(224, 224, 226);")
        self.settings_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.settings_2.setObjectName("settings_2")
        self.stacked_pages.addWidget(self.page_acc)
        self.page_security = QtWidgets.QWidget()
        self.page_security.setObjectName("page_security")
        self.input_pw = QtWidgets.QLineEdit(self.page_security)
        self.input_pw.setGeometry(QtCore.QRect(10, 30, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.input_pw.setFont(font)
        self.input_pw.setStyleSheet("")
        self.input_pw.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.input_pw.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_pw.setClearButtonEnabled(True)
        self.input_pw.setObjectName("input_pw")
        self.input_pw_2 = QtWidgets.QLineEdit(self.page_security)
        self.input_pw_2.setGeometry(QtCore.QRect(10, 80, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.input_pw_2.setFont(font)
        self.input_pw_2.setStyleSheet("")
        self.input_pw_2.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.input_pw_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_pw_2.setClearButtonEnabled(True)
        self.input_pw_2.setObjectName("input_pw_2")
        self.input_email = QtWidgets.QLineEdit(self.page_security)
        self.input_email.setGeometry(QtCore.QRect(10, 150, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.input_email.setFont(font)
        self.input_email.setStyleSheet("")
        self.input_email.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_email.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_email.setClearButtonEnabled(True)
        self.input_email.setObjectName("input_email")
        self.btn_security_save = QtWidgets.QPushButton(self.page_security)
        self.btn_security_save.setGeometry(QtCore.QRect(10, 460, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_security_save.setFont(font)
        self.btn_security_save.setStyleSheet("")
        self.btn_security_save.setObjectName("btn_security_save")
        self.settings_3 = QtWidgets.QLabel(self.page_security)
        self.settings_3.setGeometry(QtCore.QRect(12, 0, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.settings_3.setFont(font)
        self.settings_3.setStyleSheet("color: rgb(224, 224, 226);")
        self.settings_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.settings_3.setObjectName("settings_3")
        self.settings_4 = QtWidgets.QLabel(self.page_security)
        self.settings_4.setGeometry(QtCore.QRect(12, 120, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.settings_4.setFont(font)
        self.settings_4.setStyleSheet("color: rgb(224, 224, 226);")
        self.settings_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.settings_4.setObjectName("settings_4")
        self.stacked_pages.addWidget(self.page_security)
        self.page_song = QtWidgets.QWidget()
        self.page_song.setStyleSheet("QPushButton#btn_remove, #btn_download {\n"
"    background-color: rgb(20, 92, 158);\n"
"    color: rgb(224, 224, 226);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_remove:hover, #btn_download:hover {\n"
"    background-color: rgb(19, 55, 88);\n"
"}\n"
"QPushButton#btn_remove:pressed, #btn_download:pressed {\n"
"    background-color: rgb(19, 37, 53);\n"
"}")
        self.page_song.setObjectName("page_song")
        self.list_song = QtWidgets.QListWidget(self.page_song)
        self.list_song.setGeometry(QtCore.QRect(10, 30, 320, 391))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.list_song.setFont(font)
        self.list_song.setStyleSheet("")
        self.list_song.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_song.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_song.setObjectName("list_song")
        self.settings_7 = QtWidgets.QLabel(self.page_song)
        self.settings_7.setGeometry(QtCore.QRect(12, 0, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.settings_7.setFont(font)
        self.settings_7.setStyleSheet("color: rgb(224, 224, 226);")
        self.settings_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.settings_7.setObjectName("settings_7")
        self.widget_song = QtWidgets.QWidget(self.page_song)
        self.widget_song.setGeometry(QtCore.QRect(0, 420, 340, 91))
        self.widget_song.setObjectName("widget_song")
        self.btn_remove = QtWidgets.QPushButton(self.widget_song)
        self.btn_remove.setGeometry(QtCore.QRect(300, 10, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_remove.setFont(font)
        self.btn_remove.setStyleSheet("QPushButton#btn_remove {\n"
"    border-image: url(:/icons/images/icons/delete.png);\n"
"}\n"
"QPushButton#btn_remove:hover {\n"
"    border-image: url(:/icons/images/icons/hover_delete.png);\n"
"}")
        self.btn_remove.setText("")
        self.btn_remove.setObjectName("btn_remove")
        self.song_art = QtWidgets.QLabel(self.widget_song)
        self.song_art.setGeometry(QtCore.QRect(10, 10, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.song_art.setFont(font)
        self.song_art.setStyleSheet("border-image: url(:/art/images/art/art_1.png);")
        self.song_art.setText("")
        self.song_art.setAlignment(QtCore.Qt.AlignCenter)
        self.song_art.setObjectName("song_art")
        self.song_name = QtWidgets.QLabel(self.widget_song)
        self.song_name.setGeometry(QtCore.QRect(90, 15, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.song_name.setFont(font)
        self.song_name.setStyleSheet("color: rgb(224, 224, 226);")
        self.song_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.song_name.setObjectName("song_name")
        self.btn_download = QtWidgets.QPushButton(self.widget_song)
        self.btn_download.setGeometry(QtCore.QRect(300, 50, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_download.setFont(font)
        self.btn_download.setStyleSheet("QPushButton#btn_download {\n"
"    border-image: url(:/icons/images/icons/download.png);\n"
"}\n"
"QPushButton#btn_download:hover {\n"
"    border-image: url(:/icons/images/icons/hover_download.png);\n"
"}")
        self.btn_download.setText("")
        self.btn_download.setObjectName("btn_download")
        self.song_artist = QtWidgets.QLabel(self.widget_song)
        self.song_artist.setGeometry(QtCore.QRect(90, 35, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.song_artist.setFont(font)
        self.song_artist.setStyleSheet("color: rgb(224, 224, 226);")
        self.song_artist.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.song_artist.setObjectName("song_artist")
        self.stacked_pages.addWidget(self.page_song)
        self.page_playlist = QtWidgets.QWidget()
        self.page_playlist.setStyleSheet("QPushButton#btn_playlist_remove, #btn_playlist_download, #btn_save, #btn_search {\n"
"    background-color: rgb(20, 92, 158);\n"
"    color: rgb(224, 224, 226);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_playlist_remove:hover, #btn_playlist_download :hover, #btn_save:hover, #btn_search:hover {\n"
"    background-color: rgb(19, 55, 88);\n"
"}\n"
"QPushButton#btn_playlist_remove:pressed, #btn_playlist_download :pressed, #btn_save:pressed, #btn_search:pressed {\n"
"    background-color: rgb(19, 37, 53);\n"
"}")
        self.page_playlist.setObjectName("page_playlist")
        self.settings_8 = QtWidgets.QLabel(self.page_playlist)
        self.settings_8.setGeometry(QtCore.QRect(12, 40, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.settings_8.setFont(font)
        self.settings_8.setStyleSheet("color: rgb(224, 224, 226);")
        self.settings_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.settings_8.setObjectName("settings_8")
        self.playlist_songs = QtWidgets.QListWidget(self.page_playlist)
        self.playlist_songs.setGeometry(QtCore.QRect(10, 70, 320, 151))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.playlist_songs.setFont(font)
        self.playlist_songs.setStyleSheet("")
        self.playlist_songs.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.playlist_songs.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.playlist_songs.setObjectName("playlist_songs")
        self.playlist_desc = QtWidgets.QLabel(self.page_playlist)
        self.playlist_desc.setGeometry(QtCore.QRect(12, 20, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.playlist_desc.setFont(font)
        self.playlist_desc.setStyleSheet("color: rgb(224, 224, 226);")
        self.playlist_desc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.playlist_desc.setObjectName("playlist_desc")
        self.playlist_name = QtWidgets.QLabel(self.page_playlist)
        self.playlist_name.setGeometry(QtCore.QRect(12, 0, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.playlist_name.setFont(font)
        self.playlist_name.setStyleSheet("color: rgb(224, 224, 226);")
        self.playlist_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.playlist_name.setObjectName("playlist_name")
        self.btn_playlist_download = QtWidgets.QPushButton(self.page_playlist)
        self.btn_playlist_download.setGeometry(QtCore.QRect(300, 10, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_playlist_download.setFont(font)
        self.btn_playlist_download.setStyleSheet("QPushButton#btn_playlist_download {\n"
"    border-image: url(:/icons/images/icons/download.png);\n"
"}\n"
"QPushButton#btn_playlist_download:hover {\n"
"    border-image: url(:/icons/images/icons/hover_download.png);\n"
"}")
        self.btn_playlist_download.setText("")
        self.btn_playlist_download.setObjectName("btn_playlist_download")
        self.btn_playlist_remove = QtWidgets.QPushButton(self.page_playlist)
        self.btn_playlist_remove.setGeometry(QtCore.QRect(260, 10, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_playlist_remove.setFont(font)
        self.btn_playlist_remove.setStyleSheet("QPushButton#btn_playlist_remove {\n"
"    border-image: url(:/icons/images/icons/delete.png);\n"
"}\n"
"QPushButton#btn_playlist_remove:hover {\n"
"    border-image: url(:/icons/images/icons/hover_delete.png);\n"
"}")
        self.btn_playlist_remove.setText("")
        self.btn_playlist_remove.setObjectName("btn_playlist_remove")
        self.widget_edit = QtWidgets.QWidget(self.page_playlist)
        self.widget_edit.setGeometry(QtCore.QRect(0, 230, 341, 281))
        self.widget_edit.setObjectName("widget_edit")
        self.settings_9 = QtWidgets.QLabel(self.widget_edit)
        self.settings_9.setGeometry(QtCore.QRect(12, -10, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.settings_9.setFont(font)
        self.settings_9.setStyleSheet("color: rgb(224, 224, 226);")
        self.settings_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.settings_9.setObjectName("settings_9")
        self.input_search = QtWidgets.QLineEdit(self.widget_edit)
        self.input_search.setGeometry(QtCore.QRect(10, 20, 271, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.input_search.setFont(font)
        self.input_search.setStyleSheet("QLineEdit {\n"
"    background-color: rgba(0,0,0,0);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(20, 92, 158);\n"
"    color: rgb(224, 224, 226);\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"")
        self.input_search.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_search.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_search.setClearButtonEnabled(True)
        self.input_search.setObjectName("input_search")
        self.list_search = QtWidgets.QListWidget(self.widget_edit)
        self.list_search.setGeometry(QtCore.QRect(10, 70, 320, 151))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.list_search.setFont(font)
        self.list_search.setStyleSheet("")
        self.list_search.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_search.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_search.setObjectName("list_search")
        self.check_public = QtWidgets.QCheckBox(self.widget_edit)
        self.check_public.setGeometry(QtCore.QRect(10, 230, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.check_public.setFont(font)
        self.check_public.setStyleSheet("color: rgb(224,224,226);")
        self.check_public.setObjectName("check_public")
        self.btn_save = QtWidgets.QPushButton(self.widget_edit)
        self.btn_save.setGeometry(QtCore.QRect(200, 230, 131, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet("")
        self.btn_save.setObjectName("btn_save")
        self.btn_search = QtWidgets.QPushButton(self.widget_edit)
        self.btn_search.setGeometry(QtCore.QRect(290, 20, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_search.setFont(font)
        self.btn_search.setStyleSheet("QPushButton#btn_search {\n"
"    border-image: url(:/icons/images/icons/search.png);\n"
"}\n"
"QPushButton#btn_search:hover {\n"
"    border-image: url(:/icons/images/icons/hover_search.png);\n"
"}")
        self.btn_search.setText("")
        self.btn_search.setObjectName("btn_search")
        self.stacked_pages.addWidget(self.page_playlist)
        self.app_bg = QtWidgets.QLabel(self.frame_border)
        self.app_bg.setGeometry(QtCore.QRect(0, 0, 491, 601))
        self.app_bg.setStyleSheet("border-image: url(:/images/images/welcome_bg.png);")
        self.app_bg.setText("")
        self.app_bg.setObjectName("app_bg")
        self.app_bg.raise_()
        self.frame.raise_()
        SettingsScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsScreen)
        self.stacked_pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SettingsScreen)

    def retranslateUi(self, SettingsScreen):
        _translate = QtCore.QCoreApplication.translate
        SettingsScreen.setWindowTitle(_translate("SettingsScreen", "MainWindow"))
        self.app_name.setText(_translate("SettingsScreen", "Прело"))
        self.label.setText(_translate("SettingsScreen", "СНАГА КРАЈИНЕ"))
        self.btn_page_acc.setText(_translate("SettingsScreen", "Налог"))
        self.options.setText(_translate("SettingsScreen", "Опције"))
        self.btn_page_security.setText(_translate("SettingsScreen", "Сигурност"))
        self.btn_page_info.setText(_translate("SettingsScreen", "Информације"))
        self.btn_page_song.setText(_translate("SettingsScreen", "Пјесме"))
        self.playlist.setText(_translate("SettingsScreen", "Албуми"))
        self.info.setPlainText(_translate("SettingsScreen", "Рођендан: \n"
"Ваш мејл: \n"
"Админ: \n"
"Датум регистрације: "))
        self.info.setPlaceholderText(_translate("SettingsScreen", "Унесите поруку..."))
        self.settings_5.setText(_translate("SettingsScreen", "Информације"))
        self.user_name.setText(_translate("SettingsScreen", "Артис"))
        self.user_username.setText(_translate("SettingsScreen", "Пјесмица"))
        self.settings_6.setText(_translate("SettingsScreen", "Недавно слушано"))
        self.input_first.setPlaceholderText(_translate("SettingsScreen", "Име"))
        self.btn_acc_save.setText(_translate("SettingsScreen", "Сачувај измјене"))
        self.input_last.setPlaceholderText(_translate("SettingsScreen", "Презиме"))
        self.input_username.setPlaceholderText(_translate("SettingsScreen", "Корисничко име"))
        self.input_day.setPlaceholderText(_translate("SettingsScreen", "Дан"))
        self.input_month.setPlaceholderText(_translate("SettingsScreen", "Мјесец"))
        self.input_year.setPlaceholderText(_translate("SettingsScreen", "Година"))
        self.settings.setText(_translate("SettingsScreen", "Основне информације"))
        self.settings_2.setText(_translate("SettingsScreen", "Рођендан"))
        self.input_pw.setPlaceholderText(_translate("SettingsScreen", "Нова лозинка"))
        self.input_pw_2.setPlaceholderText(_translate("SettingsScreen", "Потврдите нову лозинку"))
        self.input_email.setPlaceholderText(_translate("SettingsScreen", "Мејл"))
        self.btn_security_save.setText(_translate("SettingsScreen", "Сачувај измјене"))
        self.settings_3.setText(_translate("SettingsScreen", "Промјена лозинке"))
        self.settings_4.setText(_translate("SettingsScreen", "Промјена мејла"))
        self.settings_7.setText(_translate("SettingsScreen", "Твоје пјесме"))
        self.song_name.setText(_translate("SettingsScreen", "PJESMA"))
        self.song_artist.setText(_translate("SettingsScreen", "ARTT"))
        self.settings_8.setText(_translate("SettingsScreen", "Пјесме у албуму (двоклик да избришеш)"))
        self.playlist_desc.setText(_translate("SettingsScreen", "ARTT"))
        self.playlist_name.setText(_translate("SettingsScreen", "PJESMA"))
        self.settings_9.setText(_translate("SettingsScreen", "Додај пјесму у албум"))
        self.input_search.setPlaceholderText(_translate("SettingsScreen", "Име пјесме"))
        self.check_public.setText(_translate("SettingsScreen", "Јавна плејлиста"))
        self.btn_save.setText(_translate("SettingsScreen", "Сачувај"))
import res_rc
