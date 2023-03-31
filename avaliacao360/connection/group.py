from utils.filters import filter_by_key
import connection.connection as connection
import connection.student as student_connection

key = 'group-list'

def get_group_list():
    return connection.get_data()[key]
    
def get_group_by_id(id):
    return filter_by_key(get_group_list(), 'id', id)

def get_group_by_name(name):
    return filter_by_key(get_group_list(), 'name', name)

def get_group_student_list(id):
    student_list = student_connection.get_student_list()
    return [student for student in student_list if student['group-id'] == id]

def create_group(new_group_dict):
    group_list = get_group_list()
    
    id = connection.get_last_id(key) + 1

    group_dict = {
        'id': id,
        'class-room-id': new_group_dict['class-room-id'],
        'name': new_group_dict['name'],
    }

    group_list.append(group_dict)
    connection.overwirte_data(key, group_list)

    return id
