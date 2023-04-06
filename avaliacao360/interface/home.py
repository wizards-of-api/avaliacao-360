import app
import PySimpleGUI as sg
import interface.login as interface_login  

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Bem-vindo!')],
        [sg.Button('Login'), sg.Button('Cancel')],
        ]

# Create the Window
window = sg.Window('Window Title', layout)

def event_handler(event, values):
    if event == 'Cancel': # if user closes window or clicks cancel
        app.close()
    elif event == 'Login':
        app.change_interface(interface_login)