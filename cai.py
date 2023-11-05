import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QLineEdit
from characterai import PyCAI


file_path = 'Secret.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()
    client = PyCAI(lines[0][:-1])
    char = lines[1][:-1]

print('READY TO GO!')

chat = client.chat.get_chat(char)
participants = chat['participants']

if not participants[0]['is_human']:
    tgt = participants[0]['user']['username']
else:
    tgt = participants[1]['user']['username']

def new_chat():
    chat = client.chat.new_chat(char)

def on_message(msg):
    data = client.chat.send_message(chat["external_id"], tgt, msg)

    try:
        text = data["replies"][0]["text"]
    except:
        text = "filtered"

    return text