import PySimpleGUI as sg
import interface.adm as interface_adm
import interface.create_class as create_class
import interface.create_registration as create_registration
import interface.create_group as create_group
import interface.create_student as create_student
import app
from config import TITLE_FONT, LABEL_FONT

def create_window():
    layout = [
        [sg.Text('O que deseja criar?', font=TITLE_FONT)],
        [sg.Button('Turma', key= 'class', s=(22,1), font=LABEL_FONT)],
        [sg.Button('Grupo', key= 'group', s=(22,1), font=LABEL_FONT)],
        [sg.Button('Aluno', key= 'student', s=(22,1), font=LABEL_FONT)],
        [sg.Button('Usuário', key= 'username', s=(22,1), font=LABEL_FONT)],
        [sg.Button('Voltar', key='return interface', s=(22, 1), font=LABEL_FONT)]
        ]
    return sg.Window('Avaliação 360 - Criar Classe/Turma/Grupo', layout, element_justification='c', finalize= True)

def event_handler(event, _):
    if event == 'return interface':
        app.change_interface(interface_adm.create_window(), interface_adm.event_handler)
    elif event == 'class':
        app.change_interface(create_class.create_window(), create_class.event_handler)
    elif event == 'group':
        app.change_interface(create_group.create_window(), create_group.event_handler)
    elif event == 'student':
        app.change_interface(create_student.create_window(), create_student.event_handler)
    elif event == 'username':
        app.change_interface(create_registration.create_window(), create_registration.event_handler)
