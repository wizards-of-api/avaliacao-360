import app
import PySimpleGUI as sg
import interface.adm as adm

def create_window():
    layout = [
    [sg.Text('Dashboard desempenho médio de turma', font=('Arial Black', 16))],
    #na linha abaixo tem espaço para um dash de adm

    [sg.Text('Dashboard desempenho de grupo', font=('Arial Black', 16))],
    #na linha abaixo tem espaço para um dash de adm

    #no insigh (na linha abaixo) pode por destaques, tipo um qual foi a maior mais a competencia mais votada no grupo
    [sg.Text('Insigh', font=('Arial Black', 16))],
    [sg.Button('voltar',key='return')]
    ]
          

    return sg.Window('Avaliação 360 - Dashboard Aluno', layout, element_justification='c')

def event_handler(event, _):
    if event == 'return':
        app.change_interface(adm.create_window(), adm.event_handler)
    