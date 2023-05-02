import app
import PySimpleGUI as sg
import interface.login as interface_login  
import interface.createclass as create_class
import interface.resultevaluation as result_evaluation
import interface.sprint_control as request_evaluation
import interface.classlist as class_list

def create_window():
  layout = [ 
            [sg.Text('Administrador')], 
            [sg.Button('Criar turma/grupo/aluno', key='create class', s=(18, 1) )],
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

  elif event == 'create class':

    app.change_interface(create_class.create_window(),create_class.event_handler)

  elif event == 'result evaluation':
    
    app.change_interface(result_evaluation.create_window(),result_evaluation.event_handler)

  elif event == 'request evaluation':
    
    room_select_interface = request_evaluation.room_select_interface()

    app.change_interface(room_select_interface[0](),room_select_interface[1])

  elif event == 'class list':
    
    app.change_interface(class_list.create_window(),class_list.event_handler)
    