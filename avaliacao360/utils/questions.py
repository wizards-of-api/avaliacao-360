import PySimpleGUI as sg


list_students = ['João', 'Maria', 'Clara', 'Ana', 'Claudio', 'Leandro']

list_questions = [
    'se comunica de forma clara e objetiva.',
    'faz contribuições regulares pro projeto.',
    'consegue receber críticas.',
    'entende como o projeto funciona.',
    'realizou as entregas no prazo.',
    'tem afinidade com autogestão.'
]

list_answers = []

while True:
    for student in list_students:
        for question in list_questions:
            layout = [
                [sg.Text(f'{student} {question}')],
                [
                    sg.Button('Discordo totalmente',
                            s=(10, 5)),
                    sg.Button('Discordo parcialmente',
                            s=(10, 5)),
                    sg.Button('Neutro',  s=(10, 5)),
                    sg.Button('Concordo parcialmente',  s=(10, 5)),
                    sg.Button('Concordo totalmente',  s=(10, 5)),
                ]
            ]
            window = sg.Window('Questionário', layout)
            event, values = window.read()
            print(event,values)

            if event == 'Discordo totalmente':
                list_answers.append(1)
            elif event == 'Discordo parcialmente':
                list_answers.append(2)
            elif event == 'Neutro':
                list_answers.append(3)
            elif event == 'Concordo parcialmente':
                list_answers.append(4)
            elif event =='Concordo totalmente':
                list_answers.append(5)
    
        print(f'Notas do aluno {student}: {list_answers}')
        list_answers = []
    break
    
    