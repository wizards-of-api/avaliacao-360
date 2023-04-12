import app
import PySimpleGUI as sg
import interface.student as interface_student 
import interface.adm as interface_adm

def create_window():
    layout = [[sg.Text('Login!')],
        [sg.Text('Usuário: ', size = (6,0)), sg.InputText(size = (20,0), key='input')],
        [sg.Text('Senha: ', size = (6,0)), sg.InputText(size = (20,0))]
        [sg.Text('\n')],
        [sg.Button('Login'), sg.Button('Cancelar')]
        ]

    return sg.Window('Avaliação 360 - Login', layout, element_justification = 'c')

def event_handler(event, values):
    if event == 'Cancelar':
        app.close()
    elif event == 'Login':
        input_text_value = values['input']
        if input_text_value =='aluno':
            app.change_interface(interface_student.create_window(), interface_student.event_handler)
        elif input_text_value =='adm':
            app.change_interface(interface_adm.create_window(), interface_adm.event_handler)
        else: 
            app.pop_up('Não possui Login')
