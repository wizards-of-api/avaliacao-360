import app
import PySimpleGUI as sg
import interface.login as interface_login  

def create_window():
    layout = [[sg.Text('Bem-vindo!')],
        [sg.Button('Login'), sg.Button('Cancel')]]
    return sg.Window('Window Title', layout)

def event_handler(event, _):
    if event == 'Cancel':
        app.close()
    elif event == 'Login':
        app.change_interface(interface_login.create_window(), interface_login.event_handler)