import app
import config
import connection.evaluation as connect_eval
import connection.group as connect_group
from utils.graph_generator import generate_table, generate_bar_graph, draw_figure
import interface.student_specific as interface_student_specific

import PySimpleGUI as sg

def create_window(student_id, group_id, sprint):
    global arg_student, arg_group, arg_sprint
    arg_student = student_id
    arg_group = group_id
    arg_sprint = sprint

    eval_list = connect_eval.get_evaluation_by_group_id(group_id)
    eval_list = [evaluation for evaluation in eval_list if evaluation['status'] == 'done']

    sprint_list = [evaluation['sprint'] for evaluation in eval_list]

    table_top_row = ['Competencia', 'nota', 'feedback']
    table_rows = []

    combo = sg.Combo(sprint_list, key='sprint', readonly=True)
    if sprint > 0:
        combo.DefaultValue = sprint

        selected_eval = [evaluation for evaluation in eval_list if evaluation['sprint'] == sprint][0]

        for evaluator_id, evaluted_dict in selected_eval['answer-dict'].items():
            if evaluator_id == student_id:
                continue
            student_answer = evaluted_dict[str(student_id)]
            i = 0
            for answer in student_answer:
                if answer['value'] < 3:
                    table_rows.append([config.competence_list[i], answer['value'], answer['feedback']])
                i += 1

    feedback_table = generate_table('feeback-table', table_top_row, table_rows)

    average_list = [[] for _ in config.competence_list]

    if len(eval_list) > 0:
        for evaluation in eval_list:
            for evaluator_dict in evaluation['answer-dict'].values():
                student_answer = evaluator_dict[str(student_id)]
                i = 0
                for answer in student_answer:
                    average_list[i].append(answer['value'])
                    i += 1
        average_list = [sum(value_list) / len(value_list) for value_list in average_list]
    else:
        average_list = [0 for _ in average_list]
    fig = generate_bar_graph('Médias das Competencias das Sprints', 'Competencias', 'Média', config.competence_list, average_list, (8,5))

    group = connect_group.get_group_by_id(group_id)

    layout = [
        [sg.Text('Grupo: ' + group['name'])],
        [sg.Text('Sprint: '), combo, sg.Button('Refresh', key='refresh')],
        [feedback_table, sg.Canvas(key='canvas', size=(1000, 1000), background_color='gray')],
        [sg.Button('Voltar', key='return')]
    ]

    window = sg.Window('Avaliação 360 - Dashboard do aluno', layout, finalize=True)

    draw_figure(window['canvas'], fig)

    return window

def event_handler(event, values):
    global arg_student, arg_group, arg_sprint

    if event == 'refresh':
        if values['sprint'] == '':
            return
        
        app.change_interface(create_window(arg_student, arg_group, int(values['sprint'])), event_handler)
    if event == 'return':
        room_id = connect_group.get_group_by_id(arg_group)['class-room-id']
        app.change_interface(interface_student_specific.create_window(arg_student, room_id), interface_student_specific.event_handler)