import app
import PySimpleGUI as sg
import interface.student as interface_student 
import interface.adm as interface_adm
import connection.student as connection_student

def create_window():
    layout = [[sg.Text('Login!')],
        [sg.Text('User: '), sg.InputText(key='input')],
        [sg.Text('Password: '), sg.InputText()],
        [sg.Button('Login'), sg.Button('Cancel')]
        ]

    return sg.Window('Window Title', layout)

def event_handler(event, values):
    input_name = values['input']
    student_list = connection_student.get_student_by_name(input_name)

    if event == 'Cancel':
        app.close()
    elif event == 'Login':
        if student_list:
            app.change_interface(interface_student.create_window(input_name), interface_student.event_handler)
        elif input_name =='adm':
            app.change_interface(interface_adm.create_window(), interface_adm.event_handler, input_name  )
        else: 
            app.pop_up('Não possui Login')