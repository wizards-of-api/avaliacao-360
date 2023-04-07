import PySimpleGUI as sg
import app
#import interface.student as interface_student


#change to mockup student list
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

#change window theme
sg.theme('DarkAmber')

while True:
    for student in list_students:
        for question in list_questions:
            layout = [
                [sg.T(f'{student} {question}')],
                [
                    sg.B('Discordo totalmente', s=(10, 3)),
                    sg.B('Discordo parcialmente', s=(10, 3)),
                    sg.B('Neutro',  s=(10, 3)),
                    sg.B('Concordo parcialmente',  s=(10, 3)),
                    sg.B('Concordo totalmente',  s=(10, 3)),
                ],
                [sg.B('Voltar', s=(59, 0))]
            ]
            window = sg.Window(
                f'Questionário - {student}', layout,
                element_justification = 'c', finalize = True)
            event, values = window.read()
            window.hide()

            # testing events to give grades for the student
            if event == 'Discordo totalmente':
                list_answers.append(1)
            elif event == 'Discordo parcialmente':
                list_answers.append(2)
            elif event == 'Neutro':
                list_answers.append(3)
            elif event == 'Concordo parcialmente':
                list_answers.append(4)
            elif event == 'Concordo totalmente':
                list_answers.append(5)
            elif event == 'Voltar':
                pass#app.change_interface(interface_student) 

            #add close function from app.py
            elif event == sg.WIN_CLOSED:
                app.close()

        #getting students grades in a list one by one
        print(f'\nNotas do aluno {student}: {list_answers}')
        list_answers = []
    break

