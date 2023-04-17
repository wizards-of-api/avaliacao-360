import app
import PySimpleGUI as sg
import interface.login as interface_login
import interface.evaluation as interface_evaluation
import connection.student as connection_student
import connection.group as connection_group

def create_window(name):

    global student_info, group_info

    student_raw = connection_student.get_student_by_name(name)[0]
    student_info = connection_student.resolve_student(student_raw)

    group_info = student_info['group']
    group_name = group_info['name']

    class_room_info = group_info['class-room']
    class_room_name = class_room_info['name']

    col1 = [[sg.Text(f'Aluno: {name}')], [sg.Text(f'Turma: { group_name}')], [sg.Text(f'Grupo: {class_room_name}')], [sg.Text('\n')]]
    col2 = [[sg.Button('Voltar'), sg.Button('Avaliação'), sg.Button('Cancelar'), sg.Button('Resultados')]]

    layout = [
        [sg.Column(col1, justification='center', pad=(0, 10))],
        [sg.Column(col2, justification='center')]
    ]        

    window = sg.Window('Avaliação 360 - Aluno', layout)

    return window

def event_handler(event, _):
    if event == 'Cancelar':
        app.close()
    elif event == 'Voltar':
        app.change_interface(interface_login.create_window(), interface_login.event_handler)
    elif event == 'Avaliação':
        #seleciona um grupo para realizar avaliacao
        student_list = connection_group.get_group_student_list(group_info['id'])
        interface_evaluation.create_evaluation(student_info['id'], student_list)