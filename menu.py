import item

isToggled = False
global settings_button

def toggle_menu():
    global isToggled
    global settings_button

    isToggled = not isToggled

    if isToggled:
        settings_button = item.add_button(50, 50, 30, '☼', useless, 'black', 'white', 15)
        print('enable')
    else:
        item.remove(settings_button)
        print('disable')


def useless():
    settings_button = item.add_button(0, 0, 30, '☼', useless, 'black', 'white', 15)