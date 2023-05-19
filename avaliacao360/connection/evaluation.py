from utils.filters import filter_by_key, replace_on_list
import connection.controller as controller
import connection.group as group_connection
import connection.student as student_connection

key = 'evaluation-list'

def get_evaluation_list():
    """
    Retorna lista de avaliações
    """
    return controller.get_data()[key]

def get_evaluation_by_id(id: int):
    """
    Retorna avaliação usando um id.

    :parâmetro id: um integer que repesenta o id que deseja procurar.parâmetro
    :return: dicionario da avaliação
    """
    return filter_by_key(get_evaluation_list(), 'id', id)

def get_evaluation_by_student_id(student_id: int):
    """
    Retorna avaliação usando o id de um estudante.

    :parâmetro student_id: um integer que representa o id do estudante que deseja procurar.
    :return: dicionario da avaliação
    """

    group_id = student_connection.get_student_by_id(student_id)['group-id']
    return filter_by_key(get_evaluation_list(), 'group-id', group_id)

def get_evaluation_by_group_id(group_id: int):
    """
    Returna avaliação usando o id de um grupo.

    :parâmetro group_id: um integer que representa o id do grupo que deseja procurar.
    :return: dicionario da avaliação
    """
    return filter_by_key(get_evaluation_list(), 'group-id', group_id)

def force_close_evaluation(evaluation: dict):
    evaluation['unfinish-student-id-list'] = evaluation['todo-student-id-list']
    evaluation['todo-student-id-list'] = []
    return close_evaluation(evaluation)

def close_evaluation(evaluation: dict):
    """
    Checa se a avaliação esta pronta e modifica os dados no bando de dados mocado (ficticio).

    Retorna False se não estaja finalizado e True caso contrario.

    :parâmetro evaluation: dicionario da avaliação
    :return: bool
    """
    if(len(evaluation['todo-student-id-list']) != 0):
        return False
    
    evaluation['status'] = 'done'
    del evaluation['todo-student-id-list']

    evaluation_list = get_evaluation_list()
    evaluation_list = replace_on_list(evaluation_list, 'id', evaluation)

    controller.overwrite_data(key, evaluation_list)

    return True
    
def validate_answer_dict(student_id: int, answer_dict: dict):
    student = student_connection.get_student_by_id(student_id)
    group_student_list = group_connection.get_group_student_list(student['group-id'])
    student_id_list = [student['id'] for student in group_student_list]

    for evaluted_id, answer_list in answer_dict.items():
        if evaluted_id not in student_id_list:
            raise Exception('Aluno com id [' + str(evaluted_id) + '] não pertence ao mesmo grupo do aluno com id [' + str(student_id) + ']')
        for individual_answer in answer_list:
            if type(individual_answer) != dict:
                raise Exception('Respostas deve ser um dicionario com as chaves [value, feedback]')
            for key in individual_answer.keys():
                if key not in ['value', 'feedback']:
                    raise Exception('Resposta com chave [' + key + '] invalida')


# Adicionar validação de resposta
def answer_evaluation(student_id: int, evaluation_id: int, answer_dict: dict):
    """
    Adiciona a repostas answer_dict do aluno student_id e remove 
    ele da lista todo-sutdent-id-list na base de dados.
    
    A função também roda close_evaluation e fecha a avaliação caso a lista todo-student-id-list esteja vazia

    :parâmetro student_id: referencia inteira do id do estudante avaliador
    :parâmetro answer_dict: dicionario das respostas do estudante avaliador, aonde a key é o id do avaliado,
    e o valor uma array com as notas da pergunta

    """
    validate_answer_dict(student_id, answer_dict)

    student = student_connection.get_student_by_id(student_id)
    evaluation_list = get_evaluation_by_group_id(student['group-id'])

    evaluation = [evaluation for evaluation in evaluation_list if evaluation['id'] == evaluation_id][0]

    evaluation['todo-student-id-list'].remove(student['id'])
    evaluation['finish-student-id-list'].append(student['id'])
    evaluation['answer-dict'][student['id']] = answer_dict

    if(close_evaluation(evaluation)):
        return

    evaluation_list = get_evaluation_list()
    evaluation_list = replace_on_list(evaluation_list, 'id', evaluation)

    controller.overwrite_data(key, evaluation_list)


def create_evaluation(new_evaluation_dict):
    """
    Gera uma avaliação nova para um grupo no banco de dados mockado, retornando o id da recem gerada avaliação

    :parâmetro new_evaluation_dict: um dicionario aonde o atributo group-id se refere ao id do grupo que pertence a avaliação 
    :return: id da avaliação criada
    """

    evaluation_list = get_evaluation_list()

    evaluation_id = controller.get_last_id(key) + 1

    student_list = group_connection.get_group_student_list(new_evaluation_dict['group-id'])
    student_id_list = [student['id'] for student in student_list]

    evaluation_dict = {
        'id': evaluation_id,
        'group-id': new_evaluation_dict['group-id'],
        'sprint': new_evaluation_dict['sprint'],
        'finish-student-id-list': [],
        'todo-student-id-list': student_id_list,
        'status': 'todo',
        'answer-dict': {},
    }

    evaluation_list.append(evaluation_dict)
    controller.overwrite_data(key, evaluation_list)

    return evaluation_id


def resolve_evaluation(evaluation_dict):
    """
    Transforma o inteiro group-id em um dict de grupo, e a array de inteiros todo-student-id-list
    em uma array de dict de estudantes.

    :parâmetro evaluation_dict: dicionario a ser convertido
    :return: dicionario convertido
    """
    group = group_connection.resolve_group_by_id(evaluation_dict['group-id'])
    del evaluation_dict['group-id']
    evaluation_dict['group'] = group
    
    todo_student_list = []

    for student_id in evaluation_dict['todo-student-id-list']:
        student = student_connection.resolve_student_by_id(student_id)
        todo_student_list.append(student)

    del evaluation_dict['todo-student-id-list']
    evaluation_dict['todo-student-list'] = todo_student_list

    return evaluation_dict

def resolve_evaluation_by_id(evaluation_id):
    """
    Transforma o inteiro group-id em um dict de grupo, e a array de inteiros todo-student-id-list
    em uma array de dict de estudantes.

    :parâmetro evaluation_id: id da avaliação a ser convertido
    :return: dicionario convertido
    """
    return resolve_evaluation(get_evaluation_by_id(evaluation_id))