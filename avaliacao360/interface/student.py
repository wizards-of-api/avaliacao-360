import app
import PySimpleGUI as sg
import interface.login as interface_login
import interface.evaluation as interface_evaluation
import connection.group as connection_group
import connection.class_room as connection_class_room
import connection.student as connection_student

def create_window(name):
    student_info = connection_student.get_student_by_name(name)
    global group_id
    group_id = student_info[0]['group-id']
    group_info = connection_group.get_group_by_id(group_id)
    group_name = group_info['name']
    class_room_id = group_info['class-room-id']
    class_room_information = connection_class_room.get_class_room_by_id(class_room_id)
    class_room_name = class_room_information['name']

    col1 = [[sg.Text(f'Aluno: {name}')], [sg.Text(f'Turma: { group_name}')], [sg.Text(f'Grupo: {class_room_name}')], [sg.Text('\n')]]
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
        student_list = connection_group.get_group_student_list(group_id)
        interface_evaluation.create_evaluation(student_list)