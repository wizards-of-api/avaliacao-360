import app
import PySimpleGUI as sg
import interface.login as interface_login

def create_window():
    col1 = [[sg.Text('Aluno: test')], [sg.Text('Turma: test')], [sg.Text('Grupo: test')], [sg.Text('\n')]]
    col2 = [[sg.Button('Voltar'), sg.Button('Avaliação'), sg.Button('Cancelar'), sg.Button('Resultados')]]


    layout = [
        [sg.Column(col1, justification='center', pad=(0, 10))],
        [sg.Column(col2, justification='center')]
    ]        

    window = sg.Window('Avaliação360', layout, resizable=True, size=(400, 180))

    return window

def event_handler(event, _):
    if event == 'Cancelar':
        app.close()
    elif event == 'Voltar':
        app.change_interface(interface_login.create_window(), interface_login.event_handler)