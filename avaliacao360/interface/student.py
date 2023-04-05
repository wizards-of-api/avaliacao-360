import app
import PySimpleGUI as sg
import interface.login as interface_login  
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [ [sg.Text('Aluno')], [sg.Button('Back'), sg.Button('Cancel')]]
# Create the Window
window = sg.Window('Avaliação360', layout)

def event_handler(event, values):
    if event == 'Cancel': # if user closes window or clicks cancel
        app.close()
    elif event == 'Back':
        app.change_interface(interface_login)