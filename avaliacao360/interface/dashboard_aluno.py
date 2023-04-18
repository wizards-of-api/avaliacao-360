import app
import interface.dashboard_aluno as interface_dashboard_aluno
import connection.student as connection_student
import PySimpleGUI as sg

def dashboard_aluno():

    layout = [[sg.Text('Avaliação 360 - Dashboard Aluno')]]

    window = sg.Window('Avaliação 360 - Aluno', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
    window.close()
