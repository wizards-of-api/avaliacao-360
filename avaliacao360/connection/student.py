from utils.filters import filter_by_key
import connection.controller as controller
import connection.group as group_connection

key = 'student-list'

def get_student_list():
    return controller.get_data()[key]
    
def get_student_by_id(id):
    return filter_by_key(get_student_list(), 'id', id)

def get_student_by_name(name):
    return filter_by_key(get_student_list(), 'name', name)

def create_student(new_student_dict):
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

def resolve_student(student_dict):
    group = group_connection.resolve_group_by_id(student_dict['group-id'])
    del student_dict['group-id']
    student_dict['group'] = group
    return student_dict

def resolve_student_by_id(student_id):
    return resolve_student(get_student_by_id(student_id))