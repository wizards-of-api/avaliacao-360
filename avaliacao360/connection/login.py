
from connection.controller import get_data, get_last_id
from os.path import abspath
import json
from os.path import abspath

key = 'user-list'

mock_path = abspath('./mock_db.json')

def get_username_list():
    """
    Retorna a lista de salas de aula armazenada no banco de dados mockado.
    """
    return get_data()[key]

def create_user(credentials):
    """
    Cria um novo usuário com as credenciais fornecidas e adiciona-o à lista de usuários no arquivo JSON.
    """
    data = get_data()
    username_id = get_last_id(key) + 1

    # student_list = get_student_list()
    student_id = get_last_id('student-list')

    username = credentials['username']
    password = credentials['password']

    data['user-list'].append(
        {'id': username_id,
         'student-id':student_id,
         'username': username, 
         'password': password
         })

    # Salva os dados atualizados no arquivo JSON
    with open(mock_path, 'w') as mock_db_file:
        json.dump(data, mock_db_file)

import json

def check_login(username, password):
    """
    Verifica se o usuário e a senha existem no JSON e retorna True se forem encontrados, caso contrário, retorna False.
    """
    user_list = get_username_list()

    for user in user_list:
        if user['username'] == username and user['password'] == password:
            return user['id']

    return False
