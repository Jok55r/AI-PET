import threading
import speech
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap

global txt, img, input_field, cai, fileName

def execute_steps():
    global txt, img, input_field, cai, fileName
    out = cai.on_message(input_field.text())
    txt.setText(out)
    input_field.setText(">>")
    yield
    img.setPixmap(QPixmap(f"Resources\\{fileName}_talking.jpg"))
    yield
    t = threading.Thread(target=speech.speak(out), daemon=True)
    t.start()
    yield
    img.setPixmap(QPixmap(f"Resources\\{fileName}_idle.jpg"))

def thread():
    global txt, img, input_field, cai, fileName
    step_generator = execute_steps()

    def next_step():
        try:
            next(step_generator)
            QTimer.singleShot(0, next_step)
        except StopIteration:
            pass

    next_step()

def on_enter(ntxt, nimg, ninput_field, ncai, nfileName):
    global txt, img, input_field, cai, fileName
    txt = ntxt
    img = nimg
    input_field = ninput_field
    cai = ncai
    fileName = nfileName

    t = threading.Thread(target=thread())
    t.start()