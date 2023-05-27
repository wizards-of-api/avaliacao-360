import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'avaliacao360')))

from avaliacao360.connection import controller
from avaliacao360.connection import class_room
from avaliacao360.connection import group
from avaliacao360.connection import student
from avaliacao360.connection import login
from avaliacao360.connection import evaluation

date_format = '%d/%m/%Y'

def reset():
    controller.create_db()
    controller.clear_db()

    room_a_id = class_room.create_class_room({'name': 'Sala A'})
    room_b_id = class_room.create_class_room({'name': 'Sala B'})

    sprint_1_object = {'start': '01/01/2023', 'end': '28/01/2023'}
    sprint_2_object = {'start': '01/02/2023', 'end': '28/02/2023'}

    class_room.add_sprint(room_a_id, sprint_1_object)
    class_room.add_sprint(room_a_id, sprint_2_object)
    
    class_room.add_sprint(room_b_id, sprint_1_object)

    group_mega_id = group.create_group({'class-room-id': room_a_id, 'name': 'Grupo Mega'})
    group_ultra_id = group.create_group({'class-room-id': room_b_id, 'name': 'Grupo Ultra'})

    ana_id = student.create_student({'group-id-list': [group_mega_id, group_ultra_id], 'name': 'Ana'})
    login.create_user({'username': 'ana', 'password': '12345678', 'student-id': ana_id})
    paulo_id = student.create_student({'group-id-list': [group_mega_id, group_ultra_id], 'name': 'Paulo'})
    login.create_user({'username': 'paulo', 'password': '12345678', 'student-id': paulo_id})

    eval_mega_1 = evaluation.create_evaluation({'group-id': group_mega_id, 'sprint': 1})
    eval_mega_2 = evaluation.create_evaluation({'group-id': group_mega_id, 'sprint': 2})
    eval_ultra_1 = evaluation.create_evaluation({'group-id': group_ultra_id, 'sprint': 1})

    ana_eval_1 = {
        ana_id: [
            {
                'value': 5,
                'feedback': None
            },
            {
                'value': 5,
                'feedback': None
            },
            {
                'value': 5,
                'feedback': None
            },
            {
                'value': 5,
                'feedback': None
            },
            {
                'value': 5,
                'feedback': None
            },
            {
                'value': 5,
                'feedback': None
            },
        ],
        paulo_id: [
            {
                'value': 1,
                'feedback': 'Não dá'
            },
            {
                'value': 1,
                'feedback': 'Não se esforça'
            },
            {
                'value': 1,
                'feedback': 'Muita ruim'
            },
            {
                'value': 1,
                'feedback': 'Tem que melhorar'
            },
            {
                'value': 1,
                'feedback': 'Faltou aquilo'
            },
            {
                'value': 1,
                'feedback': 'Lorem Ipsum'
            },
        ]
    }
    ana_eval_2 = {
        ana_id: [
            {
                'value': 4,
                'feedback': None
            },
            {
                'value': 3,
                'feedback': None
            },
            {
                'value': 4,
                'feedback': None
            },
            {
                'value': 3,
                'feedback': None
            },
            {
                'value': 4,
                'feedback': None
            },
            {
                'value': 3,
                'feedback': None
            },
        ],
        paulo_id: [
            {
                'value': 2,
                'feedback': 'Não dá'
            },
            {
                'value': 2,
                'feedback': 'Não se esforça'
            },
            {
                'value': 4,
                'feedback': None
            },
            {
                'value': 4,
                'feedback': None
            },
            {
                'value': 5,
                'feedback': None
            },
            {
                'value': 1,
                'feedback': 'Lorem Ipsum'
            },
        ]
    }
    ana_eval_3 = {
        ana_id: [
            {
                'value': 3,
                'feedback': None
            },
            {
                'value': 3,
                'feedback': None
            },
            {
                'value': 3,
                'feedback': None
            },
            {
                'value': 3,
                'feedback': None
            },
            {
                'value': 3,
                'feedback': None
            },
            {
                'value': 3,
                'feedback': None
            },
        ],
        paulo_id: [
            {
                'value': 5,
                'feedback': None
            },
            {
                'value': 4,
                'feedback': None
            },
            {
                'value': 5,
                'feedback': None
            },
            {
                'value': 4,
                'feedback': None
            },
            {
                'value': 5,
                'feedback': None
            },
            {
                'value': 4,
                'feedback': None
            },
        ]
    }

    paulo_eval = {
        paulo_id: [
            {
                'value': 5,
                'feedback': None
            },
            {
                'value': 5,
                'feedback': None
            },
            {
                'value': 5,
                'feedback': None
            },
            {
                'value': 5,
                'feedback': None
            },
            {
                'value': 5,
                'feedback': None
            },
            {
                'value': 5,
                'feedback': None
            },
        ],
        ana_id: [
            {
                'value': 3,
                'feedback': None
            },
            {
                'value': 4,
                'feedback': None
            },
            {
                'value': 3,
                'feedback': None
            },
            {
                'value': 5,
                'feedback': None
            },
            {
                'value': 3,
                'feedback': None
            },
            {
                'value': 4,
                'feedback': None
            },
        ]
    }

    evaluation.answer_evaluation(ana_id, eval_mega_1, ana_eval_1)
    evaluation.answer_evaluation(ana_id, eval_mega_2, ana_eval_2)
    evaluation.answer_evaluation(ana_id, eval_ultra_1, ana_eval_3)
    evaluation.answer_evaluation(paulo_id, eval_mega_1, paulo_eval)
    evaluation.answer_evaluation(paulo_id, eval_mega_2, paulo_eval)
    evaluation.answer_evaluation(paulo_id, eval_ultra_1, paulo_eval)


if __name__ == '__main__':
    reset()