from datetime import timedelta
from utils.date_functions import convert_date_str
import connection.evaluation as evaluation_connection
import connection.class_room as room_connection
import connection.group as group_connection

def close_evaluations(room_id, sprint):
    evaluation_list = evaluation_connection.get_evaluation_list()
    evaluation_list = [evaluation for evaluation in evaluation_list if evaluation['sprint'] == sprint]
    for evaluation in evaluation_list:
        group = group_connection.get_group_by_id(evaluation['group-id'])
        if group['class-room-id'] != room_id:
            continue
        if evaluation['status'] == 'done':
          continue
        evaluation_connection.force_close_evaluation(evaluation)

def init_evaluations(room, sprint):
    group_list = room_connection.get_class_room_group_list(room['id'])
    for group in group_list:
        evaluation_list = evaluation_connection.get_evaluation_by_group_id(group['id'])
        sprint_evaluation = [evaluation for evaluation in evaluation_list if evaluation['sprint'] == sprint]
        if len(sprint_evaluation) == 0:
            evaluation_connection.create_evaluation({'group-id': group['id'], 'sprint': sprint})

def check_sprint(room, date_now):
    sprint_list = room['sprint_list']
    for i, sprint in enumerate(sprint_list):
        sprint_index = i + 1
        sprint_end_date = convert_date_str(sprint['end'])
        eval_end_date = sprint_end_date + timedelta(days=5)
        
        if date_now <= sprint_end_date:
            continue

        init_evaluations(room, sprint_index)
        if date_now > eval_end_date:
            close_evaluations(room['id'], sprint_index)
            continue


def check_sprint_all(date_now):
    room_list = room_connection.get_class_room_list()
    for room in room_list:
        check_sprint(room, date_now)