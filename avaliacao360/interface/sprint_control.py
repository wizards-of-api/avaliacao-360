import PySimpleGUI as sg
import interface.adm as interface_adm
import connection.class_room as room_connection
from datetime import timedelta
from utils.date_functions import convert_date_str
import app

def default_event_handler(event, _):
    if event == 'return interface':
        app.change_interface(interface_adm.create_window(), interface_adm.event_handler)

def get_sprint_number(values):
    try:
        sprint_total = int(values['sprint_total'])
        if sprint_total > 10 or sprint_total < 1:
            raise Exception('')
        return sprint_total
    except:
        sg.popup('Numero total de sprint invalido (1 à 10)')

def sprint_configure_handler(room_id, sprint_total):
    sprint_num = 1
    date_format = '%d/%m/%Y'
    last_date = None
    sprint_list = []

    room_connection.reset_sprints(room_id)

    def recursive_call():
        nonlocal room_id

        if sprint_num > sprint_total:
            for sprint in sprint_list:
                room_connection.add_sprint(room_id, sprint)
            app.change_interface(interface_adm.create_window(), interface_adm.event_handler)
            return
        app.change_interface(create_window(), event_handler)

    def create_window():
        nonlocal sprint_num, last_date, date_format
        disable_initial_calendar = last_date != None
        initial_date = ''
        if disable_initial_calendar:
            last_date += timedelta(days=1)
            initial_date = last_date.strftime(date_format)
        layout = [
            [sg.Text('Sprint: ' + str(sprint_num))],
            [
                sg.Text("Data Inicial: ", size=(12,1)), 
                sg.InputText(initial_date, key='date1', disabled=True, size=(10, 1), text_color='black'), 
                sg.CalendarButton("Escolher", format=date_format, target='date1', disabled=disable_initial_calendar)
            ],
            [
                sg.Text("Data Final: ", size=(12,1)), 
                sg.InputText('', key='date2', disabled=True, size=(10, 1), text_color='black'), 
                sg.CalendarButton("Escolher", format=date_format, target='date2')
            ],
            [sg.Button('Confirmar', key='confirm')]
        ]
        return sg.Window('Avaliação 360 - Controle de Sprint', layout, element_justification='c', finalize= True)
    
    def event_handler(event, values):
        nonlocal sprint_num, last_date, date_format, room_id
        if event == 'confirm':
            date1 = convert_date_str(values['date1'])
            date2 = convert_date_str(values['date2'])
            if date1 >= date2:
                sg.popup('Data Inical não pode ser antes da Data Final')
                return
            sprint_list.append({'start': values['date1'], 'end': values['date2']})

            last_date = date2
            sprint_num += 1
            recursive_call()

    recursive_call()

def room_select_interface():
    def create_window():
        room_list = room_connection.get_class_room_list()

        room_name_list = [room['name'] for room in room_list]

        layout = [
            [sg.Text("Selecione uma sala: "), sg.Combo(room_name_list, default_value=room_name_list[0], key='class_room')],
            [sg.Text("Total de sprints: "), sg.Input(key='sprint_total')],
            [sg.Button('Confirmar', key='confirm'), sg.Button('Voltar', key='return interface')]
        ]
        return sg.Window('Avaliação 360 - Controle de Sprint', layout, element_justification='c', finalize= True)

    def event_handler(event, values):
        default_event_handler(event, values)
        if event == 'confirm':
                if values['class_room'] == '':
                    return
                room_name = values['class_room']
                sprint_total = get_sprint_number(values)
                if not sprint_total:
                    return
                sprint_configure_handler(room_connection.get_class_room_by_name(room_name)[0]['id'], sprint_total)


    return [create_window, event_handler]

