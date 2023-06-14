import PySimpleGUI as sg
from datetime import date
from utils.sprint_handler import check_sprint_all
from config import TITLE_FONT, LABEL_FONT
sg.theme('DarkAmber')

to_close = False
is_running = False
fix_date = None

def pop_up(msg):
    layout = [[sg.Text(msg, font=LABEL_FONT)], [sg.Button('Ok', font=LABEL_FONT)]]
    window = sg.Window('Avaliação 360', layout)
    window.read()
    window.close()

def set_date(date):
    global fix_date
    fix_date = date

def error(msg):
    global window
    window.close()

    layout = [[sg.Text(msg, font=LABEL_FONT)], [sg.Button('Close', font=LABEL_FONT)]]
    err_window = sg.Window('Avaliação 360 - ERROR', layout)
    err_window.read()
    err_window.close()


def close():
    global to_close
    to_close = True

def change_interface(new_window: sg.Window, new_event_handler=None):
    global window, event_handler, fix_date
    date_now = fix_date

    if not date_now:
        date_now = date.today()

    print('Today: ', date_now)

    check_sprint_all(date_now)

    if 'window' in globals():
        window.close()

    window = new_window
    event_handler = new_event_handler

def run():
    global window, event_handler, to_close, is_running

    if is_running:
        raise RuntimeError('Application is already running')

    is_running = True

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        
        if event_handler:
            event_handler(event, values)
        
        if  to_close:
            break


    window.close()
