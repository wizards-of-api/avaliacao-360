from reset_mock_db import reset
import avaliacao360.connection.evaluation as evaluation_connection
import avaliacao360.connection.student as student_connection

reset()

evaluation_connection.request_evaluation()

maria_id = student_connection.get_student_by_name('Maria')[0]['id']
joao_id = student_connection.get_student_by_name('João')[0]['id']

maria_eval_id = student_connection.get_student_evaluation_by_id(maria_id)[0]['id']
joao_eval_id = student_connection.get_student_evaluation_by_id(joao_id)[0]['id']

evaluation_connection.answer_evaluation(1, maria_eval_id, { 1: [2, 5, 3, 3, 3, 4], 2: [1, 1, 1, 1, 1, 1] })
evaluation_connection.answer_evaluation(2, joao_eval_id, { 1: [2, 5, 3, 3, 3, 4], 2: [1, 1, 1, 1, 1, 1] })

