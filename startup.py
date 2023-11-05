from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout


def CreateApp(x, y):
    window = QMainWindow()
    window.setGeometry(200, 200, x, y)
    window.setWindowFlag(Qt.FramelessWindowHint)
    window.setAttribute(Qt.WA_TranslucentBackground)
    window.setWindowFlag(Qt.WindowStaysOnTopHint)
    return window

def CreateLayout(): 
    layout = QVBoxLayout()
    return layout


class DraggableWindow(QMainWindow):
    def __init__(self, x, y):
        super().__init__()

        self.setGeometry(200, 200, x, y)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.globalPos() - self.frameGeometry().topLeft()
        event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            new_position = event.globalPos() - self.drag_start_position
            self.move(new_position)

        event.accept()