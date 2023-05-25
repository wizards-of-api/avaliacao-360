import connection.student as connect_stud
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import numpy as np
import json
from utils.graph_generator import generate_radial_graph
from os.path import abspath

mock_path = abspath('./mock_db.json')

def create_window(local_student_id):
    global student_id
    student_info = connect_stud.get_student_by_id(local_student_id)
    student_name = student_info['name']
    student_id = local_student_id
    print(student_info)

    for group_id in student_info['group-id-list']:
        print(group_id) # Obter as notas pelo ID do usuário

    layout = [
        [sg.Text('Dashboard Geral do Aluno')],
        [sg.Text(f'Aluno: {student_name}')],
        [sg.Button('Gerar Gráfico')],
    ]
    return sg.Window('Avaliação 360 - Aluno', layout, element_justification='c')

def event_handler(event, _):
    if event == 'Gerar Gráfico':
        title = 'Gráfico Radial'
        data = [10, 10, 10, 10, 10]  #Atualizar de acordo com as médias de cada competência e de acordo com o turmo
        label_list = ['Autogestão', 'Colaboração', 'Competência', 'Comunicação', 'Entregas']
        size = (6, 6)
        fig = generate_radial_graph(title, data, label_list, size)

        plt.figure(fig.number)
        plt.show()
    else:
        print("Dados de avaliação não encontrados para o aluno logado.")
