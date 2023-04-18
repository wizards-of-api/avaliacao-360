import PySimpleGUI as sg
import app

def create_window ():
    layout = [
                [sg.Text("Desenvolvimento...")]
                   ]
    return sg.Window('Avaliação 360 - Criar Classe/Turma/Grupo', layout, element_justification='c', finalize= True)

def event_handler(event, _):
    if event == "Desenvolvimento...":
        sg.Text("Desenvolvimento...")
