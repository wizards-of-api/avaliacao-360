import reset_mock_db
import PySimpleGUI as sg

from datetime import date
from avaliacao360.__init__ import init
from avaliacao360.utils.date_functions import convert_date_str
    
date_format = '%d/%m/%Y'

layout = [[sg.InputText('', key='date'), sg.CalendarButton('Definir', target='date', format=date_format)],
          [sg.Button('Confirmar', key='confirm')]]

window = sg.Window('DEBUG DATE', layout)

event, values = window.read()

if event == 'confirm' and values['date'] != '':
    window.close()
    init(convert_date_str(values['date']))