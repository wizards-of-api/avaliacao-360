import app
import PySimpleGUI as sg
import interface.login as interface_login  

def create_window():
  layout = [ 
            [sg.Text('Administrador')], 
            [sg.Button('Criar turma/grupo/aluno', key='create class', s=(18, 1) )],
            [sg.Button('Resultados da avaliação', key='result evaluation', s=(18, 1))],
            [sg.Button('Requisitar avaliação', key='request evaluation', s=(18, 1))],
            [sg.Button('Lista de turmas/grupos', key='class list', s=(18, 1))]
              ]
  return sg.Window('Avaliação 360 - Administrador', layout, element_justification='c', finalize=True)
  

def event_handler(event, _):
  if event == 'Cancel':
    app.close()
  elif event == 'Back':
    app.change_interface(interface_login)

