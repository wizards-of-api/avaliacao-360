import app
import interface.dashboard_aluno as interface_dashboard_aluno
import connection.student as connection_student
import PySimpleGUI as sg

def create_window():

    layout = [[sg.Text('Avaliação 360 - Dashboard Aluno')]]

    return sg.Window('Avaliação 360 - Aluno', layout)