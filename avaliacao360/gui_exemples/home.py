import PySimpleGUI as sg
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Bem-vindo!')],
        [sg.Button('Login'), sg.Button('Cancel')],
        ]

# Create the Window
window = sg.Window('Window Title', layout)

def event_handler(event, values):
    if event == 'Cancel': # if user closes window or clicks cancel
        return ['close']
    elif event == 'Login':
        return ['change_window', 'login']