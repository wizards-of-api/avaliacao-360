import PySimpleGUI as sg
import interface.entity_manager as entity_manager
import app
import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'utils')))


def create_window(key):
    layout = [
        [sg.Text('Nome do Aluno:', size=(14,1)), sg.Input('', key='name', size=(20,1))],
        [sg.Text('Senha:', size=(14,1)), sg.Input('', key='password', password_char='*', size=(20,1))],
        [sg.Text('', key='error', text_color='red')],
        [sg.Text('', key='output')],
        [sg.Button('Cadastrar', key='register', size=(10,1)),
         sg.Button('Voltar', key='return', size=(10,1), button_color=('white', 'gray'))]
    ]
    return sg.Window('Cadastro de Aluno', layout, element_justification='c', finalize=True)



def event_handler(event, values):
    print('Evento:', event)  # adicionando um print para verificar o evento
    if event == 'return':
        app.change_interface(entity_manager.create_window(),
                             entity_manager.event_handler)
    elif event == 'register':
        name = values['name']
        password = values['password']

        # Validar se o nome e senha foram preenchidos
        if not name.strip() or not password.strip():
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

        if name in data:
            app.pop_up('Este nome de usuário já foi cadastrado')
            return

        data[name] = password

        with open(path, 'w') as f:
            json.dump(data, f)

        app.pop_up('Cadastro realizado com sucesso')

