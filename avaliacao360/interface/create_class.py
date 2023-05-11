import PySimpleGUI as sg
import interface.entity_manager as entity_manager
import connection.class_room as create_class
from utils.filters import filter_by_key
import app

def create_window(key):
    layout = [
        [sg.Text('Criação de Turmas:'),sg.Input(key='input', s=(22, 1))],
        [sg.Text('', key='output')],
        [sg.Button('Criar', key='button create', s=(8, 1)),sg.Button('Voltar', key='return interface', s=(8, 1))]
        ]
    return sg.Window('Avaliação 360 - Criar Classe/Turma/Grupo', layout, element_justification='c', finalize= True)
    

def event_handler(event, values):
    input_class = values['input']
    class_list = create_class.get_class_room_list()

    if event == 'return interface':
        app.change_interface(entity_manager.create_window(), entity_manager.event_handler)
    elif event == 'button create':
        if input_class == '':
            sg.popup('Por favor, insira o nome da Turma!')
        elif filter_by_key(class_list, 'name', input_class):
            sg.popup('Nome da Turma já existente')
        else:
            create_class.create_class_room({'name': input_class})
            app.pop_up(msg='Turma %s criada com sucesso' %input_class)
            
