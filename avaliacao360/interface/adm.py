import app
import PySimpleGUI as sg
import interface.login as interface_login  
import interface.create_room as create_room
import interface.resultevaluation as result_evaluation
import interface.sprint_control as request_evaluation
import interface.classlist as class_list
import interface.dashboard_adm as dashboard_adm
def create_window():
  layout = [ 
            [sg.Text('Administrador')], 
            [sg.Button('Criar turma/grupo/aluno', key='create room', s=(18, 1) )],
            [sg.Button('Resultados da avaliação', key='result evaluation', s=(18, 1))],
            [sg.Button('Requisitar avaliação', key='request evaluation', s=(18, 1))],
            [sg.Button('Lista de turmas/grupos', key='class list', s=(18, 1))],
            [sg.Button('Voltar', key='return interface', s=(18, 1))]
              ]
  return sg.Window('Avaliação 360 - Administrador', layout, element_justification='c', finalize=True)
  

def event_handler(event, _):
  if event == 'Cancel':

    app.close()

  elif event == 'return interface':

    app.change_interface(interface_login.create_window(), interface_login.event_handler)

  elif event == 'create room':

    app.change_interface(create_room.create_window(),create_room.event_handler)

  elif event == 'result evaluation':
    
    app.change_interface(dashboard_adm.create_window(),dashboard_adm.event_handler)

  elif event == 'request evaluation':
    
    room_select_interface = request_evaluation.room_select_interface()

    app.change_interface(room_select_interface[0](),room_select_interface[1])

  elif event == 'class list':
    
    app.change_interface(class_list.create_window(),class_list.event_handler)
    