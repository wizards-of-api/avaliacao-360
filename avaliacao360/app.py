import PySimpleGUI as sg
from datetime import date
from utils.sprint_handler import check_sprint_all
sg.theme('DarkAmber') 

to_close = False
is_running = False
fix_date = None

def pop_up_success(msg):
    layout = [[sg.Text(msg)], [sg.Button('Ok')]]
    window = sg.Window('Avaliação 360 - Sucesso', layout, element_justification='c')
    window.read()
    window.close()

def set_date(date):
    global fix_date
    fix_date = date

def pop_up_advice(msg):
    #global window
    #window.close()

    layout = [[sg.Text(msg)], [sg.Button('Ok')]]
    error_window = sg.Window('Avaliação 360 - Aviso', layout, element_justification='c')
    error_window.read()
    error_window.close()


def close():
    global to_close
    to_close = True

def change_interface(new_window, new_event_handler=None):
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
