import pyttsx3
import time


with open('settings.txt', 'r') as file:
    enabled = file.readlines()[1][:-1] == 'Y'

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    if enabled:
        target=engine.runAndWait()
    else:
        time.sleep(len(text)/15)