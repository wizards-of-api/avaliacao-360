import app
import PySimpleGUI as sg
import interface.login as interface_login
import connection.student as connection_student
import interface.student_specific as interface_student_specific

def create_window(student_id):
    global student_info, group_info, window, student_evaluation

    student_raw = connection_student.get_student_by_id(student_id)
    student_info = connection_student.resolve_student(student_raw)
    student_name = student_info['name']

    room_name_list = []
    for group in student_info['group-list']:
        room = group['class-room']
        room_name_list.append(str(room['id']) + ' | ' + room['name'])

    layout = [
        [sg.Text(f'Aluno: {student_name}')],
        [sg.Text(f'Salas: '), sg.Combo(room_name_list, default_value=room_name_list[0], readonly=True, key='list'), sg.Button('Entrar')],
        [sg.Text('\n')],
        [sg.Button('Voltar'), sg.Button('Resultados')]
    ]     
    return sg.Window('Avaliação 360 - Aluno', layout, element_justification='c')

def event_handler(event, values):
    global student_info
    room_name = values['list']
    room_id = int(room_name.split(' | ')[0])

    if event == 'Voltar':
        app.change_interface(interface_login.create_window(), interface_login.event_handler)
    elif event == 'Entrar':
        app.change_interface(interface_student_specific.create_window(student_info['id'], room_id), interface_student_specific.event_handler)
    elif event =='Resultados':
        app.pop_up('Desenvolvimento...')