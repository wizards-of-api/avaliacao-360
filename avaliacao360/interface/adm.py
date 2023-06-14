import app
import PySimpleGUI as sg
import interface.login as interface_login  
import interface.entity_manager as entity_manager
import interface.sprint_control as request_evaluation
import interface.dashboard_room_adm as dashboard_room_adm
import interface.dashboard_group_adm as dashboard_group_adm
from config import TITLE_FONT, LABEL_FONT

def create_window():
  layout = [ 
      [sg.Text('Administrador', font=TITLE_FONT)], 
      [sg.Button('Criar turma/grupo/aluno', key='create room', font=LABEL_FONT, size=(22, 1))],
      [sg.Button('Resultados de Turmas', key='dash-room', font=LABEL_FONT, size=(22, 1))],
      [sg.Button('Resultados de Grupo', key='dash-group', font=LABEL_FONT, size=(22, 1))],
      [sg.Button('Controle de sprint', key='request evaluation', font=LABEL_FONT, size=(22, 1))],
      [sg.Button('Voltar', key='return interface', font=LABEL_FONT, size=(22, 1))]
  ]
  return sg.Window('Avaliação 360 - Administrador', layout, element_justification='c', finalize=True)
  

def event_handler(event, _):
  if event == 'Cancel':

    app.close()

  elif event == 'return interface':

    app.change_interface(interface_login.create_window(), interface_login.event_handler)

  elif event == 'create room':

    app.change_interface(entity_manager.create_window(),entity_manager.event_handler)

  elif event == 'dash-room':
    app.change_interface(dashboard_room_adm.create_window(0), dashboard_room_adm.event_handler)

  elif event == 'dash-group':
    app.change_interface(dashboard_group_adm.create_window(0,0), dashboard_group_adm.event_handler)

  elif event == 'request evaluation':
    
    room_select_interface = request_evaluation.room_select_interface()

    app.change_interface(room_select_interface[0](),room_select_interface[1])
    