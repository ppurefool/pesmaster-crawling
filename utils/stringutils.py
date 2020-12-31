from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import sys

# print("[{}] -> [{}]".format(" 1 ", " 1 ".strip()))
# print("[{}] -> [{}]".format(None, "  ".strip()))
#
# print(True if "1" else False)  # True
# print(True if "" else False)  # False
# print(True if None else False)  # False


def is_blank(*args):
    for arg in args:
        if arg is not None and arg and str(arg).strip():
            return False
    return True
#
#
# print(is_blank(None))  # True
# print(is_blank(""))  # True
# print(is_blank(" "))  # True
# print(is_blank("  "))  # True
#
# print(is_blank(" 1 "))  # False
# print(is_blank(1))  # False


def is_not_blank(*args):
    for arg in args:
        if is_blank(arg):
            return False
    return True
#
#
# print(is_not_blank(None))  # False
# print(is_not_blank(""))  # False
# print(is_not_blank(" "))  # False
# print(is_not_blank("  "))  # False
#
# print(is_not_blank(" 1 "))  # True
#
#
# def is_ability(value):
#     try:
#         return True if value is not None and value and 40 <= int(value) <= 99 else False
#     except ValueError:
#         return False
#
#
# print(is_ability(None))  # False
# print(is_ability(" a40 "))  # False
# print(is_ability(" 40 "))  # True
# print(is_ability("40"))  # True
#
#
# print(list(map((lambda x:
#                 x **
#                 2), range(5))))
#
#
# def map_func(func, param):
#     return [func(x) for x in param]
#
#
# print(list(map_func((lambda x: x ** 2), range(5))))
#
#
# def chrome(success_callback, error_callback):
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#     try:
#         with webdriver.Chrome(options=options) as web_driver:
#             success_callback(web_driver)
#     except WebDriverException:
#         error_callback()
#
#
# def success(driver):
#     def get_text_of_top_element(web_driver, class_name):
#         if not web_driver or not class_name:
#             return ""
#
#         result = web_driver.find_elements_by_class_name(class_name)
#         if len(result) == 0 or not result[0].text:
#             return ""
#         return result[0].text
#     player_name = get_text_of_top_element(driver, 'subtle-text')
#     offensive_awareness = get_text_of_top_element(driver, 'offensive_awareness')
#     print(player_name)
#     print(offensive_awareness)
#     raise Exception("test")
#
#
# chrome(success, (lambda: print(sys.exc_info())))


print("__name__: " + __name__)
if __name__ == "__main__":
    print(NameError.__name__)
