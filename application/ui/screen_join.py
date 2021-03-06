# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_join.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JoinScreen(object):
    def setupUi(self, JoinScreen):
        JoinScreen.setObjectName("JoinScreen")
        JoinScreen.resize(490, 220)
        self.centralwidget = QtWidgets.QWidget(JoinScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_border = QtWidgets.QFrame(self.centralwidget)
        self.frame_border.setGeometry(QtCore.QRect(0, 0, 490, 220))
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
        self.frame.setGeometry(QtCore.QRect(10, 10, 470, 200))
        self.frame.setStyleSheet("QLabel {\n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(0, 0, 471, 201))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.label_title = QtWidgets.QLabel(self.widget)
        self.label_title.setGeometry(QtCore.QRect(139, 0, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(42)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(20, 92, 158);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.input_host = QtWidgets.QLineEdit(self.widget)
        self.input_host.setGeometry(QtCore.QRect(130, 80, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.input_host.setFont(font)
        self.input_host.setStyleSheet("QLineEdit {\n"
"    background-color: rgba(0,0,0,0);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(20, 92, 158);\n"
"    color: rgb(224, 224, 226);\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"")
        self.input_host.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_host.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_host.setClearButtonEnabled(True)
        self.input_host.setObjectName("input_host")
        self.btn_join = QtWidgets.QPushButton(self.widget)
        self.btn_join.setGeometry(QtCore.QRect(350, 130, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_join.setFont(font)
        self.btn_join.setStyleSheet("QPushButton#btn_join {\n"
"    border-radius: 5px;\n"
"    border-image: url(:/icons/images/icons/join.png);\n"
"}\n"
"QPushButton#btn_join:hover {\n"
"    border-image: url(:/icons/images/icons/hover_join.png);\n"
"}")
        self.btn_join.setText("")
        self.btn_join.setObjectName("btn_join")
        self.input_port = QtWidgets.QLineEdit(self.widget)
        self.input_port.setGeometry(QtCore.QRect(130, 130, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.input_port.setFont(font)
        self.input_port.setStyleSheet("QLineEdit {\n"
"    background-color: rgba(0,0,0,0);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(20, 92, 158);\n"
"    color: rgb(224, 224, 226);\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"")
        self.input_port.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_port.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_port.setClearButtonEnabled(True)
        self.input_port.setObjectName("input_port")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(205, 40, 115, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(224,224,226);")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        JoinScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(JoinScreen)
        QtCore.QMetaObject.connectSlotsByName(JoinScreen)

    def retranslateUi(self, JoinScreen):
        _translate = QtCore.QCoreApplication.translate
        JoinScreen.setWindowTitle(_translate("JoinScreen", "MainWindow"))
        self.label_title.setText(_translate("JoinScreen", "??????????"))
        self.input_host.setPlaceholderText(_translate("JoinScreen", "????????"))
        self.input_port.setPlaceholderText(_translate("JoinScreen", "????????"))
        self.label.setText(_translate("JoinScreen", "?????????? ??????????????"))
import res_rc
