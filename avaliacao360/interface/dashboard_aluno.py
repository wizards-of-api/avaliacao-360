import app
import PySimpleGUI as sg
import interface.student as student

def create_window(name):
    global _name
    _name = name
    layout = [
    [sg.Text('Dashboard desempenho médio do aluno', font=('Arial Black', 16))],
    #essa linha abaixo não sabemos muito se seria cabivel nos dashs do aluno
    [sg.Text('Dashboard 2', font=('Arial Black', 16))],
    #na linha abaixo tem espaço para um dash de aluno

    [sg.Text('comentarios da avaliação' , font=('Arial Black', 16))],
    #na linha abaixo tem espaço para um dash de aluno

    #no insigh (na linha abaixo) pode por destaques, tipo um qual foi a maior mais a competencia mais votada no grupo
    [sg.Text('Insigh', font=('Arial Black', 16))],
    [sg.Button('voltar',key='return')]
    ]
          

    return sg.Window('Avaliação 360 - Dashboard Aluno', layout, element_justification='c')

def event_handler(event, _):
    global _name
    if event == 'return':
        app.change_interface(student.create_window(_name), student.event_handler)
    