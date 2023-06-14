import app
import PySimpleGUI as sg
import interface.login as interface_login
from connection.evaluation import answer_evaluation
import connection.evaluation as connection_evaluation
from connection.student import get_student_by_id
from config import question_list
import connection.group as connection_group
from config import LABEL_FONT

def create_evaluation(student_id, evaluation_id):
    group_id = connection_evaluation.get_evaluation_by_id(evaluation_id)[0]['group-id']
    student_list = connection_group.get_group_student_list(group_id)
    evaluation = {}
    evaluated_index = 0
    
    def run_trough_questions(callback):
        """Cria um indice dinamico para os grupos de resposta de cada
        pergunta."""

        for index, question in enumerate(question_list):
            group_id = 'answer_' + str(index)
            callback(group_id, question)

    def event_handler(event, values):
        """Recebe os eventos e valores capturados na tela quando o botão
        Enviar é apertado. Se o valor de algum radio for 2 ou 1, captura
        um comentário de justificativa."""

        nonlocal evaluation, evaluated_index
        if event == 'Enviar':
            result = []
            
            def callback(group_id, _):
                evaluated = student_list[evaluated_index]['name']
                evaluater = get_student_by_id(student_id)['name']

                if values['1_' + group_id] and evaluated != evaluater:
                    feedback = None
                    while not feedback or feedback == "":
                        feedback = sg.popup_get_text(
                            question_list[int(group_id[-1])]+
                            "\nJustifique sua resposta: ",
                            title='Justificativa', font=LABEL_FONT
                            )
                    result.append({'value':1, 'feedback':feedback})

                elif values['1_' + group_id] and evaluated == evaluater:
                    result.append({'value':1, 'feedback':None})

                if values['2_' + group_id] and evaluated != evaluater:
                    feedback = None
                    while not feedback or feedback == "":
                        feedback = sg.popup_get_text(
                            question_list[int(group_id[-1])]+
                            "\nJustifique sua resposta: ",
                            title='Justificativa', font=LABEL_FONT
                            )
                    result.append({'value':2, 'feedback':feedback})
                    
                elif values['1_' + group_id] and evaluated == evaluater:
                    result.append({'value':2, 'feedback':None})

                if values['3_' + group_id]:
                    result.append({'value':3, 'feedback':None})
                if values['4_' + group_id]:
                    result.append({'value':4, 'feedback':None})
                if values['5_' + group_id]:
                    result.append({'value':5, 'feedback':None})

            
            def mock_students():
                """Armazena o aluno e suas respectivas avaliacoes em um dicionario no mock"""
                answer_evaluation(student_id, evaluation_id, evaluation)

            run_trough_questions(callback)

            evaluation[student_list[evaluated_index]['id']] = result

            if evaluated_index < len(student_list) - 1:
                evaluated_index += 1
                evaluate()
            else:
                mock_students()
                app.change_interface(interface_login.create_window(), interface_login.event_handler)

    def create_question_layout():
        """Cria a interface, utilizando as funções callback e 
        run_through_questions."""

        column_list = []

        def callback(group_id, question):
            """Cria as perguntas e os botões de resposta usando o indice dinamico
            criado anteriormente."""

            column_list.append([sg.Text(student_list[evaluated_index]['name'] +' '+ question, font=LABEL_FONT)])
            column_list.append(
                [sg.Radio('Discordo totalmente', group_id, key = '1_' + str(group_id), font=LABEL_FONT),
                sg.Radio('Discordo', group_id, key = '2_' + str(group_id), font=LABEL_FONT),
                sg.Radio('Neutro', group_id, default = True, key = '3_' + str(group_id), font=LABEL_FONT),
                sg.Radio('Concordo', group_id, key = '4_' + str(group_id), font=LABEL_FONT), 
                sg.Radio('Concordo totalmente', group_id, key = '5_' + str(group_id), font=LABEL_FONT)]
            )
            
            column_list.append([sg.Text("")])

        run_trough_questions(callback)

        column_list.append([sg.Button('Enviar', size = (6,0), font=LABEL_FONT)])

        return column_list

    def evaluate():
        """Inicializa o layout da avaliação e setta a 
        janela para capturar eventos com o arquivo app. """

        layout = create_question_layout()
        window = sg.Window('Avaliação 360 - Questionário ' + get_student_by_id(student_id)['name'], layout, element_justification = 'c')
        app.change_interface(window, event_handler)

    evaluate()