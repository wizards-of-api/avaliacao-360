import PySimpleGUI as sg

import gui_exemples.home as gui_home
import gui_exemples.login as gui_login

current_gui = gui_home
current_window = current_gui.window

while True:
    current_window = current_gui.window
    event, values = current_window.read()

    event_response = current_gui.event_handler(event, values)
    if event_response:
        if event == sg.WIN_CLOSED or event_response[0] == 'close':
            break

        elif event_response[0] == 'change_window':
            current_window.close()
            if event_response[1] == 'login':
                current_gui = gui_login

current_window.close()