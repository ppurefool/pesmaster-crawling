from selenium import webdriver
from selenium.common.exceptions import WebDriverException


def do(debugging_port, executable_path, success_callback, error_callback):
    options = webdriver.ChromeOptions()
# 1. 크롬을 디버깅이 가능하도록 실행
# ; "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
#   --remote-debugging-port=9222 --user-data-dir="c:/ChromeTEMP"\
# 2. 웹 페이지 표시; ex.) https://www.pesmaster.com/l-messi/pes-2021/player/7511/
    options.add_experimental_option("debuggerAddress", "127.0.0.1:" + str(debugging_port))
    try:
        with webdriver.Chrome(executable_path=executable_path, options=options) as web_driver:
            success_callback(web_driver)
    except WebDriverException:
        error_callback(WebDriverException)


def get_text_of_top_element_by_class(web_driver, class_name):
    if not web_driver or not class_name:
        return ""

    result = web_driver.find_elements_by_class_name(class_name)
    if len(result) == 0 or not result[0].text:
        return ""
    return result[0].text
