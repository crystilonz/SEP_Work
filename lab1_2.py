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

class Simple_drawing_window3(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle('Simple Drawing')
        self.ant = QPixmap('images/ant.png')

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor("red"))
        p.drawRect(100,100,50,50)

        p.drawPixmap(QRect(200, 100, 320, 320), self.ant)
        p.end()
def main():
    app = QApplication(sys.argv)

    w1 = Simple_drawing_window1()
    w3 = Simple_drawing_window3()

    w1.show()
    w3.show()

    return app.exec()

if __name__ == '__main__':
    sys.exit(main())