import app
import PySimpleGUI as sg
import interface.login as interface_login
import interface.evaluation as interface_evaluation
import connection.student as connection_student
import connection.group as connection_group
import interface.dashboard_aluno as interface_dashboard_aluno

def create_window(name):

    global student_info, group_info, window, student_evaluation

    student_raw = connection_student.get_student_by_name(name)[0]
    student_info = connection_student.resolve_student(student_raw)
    student_evaluation = connection_student.check_student_todo_evaluation(student_info['id'])

    group_info = student_info['group']
    group_name = group_info['name']

    class_room_info = group_info['class-room']
    class_room_name = class_room_info['name']

    layout = [
        [sg.Text(f'Aluno: {name}')],
        [sg.Text(f'Grupo: {group_name}')],
        [sg.Text(f'Sala: {class_room_name}')],
        [sg.Text('\n')],
        [sg.Button('Voltar'), sg.Button('Cancelar'), sg.Button('Resultados')]
    ]     
    if student_evaluation:
        layout[4].insert(1, sg.Button('Avaliação'))
    else:
        layout[4].insert(1, sg.Button('Avaliação', disabled=True, button_color=('white', 'grey')))
    window = sg.Window('Avaliação 360 - Aluno', layout, element_justification='c', resizable = True)
    return window

def event_handler(event, _):
    global student_info
    if event == 'Cancelar':
        app.close()
    elif event == 'Voltar':
        app.change_interface(interface_login.create_window(), interface_login.event_handler)
   
    elif event == 'Avaliação':
    #seleciona um grupo para realizar avaliacao
        student_list = connection_group.get_group_student_list(group_info['id'])
        interface_evaluation.create_evaluation(student_info['id'], student_list)
    elif event =='Resultados':
        app.change_interface(interface_dashboard_aluno.create_window(student_info['name']), interface_dashboard_aluno.event_handler)
