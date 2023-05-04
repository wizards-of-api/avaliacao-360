import app
import interface.dashboard_aluno as interface_dashboard_aluno
import interface.student as interface_student
import interface.create_class as interface_createclass
import connection.student as connection_student
import PySimpleGUI as sg

def create_window(name):
    global _name
    _name = name
    layout = [
                [sg.Text(interface_createclass.dev_text)],
                [sg.Button('Voltar', key='return', s=(18, 1))]
            ]

    return sg.Window('Avaliação 360 - Dashboard Aluno', layout, element_justification='c')

def event_handler(event, _):
    global _name
    if event == 'return':
        app.change_interface(interface_student.create_window(_name), interface_student.event_handler)