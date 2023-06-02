import interface.student_general as student_general
import connection.student_dash as stud_dash
import connection.student as connect_stud
import PySimpleGUI as sg
import app
from utils.graph_generator import generate_radial_graph, generate_table, draw_figure
from os.path import abspath

mock_path = abspath('./mock_db.json')

def create_window(student_id):
    global _student_id
    _student_id = student_id
    student_raw = connect_stud.get_student_by_id(student_id)
    student_info = connect_stud.resolve_student(student_raw)
    student_name = student_info['name']

    table_data = []

    for group in student_info['group-list']:
        group_id = group['id']
        general_data = stud_dash.general_dash(_student_id, group_id)
        media = general_data['average']
        name_group = general_data['group']
        sprint_numbers = general_data['sprint']

        for sprint_number in sprint_numbers:
            sprint_name = f'Sprint {sprint_number}'

        competencies = ['Comunicação', 'Contribuição', 'Engajamento', 'Conhecimento', 'Entrega', 'Auto-Gestão']
        scores = media

        table_data.append([name_group, sprint_name, *scores])

    layout = [
        [sg.Text('Dashboard Geral do Aluno')],
        [sg.Text(f'Aluno: {student_name}')],
        [sg.Canvas(background_color='grey', key='dashradial')],
        [generate_table('table_key', ['Turma', 'Sprint'] + competencies, table_data)],
        [sg.Button('Voltar')]
    ]
    window = sg.Window('Avaliação 360 - Aluno', layout, finalize=True)

    fig = generate_radial_graph('Gráfico Radial', media, competencies, (10, 6))
    draw_figure(window['dashradial'], fig)

    return window

def event_handler(event, _):
    global _student_id
    if event == 'Voltar':
        app.change_interface(student_general.create_window(_student_id), student_general.event_handler)
