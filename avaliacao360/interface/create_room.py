import PySimpleGUI as sg
import interface.adm as interface_adm
import interface.create_class as create_class
import app

def create_window():
    layout = [
        [sg.Text('O que deseja criar?')],
        [sg.Button('Turma', key= 'class', s=(18,1))],
        [sg.Button('Grupo', key= 'group', s=(18,1))],
        [sg.Button('Aluno', key= 'student', s=(18,1))],
        [sg.Button('Voltar', key='return interface', s=(18, 1))]
        ]
    return sg.Window('Avaliação 360 - Criar Classe/Turma/Grupo', layout, element_justification='c', finalize= True)

def event_handler(event, _):
    if event == 'return interface':
        app.change_interface(interface_adm.create_window(), interface_adm.event_handler)
    elif event == 'class':
        app.change_interface(create_class.create_window(key='output'), create_class.event_handler)
