import PySimpleGUI as sg
import interface.adm as interface_adm
import app

def create_window ():
    layout = [
                [sg.Text("Desenvolvimento...")],
                [sg.Button('Voltar', key='return interface', s=(18, 1))]
                   ]
    return sg.Window('Avaliação 360 - Criar Classe/Turma/Grupo', layout, element_justification='c', finalize= True)

def event_handler(event, _):
    if event == 'return interface':
        app.change_interface(interface_adm.create_window(), interface_adm.event_handler)
    elif event == "Desenvolvimento...":
        sg.Text("Desenvolvimento...")
