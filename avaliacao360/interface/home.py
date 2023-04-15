import app
import PySimpleGUI as sg
import interface.login as interface_login  

def create_window():
    layout = [[sg.Text('Bem-vindo!')],
        [sg.Button('Login'), sg.Button('Cancelar')]]
    return sg.Window('Avaliação 360', layout, element_justification = 'c')

def event_handler(event, _):
    if event == 'Cancelar':
        app.close()
    elif event == 'Login':
        app.change_interface(interface_login.create_window(), interface_login.event_handler)