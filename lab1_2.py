import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle('Simple Drawing')
        self.snowman = QPixmap('images/snowman.png')

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.drawPixmap(QRect(200, 100, 320, 320), self.snowman)
        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window1()
    w.show()

    return app.exec()

if __name__ == '__main__':
    sys.exit(main())