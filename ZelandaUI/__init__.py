import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class UI:
    def __init__(self):
        pass

    def window_ui(self):
        app = QApplication(sys.argv)
        w = QWidget()
        b = QLabel(w)
        b.setText("Hello World!")
        w.setGeometry(100,100,200,50)
        b.move(50,20)
        w.setWindowTitle("PyQt5")
        w.show()
        sys.exit(app.exec_())