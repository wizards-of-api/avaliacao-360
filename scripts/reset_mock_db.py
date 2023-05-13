import sys, os
from datetime import datetime, timedelta

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'avaliacao360')))

from avaliacao360.connection import controller
from avaliacao360.connection import class_room
from avaliacao360.connection import group
from avaliacao360.connection import student
from avaliacao360.connection import login

date_format = '%d/%m/%Y'

def reset():
    controller.create_db()
    controller.clear_db()

    room_a_id = class_room.create_class_room({'name': 'Sala A'})
    room_b_id = class_room.create_class_room({'name': 'Sala B'})

    sprint_end = datetime.today() - timedelta(days=1)
    sprint_start = sprint_end - timedelta(days=15)

    sprint_object = {'start': sprint_start.strftime(date_format), 'end': sprint_end.strftime(date_format)}

    class_room.add_sprint(room_a_id, sprint_object)
    class_room.add_sprint(room_b_id, sprint_object)

    group_mega_id = group.create_group({'class-room-id': room_a_id, 'name': 'Grupo Mega'})
    group_ultra_id = group.create_group({'class-room-id': room_a_id, 'name': 'Grupo Ultra'})

    group_blast_id = group.create_group({'class-room-id': room_b_id, 'name': 'Grupo Blast'})
    group_super_id = group.create_group({'class-room-id': room_b_id, 'name': 'Grupo Super'})

    student.create_student({'group-id': group_mega_id, 'name': 'Maria'})
    login.create_user({'username': 'maria', 'password': '12345678'})
    student.create_student({'group-id': group_mega_id, 'name': 'João'})
    login.create_user({'username': 'joao', 'password': '12345678'})

    student.create_student({'group-id': group_ultra_id, 'name': 'Ana'})
    login.create_user({'username': 'ana', 'password': '12345678'})
    student.create_student({'group-id': group_ultra_id, 'name': 'Gabriel'})
    login.create_user({'username': 'gabriel', 'password': '12345678'})

    student.create_student({'group-id': group_blast_id, 'name': 'Roberta'})
    login.create_user({'username': 'roberta', 'password': '12345678'})
    student.create_student({'group-id': group_blast_id, 'name': 'Lucas'})
    login.create_user({'username': 'lucas', 'password': '12345678'})

    student.create_student({'group-id': group_super_id, 'name': 'Luana'})
    login.create_user({'username': 'luana', 'password': '12345678'})
    student.create_student({'group-id': group_super_id, 'name': 'Davi'})
    login.create_user({'username': 'davi', 'password': '12345678'})

if __name__ == '__main__':
    reset()