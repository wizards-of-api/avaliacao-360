import app
import PySimpleGUI as sg
import interface.student as interface_student 
import interface.adm as interface_adm
import interface.error as interface_error
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Login!')],
    [sg.Text('User: '), sg.InputText(key='input')],
    [sg.Text('Password: '), sg.InputText()],
    [sg.Button('Login'), sg.Button('Cancel')]
    ]

# Create the Window
window = sg.Window('Window Title', layout)

def event_handler(event, values):
    if event == 'Cancel': # if user closes window or clicks cancel
        app.close()
    elif event == 'Login':
        input_text_value = values['input']
        if input_text_value =='aluno':
            app.change_interface(interface_student)
        elif input_text_value =='adm':
            app.change_interface(interface_adm)
        else: 
            app.change_interface(interface_error)
   
