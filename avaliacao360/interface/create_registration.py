import PySimpleGUI as sg
import interface.entity_manager as entity_manager
import connection.student as connection_student
import connection.login as login
from utils.filters import filter_by_key
import app
import os
import sys

from utils.filters import filter_by_key

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'utils')))


def create_window():
    student_list = connection_student.get_student_list()
    student_name_list = []
    user_student_id_list = [user['student-id'] for user in login.get_username_list()]
    for student in student_list:
        if student['id'] in user_student_id_list:
            continue
        resolved_student = connection_student.resolve_student(student)
        student_name_list.append(
            str(resolved_student['id']) + ' | ' +
            resolved_student['name'])

    layout = [
        [sg.Text('Aluno:', size=(6,1)), sg.Combo(student_name_list, readonly=True, key = 'student_list',size=(35,1))],
        [sg.Text('Usuário:', size=(6,1)), sg.Input('', key='username', size=(35,1))],
        [sg.Text('Senha:', size=(6,1)), sg.Input('', key='password', password_char='*', size=(35,1))],
        [sg.Text('', key='error', text_color='red')],
        [sg.Button('Cadastrar', key='register', size=(10,1)),
         sg.Button('Voltar', key='return', size=(10,1))]
    ]
    return sg.Window('Cadastro de Aluno', layout, element_justification='c', finalize=True)


def event_handler(event, values):

    input_student = values['student_list']
    print('Evento:', event)  # adicionando um print para verificar o evento
    if event == 'return':
        app.change_interface(entity_manager.create_window(),
                             entity_manager.event_handler)
        return
    if input_student == '':
        app.pop_up('Por favor, selecione o estudante')
        return

    elif event == 'register':
        username = values['username']
        password = values['password']
        student_input = values['student_list']

        user_list = login.get_username_list()

        # Validar se o nome e senha foram preenchidos
        if not username.strip() or not password.strip():
            app.pop_up('Por favor, preencha o nome e a senha')
            return

        # Validar se a senha tem pelo menos 8 caracteres
        if len(password) < 8:
            app.pop_up('A senha deve ter pelo menos 8 caracteres')
            return

        elif filter_by_key(user_list, 'username', username):
            sg.popup('Usuário já existente')
        else:
            student_id = int(student_input.split(' | ')[0])

            credentials = {'username': username, 'password': password, 'student-id': student_id}
            login.create_user(credentials)
            app.pop_up(msg='Usuário %s criado com sucesso' %username)
            app.change_interface(entity_manager.create_window(),
                             entity_manager.event_handler)
