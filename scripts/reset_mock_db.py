import sys, os
from datetime import datetime, timedelta

sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('./avaliacao360'))

from avaliacao360.connection import controller
from avaliacao360.connection import class_room
from avaliacao360.connection import group
from avaliacao360.connection import student

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
    student.create_student({'group-id': group_mega_id, 'name': 'João'})

    student.create_student({'group-id': group_ultra_id, 'name': 'Ana'})
    student.create_student({'group-id': group_ultra_id, 'name': 'Gabriel'})

    student.create_student({'group-id': group_blast_id, 'name': 'Roberta'})
    student.create_student({'group-id': group_blast_id, 'name': 'Lucas'})

    student.create_student({'group-id': group_super_id, 'name': 'Luana'})
    student.create_student({'group-id': group_super_id, 'name': 'Davi'})

if __name__ == '__main__':
    reset()