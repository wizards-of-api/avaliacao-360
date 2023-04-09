import app
import PySimpleGUI as sg
import interface.login as interface_login  

def create_window():
    layout = [[sg.Text('Administrador')], [sg.Button('Back'), sg.Button('Cancel')]]
    return sg.Window('Window Title', layout)

def event_handler(event, _):
  if event == 'Cancel':
    app.close()
  elif event == 'Back':
    app.change_interface(interface_login.create_window(), interface_login.event_handler)

