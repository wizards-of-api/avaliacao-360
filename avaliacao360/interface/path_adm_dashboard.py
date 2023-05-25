import app
import PySimpleGUI as sg
import interface.adm as adm

def create_window():
    layout = [
            [sg.Text('Qual dashboard você quer consultar?', font = ('Arial Black', 20))],
            [sg.Button('Dashboard da Turma', key='dash_class', s=(18,0)),
            sg.Button('Dashboard do Grupo', key='dash_group', s=(18,0)),
            sg.Button('Voltar', key='return', s=(18,0))]
            ]
    return sg.Window('Avaliação 360 - Dashboards Administrador Grupo e Turma', layout, element_justification='c', finalize=True)

def event_handler(event, _):
    if event == 'dash_class':
        app.pop_up('Em desenvolvimento...')
    elif event == 'dash_group':
        app.pop_up('Em desenvolvimento...')
    elif event == 'return':
        app.change_interface(adm.create_window(), adm.event_handler)