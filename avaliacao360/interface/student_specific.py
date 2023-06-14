import app
import PySimpleGUI as sg
import connection.student as connection_student
import connection.group as connection_group
import interface.student_general as interface_student_general
import interface.evaluation as interface_evaluation
import interface.dashboard_specific_student as interface_dashboard_specific_student
from config import LABEL_FONT

def create_window(student_id, room_id):

    global student_info, group_info, window, student_evaluation

    student_raw = connection_student.get_student_by_id(student_id)
    student_info = connection_student.resolve_student(student_raw)
    student_name = student_info['name']

    group_info = [group for group in student_info['group-list'] if group['class-room']['id'] == room_id][0]
    group_name = group_info['name']
    student_evaluation = connection_student.get_student_todo_evaluation(student_id, group_info['id'])

    class_room_info = group_info['class-room']
    class_room_name = class_room_info['name']

    layout = [
        [sg.Text(f'Aluno: {student_name}', font=LABEL_FONT)],
        [sg.Text(f'Grupo: {group_name}', font=LABEL_FONT)],
        [sg.Text(f'Sala: {class_room_name}', font=LABEL_FONT)],
        [sg.Text('\n')],
        [sg.Button('Voltar', font=LABEL_FONT), sg.Button('Resultados', font=LABEL_FONT)]
    ]     
    if student_evaluation:
        layout[4].insert(1, sg.Button('Avaliação', font=LABEL_FONT))
    else:
        layout[4].insert(1, sg.Button('Avaliação', disabled=True, button_color=('white', 'grey'), font=LABEL_FONT))
    return sg.Window('Avaliação 360 - Aluno', layout, element_justification='c')

def event_handler(event, _):
    global student_info, group_info, student_evaluation
    if event == 'Voltar':
        app.change_interface(interface_student_general.create_window(student_info['id']), interface_student_general.event_handler)
   
    elif event == 'Avaliação':
    #seleciona um grupo para realizar avaliacao
        student_list = connection_group.get_group_student_list(group_info['id'])
        interface_evaluation.create_evaluation(student_info['id'], student_evaluation)
    elif event == 'Resultados':
        app.change_interface(interface_dashboard_specific_student.create_window(student_info['id'], group_info['id'], 0), interface_dashboard_specific_student.event_handler)