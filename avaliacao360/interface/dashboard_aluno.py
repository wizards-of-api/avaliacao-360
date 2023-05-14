import app
import PySimpleGUI as sg
import interface.dashboard_aluno as interface_dashboard_aluno
import interface.student as student
import interface.create_class as interface_createclass
import connection.student as connection_student
import connection.result_evaluation as result_evaluation

def create_window(name):
    global _name
    _name = name
    result_group = result_evaluation.evaluation_result_student(_name)
    layout = [
                [sg.Text("Desenvolvendo")],
                [sg.Button('Voltar', key='return', s=(18, 1))]
            ]

    return sg.Window('Avaliação 360 - Dashboard Aluno', layout, element_justification='c')

def event_handler(event, _):
    global _name
    if event == 'return':
        app.change_interface(student.create_window(_name), student.event_handler)