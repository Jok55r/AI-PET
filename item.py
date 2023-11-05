import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QTextEdit, QMenu
from PyQt5.QtGui import QPixmap


window = None
layout = None
x = None
y = None

@staticmethod
def initialize(n_window, n_layout, n_x, n_y):
    global window, layout, x, y
    window = n_window
    layout = n_layout
    x = n_x
    y = n_y



def remove(widget):
    layout.removeWidget(widget)
    widget.deleteLater()


def add_button(x, y, size, text, function, color, textColor, fontSize):
    button = QPushButton(text, window)
    button.clicked.connect(function)

    button.setStyleSheet(f"background-color: {color}; color: {textColor}; font-size: {fontSize}px; ")
    button.setCursor(Qt.PointingHandCursor)
    button.setGeometry(x, y, size, size)

    layout.addWidget(button)
    
    return button


def add_image(offx, offy, fileName, function=None):
    image_label = QLabel(window)
    image = QPixmap(fileName)
    image_label.setPixmap(image)
    image_label.setScaledContents(True)
    image_label.setCursor(Qt.OpenHandCursor)

    image_label.setGeometry(int(offx/2), int(offy/4), x-offx, y-offy)

    if function is not None:
        image_label.setContextMenuPolicy(Qt.CustomContextMenu)
        image_label.customContextMenuRequested.connect(function)

    layout.addWidget(image_label)

    return image_label



def add_text(offx, offy, text, textColor, fontSize, height):
    label = QLabel(window)
    label.setText(text)
    label.setStyleSheet(f"color: {textColor}; font-size: {fontSize}px; background-color: rgba(0, 0, 0, 0.2); border: 3px solid black;")
    label.move(offx, offy)

    label.setWordWrap(True)
    label.setMinimumWidth(x - 2 * offx)
    label.setMinimumHeight(height)
    label.setAlignment(Qt.AlignTop | Qt.AlignLeft)

    layout.addWidget(label)

    return label


def add_scroll_text(offx, offy, text, textColor, fontSize, height):
    text_edit = QTextEdit(window)
    text_edit.setPlainText(text)
    text_edit.setStyleSheet(f"color: {textColor}; font-size: {fontSize}px; background-color: rgba(0, 0, 0, 0.2); border: 3px solid black;")
    text_edit.setGeometry(offx, offy, x - 2*offx, height)
    text_edit.setAlignment(Qt.AlignTop | Qt.AlignLeft)
    text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    text_edit.setReadOnly(True)
    text_edit.viewport().setCursor(Qt.ArrowCursor)

    layout.addWidget(text_edit)

    return text_edit


def add_input_field(size, function):
    input_field = QLineEdit(window)
    input_field.setStyleSheet(f"background-color: rgba(0, 0, 0, 0.2); color: white; font-size: 25px; border: none;") #border: 3px solid black;")

    input_field.setGeometry(0, y-size, x, size)

    input_field.returnPressed.connect(function)
    input_field.setText(">>")

    layout.addWidget(input_field)

    return input_field