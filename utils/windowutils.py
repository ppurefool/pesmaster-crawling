import pywinauto


def activate(success_callback, error_callback, **kwargs):
    try:
        app = pywinauto.application.Application().connect(**kwargs)
    except pywinauto.findwindows.ElementNotFoundError:
        error_callback(pywinauto.findwindows.ElementNotFoundError)
        return
    success_callback(app)
