import config
import connection.class_room as connect_room
import connection.group as connect_group
import connection.evaluation as connect_eval
from utils.filters import filter_by_key

def generate_average_group_data(room_id):
    ret_dict = {}
    group_list = connect_room.get_class_room_group_list(room_id)
    ret_dict['group-list'] = [group['name'] for group in group_list]

    data = []
    
    for group in group_list:
        eval_list = connect_eval.get_evaluation_by_group_id(group['id'])
        print(group['class-room-id'])
        group_data = [[] for _ in config.competence_list]

        for evaluation in eval_list:
            for answer_dict in evaluation['answer-dict'].values():
                for values_list in answer_dict.values():
                    i = 0
                    for competance_result in values_list:
                        group_data[i].append(competance_result['value'])
                        i += 1

        if len(group_list) > 0:
            group_data = [sum(value_list) / len(value_list) for value_list in group_data]
        else:
            group_data = [0 for _ in group_data]
        
        data.append(group_data)
    ret_dict['data'] = data
    return ret_dict

def generate_average_group_data_by_sprint(room_id):
    ret_dict = {}
    room = connect_room.get_class_room_by_id(room_id)
    sprint_arr = [*range(1, len(room['sprint_list']) + 1)]
    ret_dict['sprint-list'] = ['Sprint ' + str(i) for i in sprint_arr]
    data = []
    
    for sprint in sprint_arr:
        eval_list = filter_by_key(connect_eval.get_evaluation_list(), 'sprint', sprint)
        group_data = [[] for _ in config.competence_list]

        for evaluation in eval_list:
            group = connect_group.get_group_by_id(evaluation['group-id'])
            if group['class-room-id'] != room_id: continue
            for answer_dict in evaluation['answer-dict'].values():
                for values_list in answer_dict.values():
                    i = 0
                    for competance_result in values_list:
                        group_data[i].append(competance_result['value'])
                        i += 1

        if len(sprint_arr) > 0:
            group_data = [sum(value_list) / len(value_list) for value_list in group_data]
        else:
            group_data = [0 for _ in group_data]
        
        data.append(group_data)
    ret_dict['data'] = data
    return ret_dict

def generate_average_student_data(group_id):
    ret_dict = {}
    student_list = connect_group.get_group_student_list(group_id)
    ret_dict['student-list'] = [student['name'] for student in student_list]

    data = []
    
    for student in student_list:
        eval_list = connect_eval.get_evaluation_by_student_id(student['id'])
        eval_list = [evaluation for evaluation in eval_list if str(evaluation['group-id']) == str(group_id)]
        group_data = [[] for _ in config.competence_list]

        for evaluation in eval_list:
            for answer_dict in evaluation['answer-dict'].values():
                for eval_student_id, values_list in answer_dict.items():
                    if eval_student_id != str(student['id']): continue
                    i = 0
                    for competance_result in values_list:
                        group_data[i].append(competance_result['value'])
                        i += 1

        print(group_data)

        if len(student_list) > 0:
            group_data = [sum(value_list) / len(value_list) for value_list in group_data]
        else:
            group_data = [0 for _ in group_data]
        
        data.append(group_data)
    ret_dict['data'] = data
    return ret_dict

def generate_average_student_data_by_sprint(group_id):
    ret_dict = {}
    group = connect_group.get_group_by_id(group_id)
    room = connect_room.get_class_room_by_id(group['class-room-id'])
    sprint_arr = [*range(1, len(room['sprint_list']) + 1)]
    ret_dict['sprint-list'] = ['Sprint ' + str(i) for i in sprint_arr]
    data = []
    
    for sprint in sprint_arr:
        eval_list = filter_by_key(connect_eval.get_evaluation_list(), 'sprint', sprint)
        group_data = [[] for _ in config.competence_list]

        for evaluation in eval_list:
            if evaluation['group-id'] != group_id: continue
            for answer_dict in evaluation['answer-dict'].values():
                for values_list in answer_dict.values():
                    i = 0
                    for competance_result in values_list:
                        group_data[i].append(competance_result['value'])
                        i += 1

        if len(sprint_arr) > 0:
            group_data = [sum(value_list) / len(value_list) for value_list in group_data]
        else:
            group_data = [0 for _ in group_data]
        
        data.append(group_data)
    ret_dict['data'] = data
    return ret_dict