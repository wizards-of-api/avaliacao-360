import app
import PySimpleGUI as sg
import interface.login as interface_login  
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Não Possui Login')],
        [sg.Button('Back'), sg.Button('Cancel')]]
# Create the Window
window = sg.Window('Window Title', layout)

def event_handler(event, values):
  if event == 'Cancel': # if user closes window or clicks cancel
    app.close()
  elif event == 'Back':
    window.close()