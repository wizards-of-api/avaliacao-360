from utils.filters import filter_by_key
import connection.connection as connection
import connection.group as group_connection
import connection.student as student_connection

key = 'class-room-list'

def get_class_room_list():
    return connection.get_data()[key]
    
def get_class_room_by_id(id):
    return filter_by_key(get_class_room_list(), 'id', id)

def get_class_room_by_name(name):
    return filter_by_key(get_class_room_list(), 'name', name)

def get_class_room_group_list(id):
    group_list = group_connection.get_group_list()
    return [group for group in group_list if group['class-room-id'] == id]

def get_class_room_student_list(id):
    group_list = get_class_room_group_list(id)
    student_list = []
    for group in group_list:
        print(group)
        student_list += group_connection.get_group_student_list(group['id'])
    return student_list

def create_class_room(new_class_room_dict):
    class_room_list = get_class_room_list()

    id = connection.get_last_id(key) + 1

    class_room_dict = {
        'id': id,
        'name': new_class_room_dict['name'],
    }

    class_room_list.append(class_room_dict)
    connection.overwirte_data(key, class_room_list)
    return id