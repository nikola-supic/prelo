from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QTransform

class Character():
    """
    DOCSTRING:

    """
    def __init__(self, widget, name, pos, size, body, head, arms):
        super(Character, self).__init__()
        self.widget = widget
        self.name = name
        self.x, self.y = pos
        self.width, self.height = size
        self.body = body
        self.head = head
        self.arms = arms
        
        self.counter_head = 0
        self.counter_arms = 0
        self.timer_head = None
        self.timer_arms = None
        self.visible = False

        self.create_character()
        self.create_name()

        # self.check_head_animation()
        # self.check_arms_animation()

    def create_character(self):
        self.char_body = QtWidgets.QLabel(self.widget)
        self.char_body.setGeometry(QtCore.QRect(self.x, self.y, self.width, self.height))
        self.char_body.setStyleSheet("")
        self.char_body.setText("")
        self.char_body.setObjectName("char_body")
        self.pixmap_body = QPixmap(self.body)
        self.char_body.setPixmap(self.pixmap_body)

        self.char_head = QtWidgets.QLabel(self.widget)
        self.char_head.setGeometry(QtCore.QRect(self.x-4, self.y-6, self.width, self.height))
        self.char_head.setStyleSheet("")
        self.char_head.setText("")
        self.char_head.setObjectName("char_head")
        self.pixmap_head = QPixmap(self.head)
        self.char_head.setPixmap(self.pixmap_head)

        self.char_arms = QtWidgets.QLabel(self.widget)
        self.char_arms.setGeometry(QtCore.QRect(self.x-4, self.y-2, self.width, self.height))
        self.char_arms.setStyleSheet("")
        self.char_arms.setText("")
        self.char_arms.setObjectName("char_arms")
        self.pixmap_arms = QPixmap(self.arms)
        self.char_arms.setPixmap(self.pixmap_arms)
        
    def create_name(self):
        self.char_name = QtWidgets.QLabel(self.widget)
        self.char_name.setGeometry(QtCore.QRect(self.x - 20, self.y + 200, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.char_name.setFont(font)
        self.char_name.setStyleSheet("color: rgb(224,224,226);")
        self.char_name.setAlignment(QtCore.Qt.AlignCenter)
        self.char_name.setObjectName("char_name")
        self.char_name.setText(self.name)

    def show(self):
        if self.visible:
            return False

        self.visible = True
        self.char_body.show()
        self.char_head.show() 
        self.char_arms.show()
        self.char_name.show()

    def hide(self):
        if not self.visible:
            return False

        self.visible = False
        self.char_body.hide()
        self.char_head.hide() 
        self.char_arms.hide()
        self.char_name.hide()

    def start_head_anim(self):
        if self.timer_head is None:
            self.timer_head = QtCore.QTimer()
            self.timer_head.timeout.connect(self.head_animation)
            self.timer_head.start(750)

    def stop_head_anim(self):
        if self.timer_head is not None:
            self.timer_head.stop()
            self.timer_head = None

    def head_animation(self):
        self.counter_head += 1
        if self.counter_head % 2 == 0:
            angle = 1
        else:
            angle = -9

        pixmap_rotated = self.pixmap_head.transformed(QTransform().rotate(angle), QtCore.Qt.SmoothTransformation)
        self.char_head.setPixmap(pixmap_rotated)
    
    def start_arms_anim(self):
        if self.timer_arms is None:
            self.timer_arms = QtCore.QTimer()
            self.timer_arms.timeout.connect(self.arms_animation)
            self.timer_arms.start(750)

    def stop_arms_anim(self):
        if self.timer_arms is not None:
            self.timer_arms.stop()
            self.timer_arms = None

    def arms_animation(self):
        self.counter_arms += 1
        if self.counter_arms % 2 == 0:
            angle = 1
        else:
            angle = -3

        pixmap_rotated = self.pixmap_arms.transformed(QTransform().rotate(angle), QtCore.Qt.SmoothTransformation)
        self.char_arms.setPixmap(pixmap_rotated)