import app
from datetime import date
from connection import controller
import interface.home as interface_home


def init(fix_date = None):
    controller.create_db()

    if fix_date:
        app.set_date(fix_date)

    app.change_interface(interface_home.create_window(), interface_home.event_handler)
    app.run()

if __name__ == '__main__':
    init()