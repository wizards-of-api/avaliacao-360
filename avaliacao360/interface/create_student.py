import PySimpleGUI as sg
import interface.entity_manager as entity_manager
import connection.student as connection_student
import connection.group as connection_group
import app

def create_window():
    group_list = connection_group.get_group_list()
    group_name_list = []
    for group in group_list:
        resolved_group = connection_group.resolve_group(group)
        group_name_list.append(str(resolved_group['id']) + ' | ' + resolved_group['class-room']['name'] + ' / ' + resolved_group['name'])

    layout = [
        [sg.Text('Criar Aluno')],
        [sg.Text('Nome do Aluno:'), sg.Input(key='input')],
        [sg.Text('Grupo'), sg.Combo(group_name_list, readonly=True, key = 'list')],
        [sg.Button('Registrar Aluno', key = 'create student'),sg.Button('Voltar', key = 'return interface')]
        ]
    return sg.Window('Avaliação 360 - Criação de Alunos', layout, element_justification='c', finalize=True)

def event_handler(event, values):
    input_student = values['input']
    input_group = values['list']

    if event == 'return interface':
        app.change_interface(entity_manager.create_window(), entity_manager.event_handler)
    elif event == 'create student':
        if input_student == '':
            app.pop_up_advice('Por favor, preencha o nome do aluno')
        elif input_group == '':
            app.pop_up_advice('Por favor, selecione um grupo')
        else:          
            group_id = int(input_group.split(' | ')[0])
            connection_student.create_student({'name': input_student,'group-id': group_id})
            app.pop_up_success(f'Aluno {input_student} criado com sucesso!')
