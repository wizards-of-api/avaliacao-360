import app
import PySimpleGUI as sg
import interface.student as interface_student 
import interface.adm as interface_adm
import connection.student as connection_student

def create_window():
    layout = [[sg.Text('Login!')],
       [sg.Text('Usuário: ', size = (6,0)), sg.InputText(size = (20,0), key='input')],
        [sg.Text('Senha: ', size = (6,0)), sg.InputText(size = (20,0))],
        [sg.Text('\n')],
        [sg.Button('Login'), sg.Button('Cancel')]
        ]
    
    return sg.Window('Avaliação 360 - Login', layout, element_justification = 'c')

def event_handler(event, values):
    input_name = values['input']
    student_list = connection_student.get_student_by_name(input_name)

    if event == 'Cancel':
        app.close()
    elif event == 'Login':
        if student_list:
            app.change_interface(interface_student.create_window(input_name), interface_student.event_handler)
        elif input_name =='adm':
            app.change_interface(interface_adm.create_window(), interface_adm.event_handler)
        else: 
            app.pop_up('Não possui Login')