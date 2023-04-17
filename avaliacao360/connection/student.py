from utils.filters import filter_by_key
import connection.controller as controller
import connection.group as group_connection
import connection.evaluation as evaluation_connection

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
    return filter_by_key(get_student_list(), 'id', id)[0]


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

def get_student_evaluation_by_id(student_id):
    """
    Retorna um dict das avaliações de um estudante

    :parâmetro student_id: referencia do estudante
    :return: array de dict do estudante
    """
    return evaluation_connection.get_evaluation_by_student_id(student_id)

def check_student_todo_evaluation(student_id):
    """
    Retorna se o aluno tem uma avaliação disponivel ou não

    :parâmetro student_id: ID do estudante str
    :return: bool
    """
    evaluation_list = get_student_evaluation_by_id(student_id)
    for evaluation in evaluation_list:
        if student_id in evaluation['todo-student-id-list']:
            return True
    return False

def resolve_student(student_dict):
    """
    Transforma o inteiro group-id em um dict de grupo ja resolvido

    :parâmetro student_dict: Dicionario a ser convertido
    :return: Dicionario convertido
    """
    group = group_connection.resolve_group_by_id(student_dict['group-id'])
    del student_dict['group-id']
    student_dict['group'] = group
    return student_dict

def resolve_student_by_id(student_id):
    """
    Transforma o inteiro group-id em um dict de grupo ja resolvido

    :parâmetro student_id: id do dicionario a ser convertido
    :return: dicionario convertido
    """
    return resolve_student(get_student_by_id(student_id))