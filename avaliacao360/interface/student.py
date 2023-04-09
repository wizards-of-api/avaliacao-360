import app
import PySimpleGUI as sg
import interface.login as interface_login

def create_window():
    layout = [ [sg.Text('Aluno')], [sg.Button('Back'), sg.Button('Cancel')]]
    return sg.Window('Avaliação360', layout)

def event_handler(event, _):
    if event == 'Cancel': # if user closes window or clicks cancel
        app.close()
    elif event == 'Back':
        app.change_interface(interface_login.create_window(), interface_login.event_handler)