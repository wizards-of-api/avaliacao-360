import PySimpleGUI as sg
import interface.home as inteface_home

current_interface = inteface_home
to_close = False
is_running = False

def close():
    global to_close
    to_close = True

def change_interface(new_interface):
    global current_interface
    current_interface = new_interface

def run():
    global to_close, current_interface, is_running

    if is_running:
        raise Exception('App already running')
    is_running = True

    while True:
        current_window = current_interface.window
        event, values = current_window.read()

        current_interface.event_handler(event, values)
        if event == sg.WIN_CLOSED or to_close:
            break

    current_window.close()