# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_download.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DownloadScreen(object):
    def setupUi(self, DownloadScreen):
        DownloadScreen.setObjectName("DownloadScreen")
        DownloadScreen.resize(700, 360)
        self.centralwidget = QtWidgets.QWidget(DownloadScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_border = QtWidgets.QFrame(self.centralwidget)
        self.frame_border.setGeometry(QtCore.QRect(0, 0, 700, 360))
        self.frame_border.setStyleSheet("QFrame {    \n"
"    background-color: rgba(18, 18, 18, 175);    \n"
"}\n"
"QLabel {\n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.frame_border.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_border.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_border.setObjectName("frame_border")
        self.frame = QtWidgets.QFrame(self.frame_border)
        self.frame.setGeometry(QtCore.QRect(10, 10, 680, 340))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(0, 0, 680, 340))
        self.widget.setStyleSheet("QPushButton#btn_download{\n"
"    background-color: rgb(20, 92, 158);\n"
"    color: rgb(224, 224, 226);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_download:hover {\n"
"    background-color: rgb(19, 55, 88);\n"
"}\n"
"QPushButton#btn_download:pressed {\n"
"    background-color: rgb(19, 37, 53);\n"
"}\n"
"QLineEdit {\n"
"    background-color: rgba(0,0,0,0);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(20, 92, 158);\n"
"    color: rgb(224, 224, 226);\n"
"    padding-left: 5px;\n"
"}QPushButton {\n"
"    border: none;\n"
"}")
        self.widget.setObjectName("widget")
        self.app = QtWidgets.QLabel(self.widget)
        self.app.setGeometry(QtCore.QRect(0, 0, 680, 70))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(42)
        font.setBold(True)
        font.setWeight(75)
        self.app.setFont(font)
        self.app.setStyleSheet("color: rgb(20, 92, 158);")
        self.app.setAlignment(QtCore.Qt.AlignCenter)
        self.app.setObjectName("app")
        self.app_2 = QtWidgets.QLabel(self.widget)
        self.app_2.setGeometry(QtCore.QRect(0, 60, 680, 30))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(14)
        self.app_2.setFont(font)
        self.app_2.setStyleSheet("color: rgb(224,224,226);")
        self.app_2.setAlignment(QtCore.Qt.AlignCenter)
        self.app_2.setObjectName("app_2")
        self.btn_back = QtWidgets.QPushButton(self.widget)
        self.btn_back.setGeometry(QtCore.QRect(620, 20, 40, 40))
        self.btn_back.setStyleSheet("QPushButton#btn_back {\n"
"    border-image: url(:/images/images/back.png);\n"
"}\n"
"QPushButton#btn_back:hover {\n"
"    border-image: url(:/images/images/hover_back.png);\n"
"}")
        self.btn_back.setText("")
        self.btn_back.setObjectName("btn_back")
        self.input_url = QtWidgets.QLineEdit(self.widget)
        self.input_url.setGeometry(QtCore.QRect(150, 110, 380, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.input_url.setFont(font)
        self.input_url.setClearButtonEnabled(True)
        self.input_url.setObjectName("input_url")
        self.input_author = QtWidgets.QLineEdit(self.widget)
        self.input_author.setGeometry(QtCore.QRect(150, 160, 380, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.input_author.setFont(font)
        self.input_author.setClearButtonEnabled(True)
        self.input_author.setObjectName("input_author")
        self.input_name = QtWidgets.QLineEdit(self.widget)
        self.input_name.setGeometry(QtCore.QRect(150, 210, 380, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.input_name.setFont(font)
        self.input_name.setClearButtonEnabled(True)
        self.input_name.setObjectName("input_name")
        self.btn_download = QtWidgets.QPushButton(self.widget)
        self.btn_download.setGeometry(QtCore.QRect(150, 260, 380, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.btn_download.setFont(font)
        self.btn_download.setObjectName("btn_download")
        DownloadScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(DownloadScreen)
        QtCore.QMetaObject.connectSlotsByName(DownloadScreen)

    def retranslateUi(self, DownloadScreen):
        _translate = QtCore.QCoreApplication.translate
        DownloadScreen.setWindowTitle(_translate("DownloadScreen", "MainWindow"))
        self.app.setText(_translate("DownloadScreen", "Прело"))
        self.app_2.setText(_translate("DownloadScreen", "Скини музику са јутубета"))
        self.input_url.setPlaceholderText(_translate("DownloadScreen", "Унесите линк..."))
        self.input_author.setPlaceholderText(_translate("DownloadScreen", "Унесите аутора пјесме..."))
        self.input_name.setPlaceholderText(_translate("DownloadScreen", "Унесите име пјесме..."))
        self.btn_download.setText(_translate("DownloadScreen", "Скините пјесму на сервер"))
import res_rc
