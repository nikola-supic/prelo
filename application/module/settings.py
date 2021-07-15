# Importing the libraries
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup
from ui.screen_settings import Ui_SettingsScreen
from datetime import datetime, date

import database as db
from module.popup import PopupWarning

# SETTINGS SCREEN
class SettingsScreen(QMainWindow, Ui_SettingsScreen):
    def __init__(self, last_screen):
        super(SettingsScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.user = last_screen.user
        self.network = last_screen.network
        self.stacked_pages.setCurrentWidget(self.page_info)
        self.update_user()

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_back.clicked.connect(self.exit)
        self.btn_page_info.clicked.connect(lambda: self.stacked_pages.setCurrentWidget(self.page_info))
        self.btn_page_acc.clicked.connect(lambda: self.stacked_pages.setCurrentWidget(self.page_acc))
        self.btn_page_security.clicked.connect(lambda: self.stacked_pages.setCurrentWidget(self.page_security))
        
        self.btn_acc_save.clicked.connect(self.save_acc)
        self.btn_security_save.clicked.connect(self.save_security)

        self.click_time = get_time() + 1

        self.show()


    def save_acc(self):
        first_name = self.input_first.text()
        last_name = self.input_last.text()
        username = self.input_username.text()

        try:
            day = int(self.input_day.text())
            month = int(self.input_month.text())
            year = int(self.input_year.text())
        except ValueError:
            day = False
            month = False
            year = False


        if len(first_name) >= 4:
            self.user.first_name = first_name
            self.user.update_sql('first_name', first_name)
        elif first_name:
            self.popup = PopupWarning(self, 'Ваше име мора имати најмање 4 карактера.', 'Погреашна лозинка.')
            self.close()

        if len(last_name) >= 4:
            self.user.last_name = last_name
            self.user.update_sql('last_name', last_name)
        elif last_name:
            self.popup = PopupWarning(self, 'Ваше презиме мора имати најмање 4 карактера.', 'Погреашна лозинка.')
            self.close()

        if len(username) >= 4:
            self.user.username = username
            self.user.update_sql('username', username)
        elif username:
            self.popup = PopupWarning(self, 'Ваше корисничко име мора имати најмање 4 карактера.', 'Погреашна лозинка.')
            self.close()

        if all([day, month, year]):
            try:
                birthday = date(year, month, day)
                self.user.birthday = birthday
                self.user.update_sql('birthday', birthday)

            except TypeError:
                self.popup = PopupWarning(self, 'Дан, мјесец или годину сте унијели погрешно.', 'Неуспјешна промјена датума рођења.')
                self.close()

        self.update_user()
        self.input_first.setText('')
        self.input_last.setText('')
        self.input_username.setText('')
        self.input_day.setText('')
        self.input_month.setText('')
        self.input_year.setText('')


    def save_security(self):
        password = self.input_pw.text()
        confirm_pw = self.input_pw_2.text()
        email = self.input_email.text()

        if len(password) >= 8 and len(password) <= 48 and (password == confirm_pw):
            self.user.password = password
            self.user.update_sql('password', password)
        elif password:
            self.popup = PopupWarning(self, 'Ваша лозинка мора имати између 8 и 48 карактера.', 'Погреашна лозинка.')
            self.close()

        if len(email) >= 8:
            self.user.email = email
            self.user.update_sql('email', email)
        elif email:
            self.popup = PopupWarning(self, 'Ваш мејл мора имати најмање 8 карактера.', 'Погреашан мејл.')
            self.close()

        self.update_user()
        self.input_pw.setText('')
        self.input_pw_2.setText('')
        self.input_email.setText('')


    def update_user(self):
        name = db.get_name(self.user.id)
        username = db.get_username(self.user.id)
        self.label_name.setText(name)
        self.label_user.setText(username)

        if self.user.admin:
            admin = 'ДА'
        else:
            admin = 'НЕ'

        self.info.setPlainText(f'Рођендан: {self.user.birthday:%d.%m.%Y.}\nВаш мејл: {self.user.email}\nАдмин: {admin}\nДатум регистрације: {self.user.register_date:%d.%m.%Y. %H:%M:%S}')


    def exit(self):
        self.back.show()
        self.close()


def get_time():
    return datetime.now().timestamp()