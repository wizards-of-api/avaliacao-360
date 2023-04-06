from utils.filters import filter_by_key
import connection.connection as connection

key = 'student-list'

def get_student_list():
    return connection.get_data()[key]
    
def get_student_by_id(id):
    return filter_by_key(get_student_list(), 'id', id)

def get_student_by_name(name):
    return filter_by_key(get_student_list(), 'name', name)

def create_student(new_student_dict):
    student_list = get_student_list()

    id = connection.get_last_id(key) + 1

    student_dict = {
        'id': id,
        'group-id': new_student_dict['group-id'],
        'name': new_student_dict['name'],
    }

    student_list.append(student_dict)
    connection.overwirte_data(key, student_list)
    
    return id
