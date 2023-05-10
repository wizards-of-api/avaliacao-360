import PySimpleGUI as sg
import interface.entity_manager as entity_manager
import connection.student as connection_student
import connection.group as connection_group
import app
from utils.filters import filter_by_key

def create_window():
    group_list = connection_group.get_group_list()
    group_names = [group['name'] for group in group_list]
    layout = [
        [sg.Text('Criar Aluno')],
        [sg.Text('Nome do Aluno:'), sg.Input(key='input')],
        [sg.Text('Insira a senha de login:'), sg.Input(key='password')],
        [sg.Text('Grupo'), sg.Combo(group_names, readonly=True, key = 'list')],
        [sg.Button('Registrar Aluno', key = 'create student'),sg.Button('Voltar', key = 'return interface')]
        ]
    return sg.Window('Avaliação 360 - Criar Aluno', layout, element_justification='c', finalize=True)

def event_handler(event, values):
    student_list = connection_student.get_student_list()
    input_student_name = values['input']
    input_student_password = values['password']
    input_group_name = values['list']

    if event == 'return interface':
        app.change_interface(entity_manager.create_window(), entity_manager.event_handler)
    elif event == 'create student':
        if input_student_name == '':
            sg.popup('Por favor, preencha o nome do aluno')
        elif input_student_password == '':
            sg.popup('Por favor, insira uma senha para login')
        elif filter_by_key(student_list, 'name', input_student_name):
            sg.popup('Aluno já cadastrado')
        elif input_group_name == '':
            sg.popup('Por favor, selecione um grupo')
        else:
            group_list = connection_group.get_group_list()
            group = filter_by_key(group_list, 'name', input_group_name)
            if group:
                group_id = group[0]['id']
                connection_student.create_student({'name': input_student_name,'group-id': group_id, 'password': input_student_password})
                sg.popup(f'Aluno {input_student_name} criado com sucesso!')
            else:
                sg.popup('Grupo não encontrado')
