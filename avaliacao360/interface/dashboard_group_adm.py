import app
import config
import connection.adm_dash as adm_dash
import connection.class_room as connect_room
from utils.graph_generator import generate_combine_bar_graph, draw_figure
import interface.adm as interface_adm
from config import LABEL_FONT

import PySimpleGUI as sg

def create_window(room_id, group_id):
    global old_room_id
    old_room_id = room_id
    room_list = connect_room.get_class_room_list()
    room_str_list = [str(room['id']) + ' | ' + room['name'] for room in room_list]
    default_value = ''
    if room_id != 0:
      default_value = [room_str for room_str in room_str_list if int(room_str.split(' | ')[0]) == room_id][0]
    combo_room = sg.Combo(room_str_list, default_value, key='room', readonly=True, font=LABEL_FONT)

    group_list = connect_room.get_class_room_group_list(room_id)
    group_str_list = [str(group['id']) + ' | ' + group['name'] for group in group_list]
    default_value = ''
    if group_id != 0:
      default_value = [group_str for group_str in group_str_list if int(group_str.split(' | ')[0]) == group_id][0]
    combo_group = sg.Combo(group_str_list, default_value, key='group', readonly=True, font=LABEL_FONT)

    student_average = {
       'student-list': [],
       'data': []
    }
    sprint_average = {
       'sprint-list': [],
       'data': []
    }
    if group_id != 0: 
      student_average = adm_dash.generate_average_student_data(group_id)
      sprint_average = adm_dash.generate_average_student_data_by_sprint(group_id)

    graph1_fig = generate_combine_bar_graph('Média dos Alunos', 'Alunos', 'Médias', student_average['data'], config.competence_list, student_average['student-list'], (12, 4))
    graph2_fig = generate_combine_bar_graph('Média das Sprints', 'Sprint', 'Médias', sprint_average['data'], config.competence_list, sprint_average['sprint-list'], (12, 4))

    canvas1 = sg.Canvas(key='canvas1', background_color='gray')
    canvas2 = sg.Canvas(key='canvas2', background_color='gray')

    layout = [
        [sg.Text('Sala: ', font=LABEL_FONT), combo_room, combo_group, sg.Button('Refresh', key='refresh', font=LABEL_FONT)],
        [canvas1],
        [canvas2],
        [sg.Button('Voltar', key='return', font=LABEL_FONT)]
    ]

    window = sg.Window('Avaliação 360 - Dashboard dos Grupos (ADM)', layout, finalize=True)
    draw_figure(canvas1, graph1_fig)
    draw_figure(canvas2, graph2_fig)


    return window

def event_handler(event, values):
    global old_room_id
    if event == 'refresh':
        if values['group'] == '' and values['room'] == '':
            return
        
        room_id = int(values['room'].split(' | ')[0])
        
        group_id = 0
        if old_room_id == room_id:
          group_id = int(values['group'].split(' | ')[0])
        
        app.change_interface(create_window(room_id, group_id), event_handler)
    if event == 'return':
        app.change_interface(interface_adm.create_window(), interface_adm.event_handler)