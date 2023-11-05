import sys
import threading
import startup
import item 
import cai
import enter_handler
import menu
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap

x = 400
y = 400


cai.new_chat()
app = QApplication(sys.argv)
window = startup.DraggableWindow(x, y)  
layout = startup.CreateLayout()

item.initialize(window, layout, x, y)


def exit_app():
    app.quit()

def on_enter():
    enter_handler.on_enter(txt, img, input_field, cai, fileName)


with open('settings.txt', 'r') as file:
    fileName = file.readlines()[0][:-1]


img = item.add_image(200, 200, f"Resources\\{fileName}_idle.jpg", menu.toggle_menu)
exit_button = item.add_button(x-85, 0, 40, 'X', exit_app, 'rgba(0, 0, 0, 0.01)', 'white', 25)
txt = item.add_scroll_text(20, 250, '', 'white', 18, 120)
input_field = item.add_input_field(30, on_enter)


window.show()

sys.exit(app.exec_())