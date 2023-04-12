from reset_mock_db import reset
import avaliacao360.connection.evaluation as evaluation_connection

reset()

evaluation_connection.request_evaluation()

evaluation_connection.answer_evaluation(1, { 1: [2, 5, 3, 3, 3, 4], 2: [1, 1, 1, 1, 1, 1] })
evaluation_connection.answer_evaluation(2, { 1: [2, 5, 3, 3, 3, 4], 2: [1, 1, 1, 1, 1, 1] })