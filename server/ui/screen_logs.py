# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_logs.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LogScreen(object):
    def setupUi(self, LogScreen):
        LogScreen.setObjectName("LogScreen")
        LogScreen.resize(700, 560)
        self.centralwidget = QtWidgets.QWidget(LogScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_border = QtWidgets.QFrame(self.centralwidget)
        self.frame_border.setGeometry(QtCore.QRect(0, 0, 700, 560))
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
        self.frame.setGeometry(QtCore.QRect(10, 10, 680, 540))
        self.frame.setStyleSheet("QFrame {    \n"
"    background-color: rgba(18, 18, 18, 225);    \n"
"}\n"
"QLabel {\n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(0, 0, 680, 540))
        self.widget.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"}")
        self.widget.setObjectName("widget")
        self.btn_back = QtWidgets.QPushButton(self.widget)
        self.btn_back.setGeometry(QtCore.QRect(630, 490, 41, 41))
        self.btn_back.setStyleSheet("QPushButton#btn_back {\n"
"    border-image: url(:/images/images/back.png);\n"
"}\n"
"QPushButton#btn_back:hover {\n"
"    border-image: url(:/images/images/hover_back.png);\n"
"}")
        self.btn_back.setText("")
        self.btn_back.setObjectName("btn_back")
        self.log = QtWidgets.QPlainTextEdit(self.widget)
        self.log.setGeometry(QtCore.QRect(0, 0, 620, 540))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.log.setFont(font)
        self.log.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: rgb(224,224,226);\n"
"border: none;")
        self.log.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.log.setPlainText("")
        self.log.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.log.setObjectName("log")
        self.log.raise_()
        self.btn_back.raise_()
        LogScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(LogScreen)
        QtCore.QMetaObject.connectSlotsByName(LogScreen)

    def retranslateUi(self, LogScreen):
        _translate = QtCore.QCoreApplication.translate
        LogScreen.setWindowTitle(_translate("LogScreen", "MainWindow"))
import res_rc
