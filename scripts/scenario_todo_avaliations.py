from reset_mock_db import reset
import avaliacao360.connection.class_room as room_connection
import avaliacao360.connection.evaluation as evaluation_connection
import avaliacao360.connection.student as student_connection

reset()

room_connection.add_sprint(1, {'start': '03/04/2023', 'end': '14/04/2023'})
room_connection.add_sprint(1, {'start': '15/04/2023', 'end': '26/04/2023'})
room_connection.add_sprint(1, {'start': '27/04/2023', 'end': '04/05/2023'})

evaluation_connection.create_evaluation({'group-id': 1, 'sprint': 1})
evaluation_connection.create_evaluation({'group-id': 1, 'sprint': 2})

maria_id = student_connection.get_student_by_name('Maria')[0]['id']
joao_id = student_connection.get_student_by_name('João')[0]['id']

maria_eval_id = student_connection.get_student_evaluation_by_id(maria_id)[0]['id']
joao_eval_id = student_connection.get_student_evaluation_by_id(joao_id)[0]['id']

evaluation_connection.answer_evaluation(1, maria_eval_id, { 1: [2, 5, 3, 3, 3, 4], 2: [3, 5, 4, 4, 1, 2] })
evaluation_connection.answer_evaluation(2, joao_eval_id, { 1: [5, 2, 2, 2, 3, 1], 2: [4, 4, 2, 5, 4, 2] })

