from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import QPropertyAnimation
from random import randint, choice

class Effect():
    """
    DOCSTRING:

    """
    def __init__(self, widget, username, image):
        super(Effect, self).__init__()
        self.widget = widget
        self.username = username
        self.image = image
        self.x = 180
        self.y = 420
        self.width = 110
        self.height = 110
        self.visible = False
        self.timer = None

        self.create_effect()
        self.show()
        self.start_effect()

    def create_effect(self):
        self.effect = QtWidgets.QLabel(self.widget)
        self.effect.setGeometry(QtCore.QRect(self.x, self.y, self.width, self.height))
        self.effect.setStyleSheet("")
        self.effect.setText("")
        self.effect.setObjectName("effect")
        self.pixmap_body = QPixmap(self.image)
        self.pixmap_body = self.pixmap_body.scaled(self.width, self.height, QtCore.Qt.KeepAspectRatio)
        self.effect.setPixmap(self.pixmap_body)
        
    def show(self):
        if self.visible:
            return False

        self.visible = True
        self.effect.show()

    def hide(self):
        if not self.visible:
            return False

        self.visible = False
        self.effect.hide()

    def start_effect(self):
        self.moving = choice([0, 1, 2])
        self.anim_time = 100

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.animation)
        self.timer.start(self.anim_time)

    def animation(self):
        move_x = [randint(-6, -1), randint(-3, 3), randint(1, 6)][self.moving]

        self.anim = QPropertyAnimation(self.effect, b"geometry")
        self.anim.setDuration(self.anim_time)
        self.anim.setStartValue(QtCore.QRect(self.x, self.y, self.width, self.height))
        self.anim.setEndValue(QtCore.QRect(self.x + move_x, self.y - 10, self.width, self.height))
        self.anim.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.anim.start()

        self.x += move_x
        self.y -= 10

        if (self.y + self.height) < 0:
            self.timer.stop()
