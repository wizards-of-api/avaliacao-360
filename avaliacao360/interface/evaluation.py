import PySimpleGUI as sg

import app


question_list = [
    'se comunica de forma clara e objetiva.',
    'faz contribuições regulares pro projeto.',
    'consegue receber críticas.',
    'entende como o projeto funciona.',
    'realizou as entregas no prazo.',
    'tem afinidade com autogestão.'
]

def create_evaluation(student_list):
    result = []
    student_index = 0 
    
    def event_handler(event, _):
        nonlocal result, student_index
        if event == 'Enviar':
            if student_index < len(student_list) - 1:
                student_index += 1
                evaluate()
            else:
                app.close()
                

    def create_question_layout(question_list):
        column_list = []
        counter = 0

        for question in question_list:
    
            group_id = 'Answer' + str(counter)

            column_list.append([sg.Text(student_list[student_index]['name'] +' '+ question)])
            column_list.append(
                [sg.Radio('Discordo totalmente', group_id, '1' + str(group_id)),
                sg.Radio('Discordo', group_id, key = '2' + str(group_id)),
                sg.Radio('Neutro', group_id, key = '3' + str(group_id)),
                sg.Radio('Concordo', group_id, key = '4' + str(group_id)), 
                sg.Radio('Concordo totalmente', group_id, key = '5' + str(group_id))]
            )
            counter += 1

        column_list.append([sg.Button('Enviar', size = (6,0))])

        return column_list

    def evaluate():
        layout = create_question_layout(question_list)
        window = sg.Window('Questionário' + student_list[0]['name'], layout, element_justification = 'c')
        app.change_interface(window, event_handler)

    evaluate()
