import app
import PySimpleGUI as sg
import interface.student_general as interface_student_general 
import interface.adm as interface_adm
import connection.login as connection_login
import connection.student_dash as student

def create_window():
    layout = [[sg.Text('Login!')],
       [sg.Text('Usuário: ', size = (6,0)), sg.InputText(size = (20,0), key='username')],
        [sg.Text('Senha: ', size = (6,0)), sg.InputText(size = (20,0), key = 'password', password_char='*')],
        [sg.Text('\n')],
        [sg.Button('Login'), sg.Button('Cancel')]
        ]
    
    return sg.Window('Avaliação 360 - Login', layout, element_justification = 'c')

def event_handler(event, values):
    print(event)
    username = values['username']
    password = values['password']
    if event == 'Cancel':
        app.close()
    elif event == 'Login':
        if not username.strip() or not password.strip():
            app.pop_up('Por favor, preencha o nome e a senha!')
        elif username =='adm' and password =='adm':
            app.change_interface(interface_adm.create_window(), interface_adm.event_handler)
        elif connection_login.check_username(username) and not connection_login.check_password(password):
            app.pop_up('Senha incorreta!')
        elif connection_login.check_login(username, password):
            student_id = connection_login.check_login(username, password)
            app.change_interface(interface_student_general.create_window(student_id), interface_student_general.event_handler)
        else:
            app.pop_up('Não possui Login')