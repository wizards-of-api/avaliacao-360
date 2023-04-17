import sys, os

sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('./avaliacao360'))

import PySimpleGUI as sg
import avaliacao360.connection.class_room as connection_class_room
import avaliacao360.connection.group as connection_group
import avaliacao360.connection.evaluation as connection_eval
import avaliacao360.connection.student as connection_student

def choose_class_window():
    class_list = connection_class_room.get_class_room_list()
    class_name_list = [class_room['name'] for class_room in class_list]
    layout = [[sg.Text('Sala: '), sg.Combo(class_name_list, default_value=class_name_list[0], key='class')],
              [sg.Button('Confirmar')]]
    window = sg.Window('Escolher Sala', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == 'Confirmar':
            chosen_class_name = values['class']
            chosen_class_id = connection_class_room.get_class_room_by_name(chosen_class_name)[0]['id']

            window.close()
            choose_group_window(chosen_class_id)
            break

def choose_group_window(class_id):
    group_list = connection_class_room.get_class_room_group_list(class_id)
    group_name_list = [group['name'] for group in group_list]
    layout = [[sg.Text('Sala: '), sg.Combo(group_name_list, default_value=group_name_list[0], key='group')],
              [sg.Button('Voltar'), sg.Button('Confirmar')]]
    window = sg.Window('Escolher Grupo', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == 'Confirmar':
            chosen_group_name = values['group']
            chosen_group_id = connection_group.get_group_by_name(chosen_group_name)[0]['id']
            window.close()
            group_window(chosen_group_id)
            break
        elif event == 'Voltar':
            window.close()
            choose_class_window()
            break

def group_window(group_id):
    group_info = connection_group.resolve_group_by_id(group_id)
    student_list = connection_group.get_group_student_list(group_id)
    evaluation = connection_eval.get_evaluation_by_group_id(group_id)[0]

    student_name_list = [student['name'] for student in student_list]
    status_color = '#6AF77F'
    if evaluation['status'] == 'todo':
        status_color = '#E0D27E'

    layout = [
            [sg.Text('Grupo: ' + group_info['name'])],
            [sg.Text('Sala: ' + group_info['class-room']['name'])],
            [sg.Text('Alunos: ' + ', '.join(student_name_list))],
            [sg.Text('Status da Avaliação: '), sg.Text(evaluation['status'], text_color=status_color)],
        ]
    
    if evaluation['status'] == 'todo':
        todo_student_name_list = [connection_student.get_student_by_id(id)['name'] for id in evaluation['todo-student-id-list']]
        todo_col = [sg.Text('Alunos faltando: ' + ', '.join(todo_student_name_list))]
        layout.append(todo_col)

    layout.append([sg.Text('')])

    for evaluator_key, answer_dict in evaluation['answer-dict'].items():
        evaluator_name = connection_student.get_student_by_id(int(evaluator_key))['name']
        layout.append([sg.Text('--' + evaluator_name + '--')])

        for evaluated_key, answer_list in answer_dict.items():
            evaluated_name = connection_student.get_student_by_id(int(evaluated_key))['name']
            answer_str_list = [str(answer) for answer in answer_list]
            layout.append([sg.Text('    ' +  evaluated_name + ': ' + ' - '.join(answer_str_list))])
   
    layout.append([sg.Text('')])
    layout.append([sg.Button('Voltar'), sg.Button('Refresh')])


    window = sg.Window('Grupo - ' + group_info['name'], layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == 'Refresh':
            window.close()
            group_window(group_id)
            break
        elif event == 'Voltar':
            window.close()
            choose_group_window(group_info['class-room']['id'])
            break

choose_class_window()