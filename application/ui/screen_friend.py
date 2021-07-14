# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_friend.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FriendScreen(object):
    def setupUi(self, FriendScreen):
        FriendScreen.setObjectName("FriendScreen")
        FriendScreen.setWindowModality(QtCore.Qt.NonModal)
        FriendScreen.resize(490, 600)
        FriendScreen.setWindowOpacity(1.0)
        FriendScreen.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(FriendScreen)
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
        self.btn_page_add = QtWidgets.QPushButton(self.frame_left)
        self.btn_page_add.setGeometry(QtCore.QRect(0, 40, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_page_add.setFont(font)
        self.btn_page_add.setStyleSheet("")
        self.btn_page_add.setObjectName("btn_page_add")
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
        self.friends = QtWidgets.QLabel(self.frame_left)
        self.friends.setGeometry(QtCore.QRect(0, 120, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.friends.setFont(font)
        self.friends.setStyleSheet("color: rgb(224, 224, 226);")
        self.friends.setAlignment(QtCore.Qt.AlignCenter)
        self.friends.setObjectName("friends")
        self.list_friends = QtWidgets.QListWidget(self.frame_left)
        self.list_friends.setGeometry(QtCore.QRect(0, 160, 130, 410))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(8)
        self.list_friends.setFont(font)
        self.list_friends.setStyleSheet("QListWidget#list_friends {\n"
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
        self.list_friends.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_friends.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_friends.setObjectName("list_friends")
        self.btn_page_request = QtWidgets.QPushButton(self.frame_left)
        self.btn_page_request.setGeometry(QtCore.QRect(0, 80, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_page_request.setFont(font)
        self.btn_page_request.setStyleSheet("")
        self.btn_page_request.setObjectName("btn_page_request")
        self.stacked_pages = QtWidgets.QStackedWidget(self.widget)
        self.stacked_pages.setGeometry(QtCore.QRect(130, 70, 340, 510))
        self.stacked_pages.setStyleSheet("QStackedWidget#stacked_pages {\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"")
        self.stacked_pages.setObjectName("stacked_pages")
        self.page_add = QtWidgets.QWidget()
        self.page_add.setStyleSheet("QPushButton#btn_search, #btn_add {\n"
"    background-color: rgb(20, 92, 158);\n"
"    color: rgb(224, 224, 226);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_search:hover, #btn_add:hover {\n"
"    background-color: rgb(19, 55, 88);\n"
"}\n"
"QPushButton#btn_search:pressed, #btn_add:pressed {\n"
"    background-color: rgb(19, 37, 53);\n"
"}")
        self.page_add.setObjectName("page_add")
        self.list_search = QtWidgets.QListWidget(self.page_add)
        self.list_search.setGeometry(QtCore.QRect(10, 60, 320, 390))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(8)
        self.list_search.setFont(font)
        self.list_search.setStyleSheet("QListWidget#list_search {\n"
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
"}")
        self.list_search.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_search.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_search.setObjectName("list_search")
        self.input_name = QtWidgets.QLineEdit(self.page_add)
        self.input_name.setGeometry(QtCore.QRect(10, 10, 270, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.input_name.setFont(font)
        self.input_name.setStyleSheet("QLineEdit {\n"
"    background-color: rgba(0,0,0,0);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(20, 92, 158);\n"
"    color: rgb(224, 224, 226);\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"")
        self.input_name.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_name.setClearButtonEnabled(True)
        self.input_name.setObjectName("input_name")
        self.btn_search = QtWidgets.QPushButton(self.page_add)
        self.btn_search.setGeometry(QtCore.QRect(290, 10, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
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
        self.btn_add = QtWidgets.QPushButton(self.page_add)
        self.btn_add.setGeometry(QtCore.QRect(10, 460, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_add.setFont(font)
        self.btn_add.setStyleSheet("")
        self.btn_add.setObjectName("btn_add")
        self.stacked_pages.addWidget(self.page_add)
        self.page_request = QtWidgets.QWidget()
        self.page_request.setStyleSheet("QPushButton#req_delete, #req_accept, #req_refuse {\n"
"    background-color: rgb(20, 92, 158);\n"
"    color: rgb(224, 224, 226);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#req_delete:hover, #req_accept:hover, #req_refuse:hover {\n"
"    background-color: rgb(19, 55, 88);\n"
"}\n"
"QPushButton#req_delete:pressed, #req_accept:pressed, #req_refuse:pressed {\n"
"    background-color: rgb(19, 37, 53);\n"
"}")
        self.page_request.setObjectName("page_request")
        self.req_delete = QtWidgets.QPushButton(self.page_request)
        self.req_delete.setGeometry(QtCore.QRect(10, 210, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.req_delete.setFont(font)
        self.req_delete.setStyleSheet("")
        self.req_delete.setObjectName("req_delete")
        self.list_sent = QtWidgets.QListWidget(self.page_request)
        self.list_sent.setGeometry(QtCore.QRect(10, 30, 320, 171))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(8)
        self.list_sent.setFont(font)
        self.list_sent.setStyleSheet("QListWidget#list_sent {\n"
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
"}")
        self.list_sent.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_sent.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_sent.setObjectName("list_sent")
        self.list_received = QtWidgets.QListWidget(self.page_request)
        self.list_received.setGeometry(QtCore.QRect(10, 280, 320, 171))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(8)
        self.list_received.setFont(font)
        self.list_received.setStyleSheet("QListWidget#list_received {\n"
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
"}")
        self.list_received.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_received.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_received.setObjectName("list_received")
        self.req_accept = QtWidgets.QPushButton(self.page_request)
        self.req_accept.setGeometry(QtCore.QRect(10, 460, 155, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.req_accept.setFont(font)
        self.req_accept.setStyleSheet("")
        self.req_accept.setObjectName("req_accept")
        self.req_refuse = QtWidgets.QPushButton(self.page_request)
        self.req_refuse.setGeometry(QtCore.QRect(175, 460, 155, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.req_refuse.setFont(font)
        self.req_refuse.setStyleSheet("")
        self.req_refuse.setObjectName("req_refuse")
        self.friends_2 = QtWidgets.QLabel(self.page_request)
        self.friends_2.setGeometry(QtCore.QRect(10, 0, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.friends_2.setFont(font)
        self.friends_2.setStyleSheet("color: rgb(224, 224, 226);")
        self.friends_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.friends_2.setObjectName("friends_2")
        self.friends_3 = QtWidgets.QLabel(self.page_request)
        self.friends_3.setGeometry(QtCore.QRect(10, 250, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.friends_3.setFont(font)
        self.friends_3.setStyleSheet("color: rgb(224, 224, 226);")
        self.friends_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.friends_3.setObjectName("friends_3")
        self.stacked_pages.addWidget(self.page_request)
        self.page_friend = QtWidgets.QWidget()
        self.page_friend.setStyleSheet("QPushButton#btn_send, #btn_delete {\n"
"    background-color: rgb(20, 92, 158);\n"
"    color: rgb(224, 224, 226);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_send:hover, #btn_delete:hover {\n"
"    background-color: rgb(19, 55, 88);\n"
"}\n"
"QPushButton#btn_send:pressed, #btn_delete:pressed {\n"
"    background-color: rgb(19, 37, 53);\n"
"}\n"
"\n"
"QListWidget#list_playlist, #list_recent {\n"
"    color: rgb(224,224,226);\n"
"    background-color:rgba(0,0,0,0);\n"
"    border: 2px solid rgb(20,92,158);\n"
"    border-radius: 5px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"QListWidget::item:hover {\n"
"    background-color: rgb(20,92,158);\n"
"}\n"
"QListWidget::item:selected {\n"
"    background-color: rgb(19,55,88);\n"
"}\n"
"\n"
"QLabel#label_playlist, #label_recent {\n"
"    color: rgb(224, 224, 226);\n"
"    background-color: rgb(20,92,158);\n"
"    border-radius: 5px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"QLabel#label_art {\n"
"    border: 2px solid;\n"
"    background-color: rgb(224,224,226);\n"
"}")
        self.page_friend.setObjectName("page_friend")
        self.list_playlist = QtWidgets.QListWidget(self.page_friend)
        self.list_playlist.setGeometry(QtCore.QRect(10, 280, 155, 220))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.list_playlist.setFont(font)
        self.list_playlist.setStyleSheet("")
        self.list_playlist.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_playlist.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_playlist.setObjectName("list_playlist")
        self.list_recent = QtWidgets.QListWidget(self.page_friend)
        self.list_recent.setGeometry(QtCore.QRect(175, 280, 155, 220))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.list_recent.setFont(font)
        self.list_recent.setStyleSheet("")
        self.list_recent.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_recent.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_recent.setObjectName("list_recent")
        self.input_msg = QtWidgets.QPlainTextEdit(self.page_friend)
        self.input_msg.setGeometry(QtCore.QRect(10, 110, 320, 130))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.input_msg.setFont(font)
        self.input_msg.setStyleSheet("QPlainTextEdit#input_msg{\n"
"    color: rgb(224,224,226);\n"
"    background-color:rgba(0,0,0,0);\n"
"    border: 2px solid rgb(20,92,158);\n"
"    border-radius: 5px;\n"
"}")
        self.input_msg.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_msg.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_msg.setObjectName("input_msg")
        self.btn_delete = QtWidgets.QPushButton(self.page_friend)
        self.btn_delete.setGeometry(QtCore.QRect(290, 20, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_delete.setFont(font)
        self.btn_delete.setStyleSheet("QPushButton#btn_delete {\n"
"    border-image: url(:/icons/images/icons/delete.png);\n"
"}\n"
"QPushButton#btn_delete:hover {\n"
"    border-image: url(:/icons/images/icons/hover_delete.png);\n"
"}")
        self.btn_delete.setText("")
        self.btn_delete.setObjectName("btn_delete")
        self.label_playlist = QtWidgets.QLabel(self.page_friend)
        self.label_playlist.setGeometry(QtCore.QRect(10, 250, 155, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.label_playlist.setFont(font)
        self.label_playlist.setStyleSheet("")
        self.label_playlist.setAlignment(QtCore.Qt.AlignCenter)
        self.label_playlist.setObjectName("label_playlist")
        self.label_recent = QtWidgets.QLabel(self.page_friend)
        self.label_recent.setGeometry(QtCore.QRect(175, 250, 155, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.label_recent.setFont(font)
        self.label_recent.setStyleSheet("")
        self.label_recent.setAlignment(QtCore.Qt.AlignCenter)
        self.label_recent.setObjectName("label_recent")
        self.label_art = QtWidgets.QLabel(self.page_friend)
        self.label_art.setGeometry(QtCore.QRect(10, 10, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.label_art.setFont(font)
        self.label_art.setStyleSheet("")
        self.label_art.setAlignment(QtCore.Qt.AlignCenter)
        self.label_art.setObjectName("label_art")
        self.label_name = QtWidgets.QLabel(self.page_friend)
        self.label_name.setGeometry(QtCore.QRect(80, 10, 171, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("color: rgb(224, 224, 226);")
        self.label_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_name.setObjectName("label_name")
        self.label_user = QtWidgets.QLabel(self.page_friend)
        self.label_user.setGeometry(QtCore.QRect(80, 30, 171, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_user.setFont(font)
        self.label_user.setStyleSheet("color: rgb(224, 224, 226);")
        self.label_user.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_user.setObjectName("label_user")
        self.btn_send = QtWidgets.QPushButton(self.page_friend)
        self.btn_send.setGeometry(QtCore.QRect(290, 200, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_send.setFont(font)
        self.btn_send.setStyleSheet("QPushButton#btn_send {\n"
"    border-image: url(:/icons/images/icons/send.png);\n"
"}\n"
"QPushButton#btn_send:hover {\n"
"    border-image: url(:/icons/images/icons/hover_send.png);\n"
"}")
        self.btn_send.setText("")
        self.btn_send.setObjectName("btn_send")
        self.stacked_pages.addWidget(self.page_friend)
        self.app_bg = QtWidgets.QLabel(self.frame_border)
        self.app_bg.setGeometry(QtCore.QRect(0, 0, 491, 601))
        self.app_bg.setStyleSheet("border-image: url(:/images/images/welcome_bg.png);")
        self.app_bg.setText("")
        self.app_bg.setObjectName("app_bg")
        self.app_bg.raise_()
        self.frame.raise_()
        FriendScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(FriendScreen)
        self.stacked_pages.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(FriendScreen)

    def retranslateUi(self, FriendScreen):
        _translate = QtCore.QCoreApplication.translate
        FriendScreen.setWindowTitle(_translate("FriendScreen", "MainWindow"))
        self.app_name.setText(_translate("FriendScreen", "Прело"))
        self.label.setText(_translate("FriendScreen", "СНАГА КРАЈИНЕ"))
        self.btn_page_add.setText(_translate("FriendScreen", "Додај пријатеља"))
        self.options.setText(_translate("FriendScreen", "Опције"))
        self.friends.setText(_translate("FriendScreen", "Пријатељи"))
        self.btn_page_request.setText(_translate("FriendScreen", "Захтјеви"))
        self.input_name.setPlaceholderText(_translate("FriendScreen", "Корисничко име"))
        self.btn_add.setText(_translate("FriendScreen", "Пошаљи захтјев"))
        self.req_delete.setText(_translate("FriendScreen", "Избришии"))
        self.req_accept.setText(_translate("FriendScreen", "Прихвати"))
        self.req_refuse.setText(_translate("FriendScreen", "Одбиј"))
        self.friends_2.setText(_translate("FriendScreen", "Послати захтјеви"))
        self.friends_3.setText(_translate("FriendScreen", "Примљени захтјеви"))
        self.input_msg.setPlainText(_translate("FriendScreen", "dadadada"))
        self.input_msg.setPlaceholderText(_translate("FriendScreen", "Унесите поруку..."))
        self.label_playlist.setText(_translate("FriendScreen", "Албуми"))
        self.label_recent.setText(_translate("FriendScreen", "Недавно слушано"))
        self.label_art.setText(_translate("FriendScreen", "ART"))
        self.label_name.setText(_translate("FriendScreen", "Артис"))
        self.label_user.setText(_translate("FriendScreen", "Пјесмица"))
import res_rc
