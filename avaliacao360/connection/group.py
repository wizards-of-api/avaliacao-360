from utils.filters import filter_by_key
import connection.controller as controller
import connection.class_room as class_room_connection
import connection.student as student_connection

key = 'group-list'

def get_group_list():
    """Retorna a lista de grupos."""
    return controller.get_data()[key]
    
def get_group_by_id(id):
    """Retorna o grupo com o ID especificado."""
    return filter_by_key(get_group_list(), 'id', id)

def get_group_by_name(name):
    """Retorna o grupo com o nome especificado."""
    return filter_by_key(get_group_list(), 'name', name)

def get_group_student_list(id):
    """Retorna a lista de estudantes pertencentes ao grupo com o ID especificado."""
    student_list = student_connection.get_student_list()
    return [student for student in student_list if student['group-id'] == id]

def create_group(new_group_dict):
    """Cria um novo grupo com as informações fornecidas em new_group_dict."""
    group_list = get_group_list()
    
    id = controller.get_last_id(key) + 1

    group_dict = {
        'id': id,
        'class-room-id': new_group_dict['class-room-id'],
        'name': new_group_dict['name'],
    }

    group_list.append(group_dict)
    controller.overwrite_data(key, group_list)

    return id

def resolve_group(group_dict):
    class_room = class_room_connection.get_class_room_by_id(group_dict['class-room-id'])
    del group_dict['class-room-id']
    group_dict['class-room'] = class_room
    return group_dict

def resolve_group_by_id(group_id):
    return resolve_group(get_group_by_id(group_id))