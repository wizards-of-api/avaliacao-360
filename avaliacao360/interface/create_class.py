import PySimpleGUI as sg
import interface.create_room as create_room
import connection.class_room as create_class
import app

def create_window(key):
    layout = [
        [sg.Text('Criação de Turmas:')],
        [sg.Input('Digite o nome da Turma', key='input', s=(22, 1))],
        [sg.Text('', key='output')],
        [sg.Button('Criar', key='button create', s=(8, 1)),sg.Button('Voltar', key='return interface', s=(8, 1))]
        ]
    return sg.Window('Avaliação 360 - Criar Classe/Turma/Grupo', layout, element_justification='c', finalize= True)
    

def event_handler(event, values):
    input_class = values['input']
    if event == 'return interface':
        app.change_interface(create_room.create_window(), create_room.event_handler)
    elif event == 'button create':
        if input_class == '':
            app.pop_up('Por favor, insira o nome da Turma!')
        else:
            create_class.create_class_room({'name': input_class})
            app.pop_up(msg='Turma %s criada com sucesso' %input_class)
            
