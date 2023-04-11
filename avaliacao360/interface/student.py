import app
import PySimpleGUI as sg
import interface.login as interface_login

def create_window():
    col1 = [[sg.Text('Aluno: test')], [sg.Text('Turma: test')], [sg.Text('Grupo: test')], [sg.Text('\n')]]

    layout = [[sg.Column(col1, justification='center', pad=(0, 10))], [sg.Button('Voltar'), sg.Button('Avaliação'), sg.Button('Cancelar'), sg.Button('Resultados')]]

    window = sg.Window('Avaliação360', layout, size=(300, 180))

    return window

def event_handler(event, _):
    if event == 'Cancelar':
        app.close()
    elif event == 'Voltar':
        app.change_interface(interface_login.create_window(), interface_login.event_handler)