from utils.filters import filter_by_key, replace_on_list
import connection.controller as controller
import connection.group as group_connection
import connection.student as student_connection

key = 'evaluation-list'

def get_evaluation_list():
    return controller.get_data()[key]


def get_evaluation_by_id(id):
    return filter_by_key(get_evaluation_list(), 'id', id)

def get_evaluation_by_group_id(group_id):
    return filter_by_key(get_evaluation_list(), 'group-id', group_id)

def request_evaluation():
    group_list = group_connection.get_group_list()

    for group in group_list:
        create_evaluation({'group-id': group['id']})

def close_evaluation(evaluation):
    if(len(evaluation['todo-student-id-list']) != 0):
        return False
    
    evaluation['status'] = 'done'
    del evaluation['todo-student-id-list']

    evaluation_list = get_evaluation_list()
    evaluation_list = replace_on_list(evaluation_list, 'id', evaluation)

    controller.overwrite_data(key, evaluation_list)

    return True
    

# Adicionar validação de resposta
def answer_evaluation(student_id, answer_dict):
    student = student_connection.get_student_by_id(student_id)
    evaluation = get_evaluation_by_group_id(student['group-id'])


    evaluation['todo-student-id-list'].remove(student['id'])
    evaluation['answer-dict'][student['id']] = answer_dict

    if(close_evaluation(evaluation)):
        return

    evaluation_list = get_evaluation_list()
    evaluation_list = replace_on_list(evaluation_list, 'id', evaluation)

    controller.overwrite_data(key, evaluation_list)


def create_evaluation(new_evaluation_dict):
    evaluation_list = get_evaluation_list()

    id = controller.get_last_id(key) + 1

    student_list = group_connection.get_group_student_list(new_evaluation_dict['group-id'])
    student_id_list = [student['id'] for student in student_list]

    evaluation_dict = {
        'id': id,
        'group-id': new_evaluation_dict['group-id'],
        'todo-student-id-list': student_id_list,
        'status': 'todo',
        'answer-dict': {},
    }

    evaluation_list.append(evaluation_dict)
    controller.overwrite_data(key, evaluation_list)

    return id

def resolve_evaluation(evaluation_dict):
    print(evaluation_dict['group-id'])
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
    return resolve_evaluation(get_evaluation_by_id(evaluation_id))