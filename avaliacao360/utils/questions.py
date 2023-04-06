import PySimpleGUI as sg


list_classmates = ['João', 'Maria', 'Clara', 'Ana', 'Claudio', 'Leandro']

list_questions = [
    'se comunica de forma clara e objetiva.',
    'faz contribuições regulares pro projeto.',
    'consegue receber críticas.',
    'entende como o projeto funciona.',
    'realizou as entregas no prazo.',
    'tem afinidade com autogestão.'
]

list_answers = []


for question in list_questions:
    for classmate in list_classmates:
        layout = [
            [sg.Text(f'{classmate} {question}')],
            [
                sg.Button('Discordo totalmente',
                          size=(10, 5)),
                sg.Button('Discordo parcialmente',
                          size=(10, 5)),
                sg.Button('Neutro',  size=(10, 5)),
                sg.Button('Concordo parcialmente',  size=(10, 5)),
                sg.Button('Concordo totalmente',  size=(10, 5)),
            ]
        ]
        window = sg.Window('Questionário', layout)
        event = window.read()
        