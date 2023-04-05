import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Login!')],
        [sg.Text('User: '), sg.InputText(key='-INPUT-')],
        [sg.Text('Password: '), sg.InputText()],
        [sg.Button('Login'), sg.Button('Cancel')]
        ]

# Create the Window
window = sg.Window('Avaliação 360', layout)

def event_handler(event, values):
    if event == 'Cancel': # if user closes window or clicks cancel
        return ['close']
    if event == 'Login':
        valor = values['-INPUT-']
        if valor == 'aluno':
            return ['change_window', 'student_interface']
        elif valor =='admin':
            return ['change_window', 'adm_interface']
