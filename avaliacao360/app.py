import PySimpleGUI as sg
sg.theme('DarkAmber') 

to_close = False
is_running = False

def pop_up(msg):
    layout = [[sg.Text(msg)], [sg.Button('Ok')]]
    window = sg.Window('Avaliação 360', layout)
    window.read()
    window.close()

def error(msg):
    global window
    window.close()

    layout = [[sg.Text(msg)], [sg.Button('Close')]]
    err_window = sg.Window('Avaliação 360 - ERROR', layout)
    err_window.read()
    err_window.close()


def close():
    global to_close
    to_close = True

def change_interface(new_window, new_event_handler):
    global window, event_handler

    if 'window' in globals():
        window.close()

    window = new_window
    event_handler = new_event_handler

def run():
    global window, event_handler, to_close, is_running

    if is_running:
        raise Exception('App already running')
    is_running = True

    while True:
        event, values = window.read()

        event_handler(event, values)
        if event == sg.WIN_CLOSED or to_close:
            break

    window.close()