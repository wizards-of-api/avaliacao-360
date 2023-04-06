import app
import PySimpleGUI as sg
import interface.login as interface_login  
sg.theme('DarkAmber')

col1 = [[sg.Text('Aluno: test')], [sg.Text('Turma: test')], [sg.Text('Grupo: test')], [sg.Text('')]]

layout = [[sg.Column(col1, justification='center', pad=(0, 10))], [sg.Button('Back'), sg.Button('Rate'), sg.Button('Cancel'), sg.Button('Result')]]

window = sg.Window('Avaliação360', layout, size=(230, 180))

def event_handler(event, values):
    if event == 'Cancel':
        app.close()
    elif event == 'Back':
        app.change_interface(interface_login)