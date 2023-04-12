from utils.filters import filter_by_key
from avaliacao360.connection.controller import get_data, get_last_id, overwrite_data
import connection.group as group_connection

key = 'class-room-list'

def get_class_room_list():
    """
    Retorna a lista de salas de aula armazenada no banco de dados mockado.
    """
    return get_data()[key]
    
def get_class_room_by_id(id):
    """
    Retorna a sala de aula com o id especificado.
    
    :parâmetro id: Inteiro representando o id da sala de aula.
    :return: Um dicionário representando a sala de aula encontrada, ou None caso não seja encontrada.
    """
    return filter_by_key(get_class_room_list(), 'id', id)

def get_class_room_by_name(name):
    """
    Retorna a sala de aula com o nome especificado.
    
    :parâmetro name: String representando o nome da sala de aula.
    :return: Um dicionário representando a sala de aula encontrada, ou None caso não seja encontrada.
    """
    return filter_by_key(get_class_room_list(), 'name', name)

def get_class_room_group_list(id):
    """
    Retorna a lista de grupos associados à sala de aula com o id especificado.
    
    :parâmetro id: Inteiro representando o id da sala de aula.
    :return: Uma lista de dicionários representando os grupos encontrados.
    """
    group_list = group_connection.get_group_list()
    return [group for group in group_list if group['class-room-id'] == id]

def get_class_room_student_list(id):
    """
    Retorna a lista de estudantes associados à sala de aula com o id especificado.
    
    :parâmetro id: Inteiro representando o id da sala de aula.
    :return: Uma lista de dicionários representando os estudantes encontrados.
    """
    group_list = get_class_room_group_list(id)
    student_list = []
    for group in group_list:
        print(group)
        student_list += group_connection.get_group_student_list(group['id'])
    return student_list

def create_class_room(new_class_room_dict):
    """
    Cria uma nova sala de aula com as informações fornecidas.
    
    :parâmetro new_class_room_dict: Um dicionário representando as informações da nova sala de aula.
    :return: O id da sala de aula criada.
    """
    class_room_list = get_class_room_list()

    id = get_last_id(key) + 1

    class_room_dict = {
        'id': id,
        'name': new_class_room_dict['name'],
    }

    class_room_list.append(class_room_dict)
    overwrite_data(key, class_room_list)
    return id