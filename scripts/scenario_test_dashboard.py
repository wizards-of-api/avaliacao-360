import sys, os
import random

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
    group_super_id = group.create_group({'class-room-id': room_b_id, 'name': 'Grupo Super'})

    ana_id = student.create_student({'group-id-list': [group_mega_id, group_ultra_id], 'name': 'Ana'})
    login.create_user({'username': 'ana', 'password': '12345678', 'student-id': ana_id})
    paulo_id = student.create_student({'group-id-list': [group_mega_id, group_ultra_id], 'name': 'Paulo'})
    login.create_user({'username': 'paulo', 'password': '12345678', 'student-id': paulo_id})

    luana_id = student.create_student({'group-id-list': [group_super_id], 'name': 'Luana'})
    login.create_user({'username': 'luana', 'password': '12345678', 'student-id': luana_id})
    gabriel_id = student.create_student({'group-id-list': [group_super_id], 'name': 'Gabriel'})
    login.create_user({'username': 'gabriel', 'password': '12345678', 'student-id': gabriel_id})


    eval_mega_1 = evaluation.create_evaluation({'group-id': group_mega_id, 'sprint': 1})
    eval_mega_2 = evaluation.create_evaluation({'group-id': group_mega_id, 'sprint': 2})
    eval_ultra_1 = evaluation.create_evaluation({'group-id': group_ultra_id, 'sprint': 1})
    eval_super_1 = evaluation.create_evaluation({'group-id': group_super_id, 'sprint': 1})

    def random_answer_generator(id_list):
        def random_single():
            random_feedback_list = ['Não dá', 'Muito Ruim', 'Fala muito', 'Tem que melhorar', 'Faltou Aquilo', 'Lorem Ipsum', 'Nem sei', 'Deu vontade', 'Hmmmm pensa muito']
            value = random.randint(1,5)
            feedback = None
            if value < 3:
                feedback = random.choice(random_feedback_list)
            return { 'value': value, 'feedback': feedback }

        answer_dict = {}
        for evaluated in id_list:
            answer_dict[evaluated] = [random_single(), random_single(), random_single(), random_single(), random_single(), random_single()]

        return answer_dict
    
    
    id_list_1 = [ana_id, paulo_id]
    id_list_2 = [luana_id, gabriel_id]

    evaluation.answer_evaluation(ana_id, eval_mega_1, random_answer_generator(id_list_1))
    evaluation.answer_evaluation(ana_id, eval_mega_2, random_answer_generator(id_list_1))
    evaluation.answer_evaluation(ana_id, eval_ultra_1, random_answer_generator(id_list_1))
    evaluation.answer_evaluation(paulo_id, eval_mega_1, random_answer_generator(id_list_1))
    evaluation.answer_evaluation(paulo_id, eval_mega_2, random_answer_generator(id_list_1))
    evaluation.answer_evaluation(paulo_id, eval_ultra_1, random_answer_generator(id_list_1))
    evaluation.answer_evaluation(luana_id, eval_super_1, random_answer_generator(id_list_2))
    evaluation.answer_evaluation(gabriel_id, eval_super_1, random_answer_generator(id_list_2))


if __name__ == '__main__':
    reset()