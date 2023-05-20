import app
import PySimpleGUI as sg
import interface.login as interface_login  
import interface.entity_manager as entity_manager
import interface.resultevaluation as result_evaluation
import interface.sprint_control as request_evaluation
import interface.classlist as class_list
def create_window():
  layout = [ 
            [sg.Text('Administrador')], 
            [sg.Button('Criar turma/grupo/aluno/usuário', key='create room', s=(25, 1) )],
            [sg.Button('Resultados da avaliação', key='result evaluation', s=(25, 1))],
            [sg.Button('Requisitar avaliação', key='request evaluation', s=(25, 1))],
            [sg.Button('Lista de turmas/grupos', key='class list', s=(25, 1))],
            [sg.Button('Voltar', key='return interface', s=(25, 1))]
              ]
  return sg.Window('Avaliação 360 - Administrador', layout, element_justification='c', finalize=True)
  

def event_handler(event, _):
  if event == 'Cancel':

    app.close()

  elif event == 'return interface':

    app.change_interface(interface_login.create_window(), interface_login.event_handler)

  elif event == 'create room':

    app.change_interface(entity_manager.create_window(),entity_manager.event_handler)

  elif event == 'result evaluation':
    app.pop_up_advice('Em desenvolvimento')

  elif event == 'request evaluation':
    
    room_select_interface = request_evaluation.room_select_interface()

    app.change_interface(room_select_interface[0](),room_select_interface[1])

  elif event == 'class list':
    
    app.change_interface(class_list.create_window(),class_list.event_handler)
    