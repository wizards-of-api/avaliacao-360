import app
import PySimpleGUI as sg
import interface.login as interface_login
import interface.evaluation as interface_evaluation
import connection.group as connection_group

def create_window():
    col1 = [[sg.Text('Aluno: test')], [sg.Text('Turma: test')], [sg.Text('Grupo: test')], [sg.Text('\n')]]
    col2 = [[sg.Button('Voltar'), sg.Button('Avaliação'), sg.Button('Cancelar'), sg.Button('Resultados')]]


    layout = [
        [sg.Column(col1, justification='center', pad=(0, 10))],
        [sg.Column(col2, justification='center')]
    ]        

    window = sg.Window('Avaliação360', layout)

    return window

def event_handler(event, _):
    if event == 'Cancelar':
        app.close()
    elif event == 'Voltar':
        app.change_interface(interface_login.create_window(), interface_login.event_handler)
    elif event == 'Avaliação':
        #seleciona um grupo para realizar avaliacao
        student_list = []
        student_list = connection_group.get_group_student_list(1)
        interface_evaluation.create_evaluation(student_list)