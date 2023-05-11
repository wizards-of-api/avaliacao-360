import PySimpleGUI as sg
import interface.entity_manager as entity_manager
import connection.group as connection_group
import connection.class_room as connection_class_room
import connection.student as connection_student
import app
import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'utils')))


def create_window(key):
    student_list = connection_student.get_student_list()
    student_names = [student['name'] for student in student_list]
    class_room_list = connection_class_room.get_class_room_list()
    class_room_names = [class_room['name'] for class_room in class_room_list]
    group_list = connection_group.get_group_list()
    group_names = [group['name'] for group in group_list]
    layout = [
        [sg.Text('Aluno'), sg.Combo(student_names, readonly=True, key='student_names', size=(35,1))],
        [sg.Text('Turma'), sg.Combo(class_room_names, readonly=True, key='class', size=(35,1))],
        [sg.Text('Grupo'), sg.Combo(group_names, readonly=True, key='group', size=(35,1))],
        [sg.Text('Usuário:', size=(6,1)), sg.Input('', key='user_name', size=(35,1))],
        [sg.Text('Senha:', size=(6,1)), sg.Input('', key='password', password_char='*', size=(35,1))],
        [sg.Text('', key='error', text_color='red')],
        # [sg.Text('', key='output')],
        [sg.Button('Cadastrar', key='register', size=(10,1)),
         sg.Button('Voltar', key='return', size=(10,1))]
    ]
    return sg.Window('Cadastro de Aluno', layout, element_justification='c', finalize=True)



def event_handler(event, values):
    print('Evento:', event)  # adicionando um print para verificar o evento
    if event == 'return':
        app.change_interface(entity_manager.create_window(),
                             entity_manager.event_handler)
    elif event == 'register':
        user_name = values['user_name']
        password = values['password']

        # Validar se o nome e senha foram preenchidos
        if not user_name.strip() or not password.strip():
            app.pop_up('Por favor, preencha o nome e a senha')
            return

        # Validar se a senha tem pelo menos 8 caracteres
        if len(password) < 8:
            app.pop_up('A senha deve ter pelo menos 8 caracteres')
            return

        # Armazenar o cadastro em um arquivo JSON
         
        path = os.path.join(os.path.dirname(__file__), '..', 'utils', 'users_register.json')
        if os.path.exists(path) and os.path.getsize(path) > 0:
            with open(path, 'r') as f:
                data = json.load(f)
        else:
            data = {}

        if user_name in data:
            app.pop_up('Este nome de usuário já foi cadastrado')
            return

        data[user_name] = password

        with open(path, 'w') as f:
            json.dump(data, f)

        app.pop_up('Cadastro realizado com sucesso')
        app.change_interface(entity_manager.create_window(),
                             entity_manager.event_handler)
