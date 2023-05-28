import PySimpleGUI as sg
import connection.group as connection_group
import connection.class_room as connection_class_room
import interface.entity_manager as entity_manager
import app
from utils.filters import filter_by_key

def create_window():
    class_room_list = connection_class_room.get_class_room_list()
    class_room_names = [str(class_room['id']) + ' | ' + class_room['name'] for class_room in class_room_list]
    layout = [
        [sg.Text('Nome do Grupo'), sg.Input(key='input')],
        [sg.Text('Turma'), sg.Combo(class_room_names, readonly=True, key='list')],
        [sg.Button('Registrar Grupo', key='create group')],
        [sg.Button('Voltar', key='return interface')]
        ]
    return sg.Window('Avaliação 360 - Criar Grupo', layout, element_justification='c', finalize= True)


def event_handler(event, values):
    group_list = connection_group.get_group_list()
    input_groupname = values['input']
    input_class_room_name = values['list']

    if event == 'return interface':
        app.change_interface(entity_manager.create_window(), entity_manager.event_handler)
    elif event == 'create group':
        if input_class_room_name == '':    
            sg.popup('Por favor, selecione uma turma')
            return
        
        class_room_id = int(input_class_room_name.split(' | ')[0])
        room_group_list = connection_class_room.get_class_room_group_list(class_room_id)

        if input_groupname == '':
            sg.popup('Por favor, preencha o nome do grupo')
        elif filter_by_key(room_group_list, 'name', input_groupname):
            sg.popup('Nome de grupo já existente')
            app.change_interface(create_window(), event_handler)
        else:
            connection_group.create_group({'name': input_groupname, 'class-room-id': class_room_id})
            sg.popup(f'Grupo {input_groupname} criado com sucesso!')
            app.change_interface(create_window(), event_handler)