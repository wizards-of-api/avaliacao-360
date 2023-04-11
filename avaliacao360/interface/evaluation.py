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
    evaluation = {}
    evaluated_index = 0 

    print(student_list)
    
    def event_handler(event, values):
        nonlocal evaluation, evaluated_index
        if event == 'Enviar':
            result = []
            #para cada tela capturar a combinacao de resultados
            #iterar um contador para nomear o botao de radio capturado
            for counter in range(len(question_list)):
                if values['1'+'Answer'+ str(counter)]:
                    result.append(1)
                if values['2'+'Answer'+ str(counter)]:
                    result.append(2)
                if values['3'+'Answer'+ str(counter)]:
                    result.append(3)
                if values['4'+'Answer'+ str(counter)]:
                    result.append(4)
                if values['5'+'Answer'+ str(counter)]:
                    result.append(5)

            evaluation[student_list[evaluated_index]['name']] = result

            if evaluated_index < len(student_list) - 1:
                evaluated_index += 1
                evaluate()
            else:
                print(evaluation)
                app.close()
                

    def create_question_layout(question_list):
        column_list = []
        counter = 0

        for question in question_list:
    
            group_id = 'Answer' + str(counter)

            column_list.append([sg.Text(student_list[evaluated_index]['name'] +' '+ question)])
            column_list.append(
                [sg.Radio('Discordo totalmente', group_id, key = '1' + str(group_id)),
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
