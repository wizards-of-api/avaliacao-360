import app
from connection import controller
import interface.home as interface_home

controller.create_db()

app.change_interface(interface_home.create_window(), interface_home.event_handler)
app.run()