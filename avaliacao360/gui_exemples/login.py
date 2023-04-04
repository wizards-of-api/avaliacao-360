import PySimpleGUI as sg
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Login!')],
        [sg.Text('User: '), sg.InputText()],
        [sg.Text('Password: '), sg.InputText()],
        [sg.Button('Login'), sg.Button('Cancel')]
        ]

# Create the Window
window = sg.Window('Window Title', layout)

def event_handler(event, values):
    if event == 'Cancel': # if user closes window or clicks cancel
        return ['close']