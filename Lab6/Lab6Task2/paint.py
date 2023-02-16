import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class paintWindow(QWidget):
    def __init__(self):
        super().__init__(None)
        self.setWindowTitle("A Simple Paint Program")
        paintArea = QFrame(self)
        instruction = QLabel("Drag the mouse to draw")
        clearButton = QPushButton("Clear")