import PySimpleGUI as sg
import interface.entity_manager as entity_manager
import connection.student as connection_student
import connection.class_room as connection_room
import app
from config import TITLE_FONT, LABEL_FONT

def select_group_handler(student_name, room_id_list):
    room_list = [connection_room.get_class_room_by_id(room_id) for room_id in room_id_list]
    i = [0]
    group_id_list = []

    def create_window():
        nonlocal room_id_list
        room = room_list[i[0]]
        group_list = connection_room.get_class_room_group_list(room['id'])
        group_name_list = [str(group['id']) + ' | ' + group['name'] for group in group_list]
        layout = [
            [sg.Text('Turma: ' + room['name'], font=LABEL_FONT)],
            [sg.Text('Grupo: ', font=LABEL_FONT), sg.Combo(group_name_list, readonly=True, key='list', font=LABEL_FONT)],
            [sg.Button('Confirmar', key='confirm', font=LABEL_FONT)]
        ]
        return sg.Window('Escolha o grupo', layout)
    
    def event_handler(event, values):
        nonlocal i, group_id_list
        group_name = values['list']
        if event == 'confirm':
            if group_name == '':
                sg.popup('Por favor, selecione um grupo', font=LABEL_FONT)
                return
            group_id = int(group_name.split(' | ')[0])
            group_id_list.append(group_id)
            i[0] = i[0] + 1
            if len(group_id_list) >= len(room_id_list):
                connection_student.create_student({'name': student_name,'group-id-list': group_id_list})            
                sg.popup(f'Aluno {student_name} criado com sucesso!', font=LABEL_FONT)
                app.change_interface(entity_manager.create_window(), entity_manager.event_handler)
            else:
                app.change_interface(create_window(), event_handler)
    
    app.change_interface(create_window(), event_handler)

def create_window():
    room_list = connection_room.get_class_room_list()
    room_name_list = [str(room['id']) + ' | ' + room['name'] for room in room_list]

    room_check_list = []
    for room_name in room_name_list:
        room_check_list.append([sg.Checkbox(room_name, key='cb_room-'+str(len(room_check_list)+1), font=LABEL_FONT)])

    layout = [
        [sg.Text('Criar Aluno', font=TITLE_FONT)],
        [sg.Text('Nome do Aluno:', font=LABEL_FONT), sg.Input(key='input', font=LABEL_FONT, size=(22,1))],
        [sg.Column(room_check_list)],
        [sg.Button('Registrar Aluno', key = 'create student', font=LABEL_FONT),sg.Button('Voltar', key = 'return interface', font=LABEL_FONT)]
        ]
    return sg.Window('Avaliação 360 - Criar Aluno', layout, element_justification='c', finalize=True)

def event_handler(event, values):
    input_student = values['input']
    room_id_list = []
    for key, value in values.items():
        split_value = key.split('-')
        if split_value[0] != 'cb_room':
            continue
        if value:
            room_id_list.append(int(split_value[1]))
    if event == 'return interface':
        app.change_interface(entity_manager.create_window(), entity_manager.event_handler)
    elif event == 'create student':
        if input_student == '':
            sg.popup('Por favor, preencha o nome do aluno', font=LABEL_FONT)
        elif len(room_id_list) == 0:
            sg.popup('Por favor, selecione um grupo', font=LABEL_FONT)
        else:
            select_group_handler(input_student, room_id_list)
            #connection_student.create_student({'name': input_student,'group-id': group_id})            
            #sg.popup(f'Aluno {input_student} criado com sucesso!')
