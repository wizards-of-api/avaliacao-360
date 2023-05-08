import PySimpleGUI as sg
import connection.group as connection_group
import connection.class_room as connection_class_room
import interface.create_room as create_room
import app
from utils.filters import filter_by_key

def create_window():
    class_room_list = connection_class_room.get_class_room_list()
    class_room_names = [class_room['name'] for class_room in class_room_list]
    layout = [
        [sg.Text('Nome do Grupo'), sg.Input(key='input')],
        [sg.Text('Turma'), sg.Combo(class_room_names, readonly=True, key='list')],
        [sg.Button('Registrar Grupo', key='create group')],
        [sg.Button('Voltar', key='return interface')]
        ]
    return sg.Window('Avaliação 360 - Criar Classe/Turma/Grupo', layout, element_justification='c', finalize= True)


def event_handler(event, values):
    group_list = connection_group.get_group_list()
    input_groupname = values['input']
    input_class_room_name = values['list']

    if event == 'return interface':
        app.change_interface(create_room.create_window(), create_room.event_handler)
    elif event == 'create group':
        if input_groupname == '':
            sg.popup('Por favor, preencha o nome do grupo')
        elif filter_by_key(group_list, 'name', input_groupname):
            sg.popup('Nome de grupo já existente')
        elif input_class_room_name == '':    
            sg.popup('Por favor, selecione uma turma')
        else:
            class_room_list = connection_class_room.get_class_room_list()
            class_room = filter_by_key(class_room_list, 'name', input_class_room_name)
            if class_room:
                class_room_id = class_room[0]['id']
                connection_group.create_group({'name': input_groupname, 'class-room-id': class_room_id})
                sg.popup(f'Grupo {input_groupname} criado com sucesso!')
            else:
                sg.popup('Turma não encontrada')