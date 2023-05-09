import app
from datetime import date
from connection import controller
import interface.login as interface_login


def init(fix_date = None):
    controller.create_db()

    if fix_date:
        app.set_date(fix_date)

    app.change_interface(interface_login.create_window(), interface_login.event_handler)
    app.run()

if __name__ == '__main__':
    init()