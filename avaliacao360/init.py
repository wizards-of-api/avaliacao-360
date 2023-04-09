import app
import interface.home as interface_home

app.change_interface(interface_home.create_window(), interface_home.event_handler)
app.run()