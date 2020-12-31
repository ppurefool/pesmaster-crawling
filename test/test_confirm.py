import pyautogui

while 'OK' == pyautogui.confirm(text="확인 선택시 crawling; 취소 선택시 종료", title="알림"):
    pass
