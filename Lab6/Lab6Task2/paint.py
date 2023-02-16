import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class drawingFrame(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.drawing = []
        self.isDrawing = False

    
    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.isDrawing = True
        print("click")

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.isDrawing = False
    
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.isDrawing:
            self.drawing.append(QPoint(event.pos().x(), event.pos().y()))
            self.repaint()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QColor(255, 0, 0))
        painter.setBrush(QColor(255, 0, 0))

        for point in self.drawing:
            painter.drawEllipse(point, 5, 5)
            
        

class paintWindow(QWidget):
    def __init__(self):
        super().__init__(None)
        self.setWindowTitle("A Simple Paint Program")
        self.paintArea = drawingFrame(self)

        self.paintArea.setMinimumSize(600, 400)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.paintArea)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.clearButton)

        self.setLayout(self.layout)



def main():
    app = QApplication(sys.argv)
    window = paintWindow()
    window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
