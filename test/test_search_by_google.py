from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import sys

with webdriver.Chrome(options=currentOptions) as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.google.com/")
    try:
        search_box = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    except webdriver.common.exceptions.NoSuchElementException:
        print('google search - error: find_element_by_xpath()')
        sys.exit()
    search_box.send_keys('pesmaster 2021 kepa')
    search_box.send_keys(Keys.RETURN)
    elements = driver.find_elements_by_xpath('//*[@id="rso"]/div[*]/div/div[1]/a')
    if len(elements) > 0:
        newUrl = elements[0].get_attribute("href")
