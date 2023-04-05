import PySimpleGUI as sg
import gui_exemples.home as gui_home
import gui_exemples.login as gui_login
import gui_exemples.student_interface as gui_student
import gui_exemples.adm_interface as gui_adm

current_gui = gui_home
current_window = current_gui.window

while True:
    current_window = current_gui.window
    event, values = current_window.read()

    event_response = current_gui.event_handler(event, values)
    if event_response:
        if event == sg.WIN_CLOSED or event_response[0] == 'close':
            break

        elif event_response[0] == 'change_window':
            current_window.close()
            if event_response[1] == 'login':
                current_gui =  gui_login
            elif event_response[1] == 'student_interface':
                current_gui = gui_student
            elif event_response[1] == 'adm_interface':
                current_gui = gui_adm

current_window.close()