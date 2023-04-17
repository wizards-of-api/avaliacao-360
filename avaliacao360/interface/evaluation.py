import app
import PySimpleGUI as sg
import interface.login as interface_login
from connection.evaluation import answer_evaluation
from connection.student import get_student_evaluation_by_id, get_student_by_id

question_list = [
    'se comunica de forma clara e objetiva.',
    'faz contribuições regulares pro projeto.',
    'consegue receber críticas.',
    'entende como o projeto funciona.',
    'realizou as entregas no prazo.',
    'tem afinidade com autogestão.'
]

def create_evaluation(student_id, student_list):
    evaluation = {}
    evaluated_index = 0
    
    def run_trough_questions(callback):
        for index, question in enumerate(question_list):
            group_id = 'answer_' + str(index)
            callback(group_id, question)

    def event_handler(event, values):
        nonlocal evaluation, evaluated_index
        if event == 'Enviar':
            result = []
            #para cada tela capturar a combinacao de resultados
            #iterar um contador para nomear o botao de radio capturado
            def callback(group_id, _):
                if values['1_' + group_id]:
                    result.append(1)
                if values['2_' + group_id]:
                    result.append(2)
                if values['3_' + group_id]:
                    result.append(3)
                if values['4_' + group_id]:
                    result.append(4)
                if values['5_' + group_id]:
                    result.append(5)

            #mock dos estudantes
            def mock_students():
                evaluation_id = get_student_evaluation_by_id(student_id)[0]['id']
                answer_evaluation(student_id, evaluation_id, evaluation)

            run_trough_questions(callback)

            evaluation[student_list[evaluated_index]['id']] = result

            if evaluated_index < len(student_list) - 1:
                evaluated_index += 1
                evaluate()
            else:
                mock_students()
                app.close()

    def create_question_layout():
        column_list = []

        def callback(group_id, question):
            column_list.append([sg.Text(student_list[evaluated_index]['name'] +' '+ question)])
            column_list.append(
                [sg.Radio('Discordo totalmente', group_id, key = '1_' + str(group_id)),
                sg.Radio('Discordo', group_id, key = '2_' + str(group_id)),
                sg.Radio('Neutro', group_id, default = True, key = '3_' + str(group_id)),
                sg.Radio('Concordo', group_id, key = '4_' + str(group_id)), 
                sg.Radio('Concordo totalmente', group_id, key = '5_' + str(group_id))]
            )

        run_trough_questions(callback)

        column_list.append([sg.Button('Enviar', size = (6,0))])

        return column_list

    def evaluate():
        layout = create_question_layout()
        window = sg.Window('Avaliação 360 - Questionário ' + get_student_by_id(student_id)['name'], layout, element_justification = 'c')
        app.change_interface(window, event_handler)

    evaluate()