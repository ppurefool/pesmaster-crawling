from utils import windowutils


def success(app):
    dlg = app.window()
    print(dlg)
    # dlg.Edit.type_keys("입력테스트!!", pause=0.1)
    # dlg.menu_select("파일 -> 끝내기")
    app.top_window().type_keys("{ENTER}", pause=0.1)

    # print(app)
    # print(app.Notepad.print_control_identifiers())
    # print(app.Notepad.Edit.Properties.print_control_identifiers())
    # print(app.Properties.print_control_identifiers())
    # print(app.top_window().Edit.Properties.print_control_identifiers())
    # print(app["Edit"].Properties.print_control_identifiers())
    # dlg = app.top_window()
    # dlg[0].type_keys("{ENTER}" + "{DOWN}^a".join(["79"]) + "{ENTER}", pause=0.1)


def error(exception):
    pass


windowutils.activate(success, error, path="cheatengine-x86_64.exe")
