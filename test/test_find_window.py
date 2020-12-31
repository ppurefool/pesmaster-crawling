import pywinauto

app = pywinauto.application.Application().connect(title_re=u".*메모장.*")
dlg = app.top_window()
keyDelay = 0.5
dlg.Edit.type_keys("Hi from Python.", with_spaces=True, pause=keyDelay)
dlg.Edit.type_keys("{ENTER}", with_spaces=True, pause=keyDelay)
dlg.Edit.type_keys("Hi from Python.", with_spaces=True, pause=keyDelay)
idlg.Edit.type_keys("{ENTER}")
