from utils.filters import filter_by_key
import connection.controller as controller

key = 'student-list'

def get_student_list():
    """
    Retorna a lista de todos os estudantes.
    
    Retorna:
    list: A lista de todos os estudantes.
    """
    return controller.get_data()[key]


def get_student_by_id(id):
    """
    Retorna o estudante com o ID fornecido.
    
    Args:
    id (int): O ID do estudante.
    
    Retorna:
    dict: O estudante com o ID fornecido.
    """
    return filter_by_key(get_student_list(), 'id', id)


def get_student_by_name(name):
    """
    Retorna o estudante com o nome fornecido.
    
    Args:
    name (str): O nome do estudante.
    
    Retorna:
    dict: O estudante com o nome fornecido.
    """
    return filter_by_key(get_student_list(), 'name', name)


def create_student(new_student_dict):
    """
    Cria um novo estudante e adiciona-o à lista de estudantes.
    
    Args:
    new_student_dict (dict): Um dicionário contendo as informações do novo estudante:
        'group-id' (int): O ID do grupo ao qual o estudante pertence.
        'name' (str): O nome do estudante.
    
    Retorna:
    int: O ID do novo estudante.
    """
    student_list = get_student_list()

    id = controller.get_last_id(key) + 1

    student_dict = {
        'id': id,
        'group-id': new_student_dict['group-id'],
        'name': new_student_dict['name'],
    }

    student_list.append(student_dict)
    controller.overwrite_data(key, student_list)
    
    return id
