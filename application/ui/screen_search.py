# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_search.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SearchScreen(object):
    def setupUi(self, SearchScreen):
        SearchScreen.setObjectName("SearchScreen")
        SearchScreen.setWindowModality(QtCore.Qt.NonModal)
        SearchScreen.resize(490, 600)
        SearchScreen.setWindowOpacity(1.0)
        SearchScreen.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(SearchScreen)
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
        self.widget.setStyleSheet("QPushButton#btn_search, #btn_add, #btn_download {\n"
"    background-color: rgb(20, 92, 158);\n"
"    color: rgb(224, 224, 226);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_add:hover {\n"
"    background-color: rgb(19, 55, 88);\n"
"}\n"
"QPushButton#btn_add:pressed {\n"
"    background-color: rgb(19, 37, 53);\n"
"}")
        self.widget.setObjectName("widget")
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
        self.app_name = QtWidgets.QLabel(self.widget)
        self.app_name.setGeometry(QtCore.QRect(0, 0, 190, 60))
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
        self.label.setGeometry(QtCore.QRect(65, 35, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(224,224,226);")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.list_search = QtWidgets.QListWidget(self.widget)
        self.list_search.setGeometry(QtCore.QRect(10, 130, 450, 440))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
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
        self.input_search = QtWidgets.QLineEdit(self.widget)
        self.input_search.setGeometry(QtCore.QRect(10, 80, 191, 40))
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
        self.btn_search = QtWidgets.QPushButton(self.widget)
        self.btn_search.setGeometry(QtCore.QRect(210, 80, 40, 40))
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
        self.btn_mode = QtWidgets.QPushButton(self.widget)
        self.btn_mode.setGeometry(QtCore.QRect(260, 80, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_mode.setFont(font)
        self.btn_mode.setStyleSheet("QPushButton#btn_mode {\n"
"    background-color: rgb(20, 92, 158);\n"
"    color: rgb(224, 224, 226);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_mode:hover {\n"
"    background-color: rgb(19, 55, 88);\n"
"}\n"
"QPushButton#btn_mode:pressed {\n"
"    background-color: rgb(19, 37, 53);\n"
"}")
        self.btn_mode.setObjectName("btn_mode")
        self.btn_download = QtWidgets.QPushButton(self.widget)
        self.btn_download.setGeometry(QtCore.QRect(420, 80, 40, 40))
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
        self.downloading = QtWidgets.QLabel(self.widget)
        self.downloading.setGeometry(QtCore.QRect(210, 35, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.downloading.setFont(font)
        self.downloading.setStyleSheet("color: rgb(224,224,226);")
        self.downloading.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.downloading.setObjectName("downloading")
        self.btn_add = QtWidgets.QPushButton(self.widget)
        self.btn_add.setGeometry(QtCore.QRect(370, 80, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_add.setFont(font)
        self.btn_add.setStyleSheet("QPushButton#btn_add {\n"
"    border-image: url(:/icons/images/icons/add.png);\n"
"}\n"
"QPushButton#btn_add:hover {\n"
"    border-image: url(:/icons/images/icons/hover_add.png);\n"
"}")
        self.btn_add.setText("")
        self.btn_add.setObjectName("btn_add")
        self.app_bg = QtWidgets.QLabel(self.frame_border)
        self.app_bg.setGeometry(QtCore.QRect(0, 0, 491, 601))
        self.app_bg.setStyleSheet("border-image: url(:/images/images/welcome_bg.png);")
        self.app_bg.setText("")
        self.app_bg.setObjectName("app_bg")
        self.app_bg.raise_()
        self.frame.raise_()
        SearchScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SearchScreen)
        QtCore.QMetaObject.connectSlotsByName(SearchScreen)

    def retranslateUi(self, SearchScreen):
        _translate = QtCore.QCoreApplication.translate
        SearchScreen.setWindowTitle(_translate("SearchScreen", "MainWindow"))
        self.app_name.setText(_translate("SearchScreen", "??????????"))
        self.label.setText(_translate("SearchScreen", "?????????? ??????????????"))
        self.input_search.setPlaceholderText(_translate("SearchScreen", "?????? ????????????"))
        self.btn_mode.setText(_translate("SearchScreen", "?????????? ????????????"))
        self.downloading.setText(_translate("SearchScreen", "???????????????????? ?? ????????..."))
import res_rc
