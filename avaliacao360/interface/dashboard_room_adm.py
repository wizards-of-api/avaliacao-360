import app
import config
import connection.adm_dash as adm_dash
import connection.class_room as connect_room
from utils.graph_generator import generate_combine_bar_graph, draw_figure
import interface.adm as interface_adm

import PySimpleGUI as sg

def create_window(room_id):
    room_list = connect_room.get_class_room_list()
    room_str_list = [str(room['id']) + ' | ' + room['name'] for room in room_list]
    default_value = ''
    if room_id != 0:
      default_value = [room_str for room_str in room_str_list if int(room_str.split(' | ')[0]) == room_id][0]
    combo = sg.Combo(room_str_list, default_value, key='room', readonly=True)

    groups_average = {
       'group-list': [],
       'data': []
    }
    sprint_average = {
       'sprint-list': [],
       'data': []
    }
    if room_id != 0: 
      groups_average = adm_dash.generate_average_group_data(room_id)
      sprint_average = adm_dash.generate_average_group_data_by_sprint(room_id)

    graph1_fig = generate_combine_bar_graph('Média dos Grupos', 'Grupos', 'Médias', groups_average['data'], config.competence_list, groups_average['group-list'], (8, 4))
    graph2_fig = generate_combine_bar_graph('Média das Sprints', 'Sprint', 'Médias', sprint_average['data'], config.competence_list, sprint_average['sprint-list'], (8, 4))

    canvas1 = sg.Canvas(key='canvas1', size=(5, 5), background_color='gray')
    canvas2 = sg.Canvas(key='canvas2', size=(5, 5), background_color='gray')

    layout = [
        [sg.Text('Sala: '), combo, sg.Button('Refresh', key='refresh')],
        [canvas1],
        [canvas2],
        [sg.Button('Voltar', key='return')]
    ]

    window = sg.Window('Avaliação 360 - Dashboard das salas (ADM)', layout, finalize=True)
    draw_figure(canvas1, graph1_fig)
    draw_figure(canvas2, graph2_fig)


    return window

def event_handler(event, values):
    if event == 'refresh':
        if values['room'] == '':
            return
        
        room_id = int(values['room'].split(' | ')[0])
        app.change_interface(create_window(room_id), event_handler)
    if event == 'return':
        app.change_interface(interface_adm.create_window(), interface_adm.event_handler)