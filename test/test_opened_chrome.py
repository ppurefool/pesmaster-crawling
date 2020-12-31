from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 1. 크롬을 디버깅이 가능하도록 실행; "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="c:/ChromeTEMP"\
# 2. 웹 페이지 표시; ex.) https://www.pesmaster.com/l-messi/pes-2021/player/7511/
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

with webdriver.Chrome(options=chrome_options) as driver:
    elements = driver.find_elements_by_class_name('offensive_awareness')
    if len(elements) > 0:
        offensive_awareness = elements[0].text
        print("offensive_awareness: " + offensive_awareness)
    else:
        print("error")
