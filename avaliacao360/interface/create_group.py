import PySimpleGUI as sg
import connection.group as connection_group
import connection.class_room as connection_class_room
import interface.entity_manager as entity_manager
import app
from utils.filters import filter_by_key
from config import TITLE_FONT, LABEL_FONT

def create_window():
    class_room_list = connection_class_room.get_class_room_list()
    class_room_names = [str(class_room['id']) + ' | ' + class_room['name'] for class_room in class_room_list]

    col1 = [[sg.Text('Nome do Grupo:', font=LABEL_FONT)], [sg.Text('Turma:',font=LABEL_FONT)]]
    col2 = [[sg.Input(key='input', size=(22, 1), font=LABEL_FONT)], [sg.Combo(class_room_names, readonly=True, key='list',size=(22, 1), font=LABEL_FONT)]]

    layout = [
        [sg.Column(col1), sg.Column(col2)],
        [sg.Button('Registrar Grupo', key='create group', font=LABEL_FONT)],
        [sg.Button('Voltar', key='return interface', font=LABEL_FONT)]
        ]
    return sg.Window('Avaliação 360 - Criar Grupo', layout, element_justification='c', finalize= True)


def event_handler(event, values):
    input_groupname = values['input']
    input_class_room_name = values['list']

    if event == 'return interface':
        app.change_interface(entity_manager.create_window(), entity_manager.event_handler)
    elif event == 'create group':
        if input_class_room_name == '':    
            sg.popup('Por favor, selecione uma turma',font=LABEL_FONT)
            return
        
        class_room_id = int(input_class_room_name.split(' | ')[0])
        room_group_list = connection_class_room.get_class_room_group_list(class_room_id)

        if input_groupname == '':
            sg.popup('Por favor, preencha o nome do grupo', font=LABEL_FONT)
        elif filter_by_key(room_group_list, 'name', input_groupname):
            sg.popup('Nome de grupo já existente',font=LABEL_FONT)
            app.change_interface(create_window(), event_handler)
        else:
            connection_group.create_group({'name': input_groupname, 'class-room-id': class_room_id})
            sg.popup(f'Grupo {input_groupname} criado com sucesso!',font=LABEL_FONT)
            app.change_interface(create_window(), event_handler)