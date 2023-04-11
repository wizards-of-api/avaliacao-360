import app
import PySimpleGUI as sg
import interface.student as interface_student 
import interface.adm as interface_adm

def create_window():
    layout = [[sg.Text('Login!')],
        [sg.Text('User: '), sg.InputText(key='input')],
        [sg.Text('Password: '), sg.InputText()],
        [sg.Button('Login'), sg.Button('Cancel')]
        ]

    return sg.Window('Window Title', layout)

def event_handler(event, values):
    if event == 'Cancel':
        app.close()
    elif event == 'Login':
        input_text_value = values['input']
        if input_text_value =='aluno':
            app.change_interface(interface_student.create_window(), interface_student.event_handler)
        elif input_text_value =='adm':
            app.change_interface(interface_adm.create_window(), interface_adm.event_handler)
        else: 
            app.pop_up('Não possui Login')
