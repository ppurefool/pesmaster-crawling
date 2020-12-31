import sys
import pyautogui

from utils import stringutils, windowutils, requestutils, yamlutils

global CHROME_REMOTE_DEBUGGING_PORT
global CHEAT_ENGINE_KEY_DELAY
global CHEAT_ENGINE_WINDOW_TITLE
global CHEAT_ENGINE_WINDOW_INDEX
global KEYS


def main() -> int:
    print('pesmaster.yaml read - start')
    yamlutils.load("resource/pesmaster.yaml", yaml_load_success)
    if not stringutils.is_not_blank([CHROME_REMOTE_DEBUGGING_PORT, CHEAT_ENGINE_KEY_DELAY, CHEAT_ENGINE_WINDOW_TITLE,
                                     CHEAT_ENGINE_WINDOW_INDEX]):
        print('pesmaster.yaml read - error')
        return 1
    print("pesmaster.yaml read - CHROME_REMOTE_DEBUGGING_PORT: " + str(CHROME_REMOTE_DEBUGGING_PORT))
    print("pesmaster.yaml read - CHEAT_ENGINE_KEY_DELAY: " + str(CHEAT_ENGINE_KEY_DELAY))
    print("pesmaster.yaml read - CHEAT_ENGINE_WINDOW_TITLE: " + CHEAT_ENGINE_WINDOW_TITLE)
    print("pesmaster.yaml read - CHEAT_ENGINE_WINDOW_INDEX: " + str(CHEAT_ENGINE_WINDOW_INDEX))
    print('pesmaster.yaml read - end')

    while 'OK' == pyautogui.confirm(text="확인 선택시 crawling; 취소 선택시 종료", title="알림"):
        requestutils.do(
            CHROME_REMOTE_DEBUGGING_PORT,
            "resource/chromedriver",
            request_success,
            (lambda exception: print('pesmaster 2021 player crawl - error: ' + exception.__name__ + ' / ' +
                                     str(sys.exc_info()))))
    return 0


def request_success(driver):
    global KEYS

    print('pesmaster 2021 player crawl - start')
    player_name = requestutils.get_text_of_top_element_by_class(driver, 'subtle-text')
    offensive_awareness = requestutils.get_text_of_top_element_by_class(driver, 'offensive_awareness')
    finishing = requestutils.get_text_of_top_element_by_class(driver, 'finishing')
    kicking_power = requestutils.get_text_of_top_element_by_class(driver, 'kicking_power')
    ball_control = requestutils.get_text_of_top_element_by_class(driver, 'ball_control')
    dribbling = requestutils.get_text_of_top_element_by_class(driver, 'dribbling')
    tight_possession = requestutils.get_text_of_top_element_by_class(driver, 'tight_possession')
    balance = requestutils.get_text_of_top_element_by_class(driver, 'balance')
    heading = requestutils.get_text_of_top_element_by_class(driver, 'heading')
    jump = requestutils.get_text_of_top_element_by_class(driver, 'jump')
    defensive_awareness = requestutils.get_text_of_top_element_by_class(driver, 'defensive_awareness')
    ball_winning = requestutils.get_text_of_top_element_by_class(driver, 'ball_winning')
    aggression = requestutils.get_text_of_top_element_by_class(driver, 'aggression')
    low_pass = requestutils.get_text_of_top_element_by_class(driver, 'low_pass')
    lofted_pass = requestutils.get_text_of_top_element_by_class(driver, 'lofted_pass')
    place_kicking = requestutils.get_text_of_top_element_by_class(driver, 'place_kicking')
    curl = requestutils.get_text_of_top_element_by_class(driver, 'curl')
    speed = requestutils.get_text_of_top_element_by_class(driver, 'speed')
    acceleration = requestutils.get_text_of_top_element_by_class(driver, 'acceleration')
    physical_contact = requestutils.get_text_of_top_element_by_class(driver, 'physical_contact')
    stamina = requestutils.get_text_of_top_element_by_class(driver, 'stamina')
    gk_awareness = requestutils.get_text_of_top_element_by_class(driver, 'gk_awareness')
    gk_catching = requestutils.get_text_of_top_element_by_class(driver, 'gk_catching')
    gk_clearing = requestutils.get_text_of_top_element_by_class(driver, 'gk_clearing')
    gk_reflexes = requestutils.get_text_of_top_element_by_class(driver, 'gk_reflexes')
    gk_reach = requestutils.get_text_of_top_element_by_class(driver, 'gk_reach')

    if stringutils.is_blank(player_name):
        print('pesmaster 2021 player crawl - player_name error: ' + str(player_name))
        return  # return  # continue  # sys.exit(1)
    if is_not_ability(offensive_awareness):
        print('pesmaster 2021 player crawl - offensive_awareness error: ' + str(offensive_awareness))
        return  # continue  # sys.exit(1)
    if is_not_ability(finishing):
        print('pesmaster 2021 player crawl - finishing error: ' + str(finishing))
        return  # continue  # sys.exit(1)
    if is_not_ability(kicking_power):
        print('pesmaster 2021 player crawl - kicking_power error: ' + str(kicking_power))
        return  # continue  # sys.exit(1)
    if is_not_ability(ball_control):
        print('pesmaster 2021 player crawl - ball_control error: ' + str(ball_control))
        return  # continue  # sys.exit(1)
    if is_not_ability(dribbling):
        print('pesmaster 2021 player crawl - dribbling error: ' + str(dribbling))
        return  # continue  # sys.exit(1)
    if is_not_ability(tight_possession):
        print('pesmaster 2021 player crawl - tight_possession error: ' + str(tight_possession))
        return  # continue  # sys.exit(1)
    if is_not_ability(balance):
        print('pesmaster 2021 player crawl - balance error: ' + str(balance))
        return  # continue  # sys.exit(1)
    if is_not_ability(heading):
        print('pesmaster 2021 player crawl - heading error: ' + str(heading))
        return  # continue  # sys.exit(1)
    if is_not_ability(jump):
        print('pesmaster 2021 player crawl - jump error: ' + str(jump))
        return  # continue  # sys.exit(1)
    if is_not_ability(defensive_awareness):
        print('pesmaster 2021 player crawl - defensive_awareness error: ' + str(defensive_awareness))
        return  # continue  # sys.exit(1)
    if is_not_ability(ball_winning):
        print('pesmaster 2021 player crawl - ball_winning error: ' + str(ball_winning))
        return  # continue  # sys.exit(1)
    if is_not_ability(aggression):
        print('pesmaster 2021 player crawl - aggression error: ' + str(aggression))
        return  # continue  # sys.exit(1)
    if is_not_ability(low_pass):
        print('pesmaster 2021 player crawl - low_pass error: ' + str(low_pass))
        return  # continue  # sys.exit(1)
    if is_not_ability(lofted_pass):
        print('pesmaster 2021 player crawl - lofted_pass error: ' + str(lofted_pass))
        return  # continue  # sys.exit(1)
    if is_not_ability(place_kicking):
        print('pesmaster 2021 player crawl - place_kicking error: ' + str(place_kicking))
        return  # continue  # sys.exit(1)
    if is_not_ability(curl):
        print('pesmaster 2021 player crawl - curl error: ' + str(curl))
        return  # continue  # sys.exit(1)
    if is_not_ability(speed):
        print('pesmaster 2021 player crawl - speed error: ' + str(speed))
        return  # continue  # sys.exit(1)
    if is_not_ability(acceleration):
        print('pesmaster 2021 player crawl - acceleration error: ' + str(acceleration))
        return  # continue  # sys.exit(1)
    if is_not_ability(physical_contact):
        print('pesmaster 2021 player crawl - physical_contact error: ' + str(physical_contact))
        return  # continue  # sys.exit(1)
    if is_not_ability(stamina):
        print('pesmaster 2021 player crawl - stamina error: ' + str(stamina))
        return  # continue  # sys.exit(1)
    if is_not_ability(gk_awareness):
        print('pesmaster 2021 player crawl - gk_awareness error: ' + str(gk_awareness))
        return  # continue  # sys.exit(1)
    if is_not_ability(gk_catching):
        print('pesmaster 2021 player crawl - gk_catching error: ' + str(gk_catching))
        return  # continue  # sys.exit(1)
    if is_not_ability(gk_clearing):
        print('pesmaster 2021 player crawl - gk_clearing error: ' + str(gk_clearing))
        return  # continue  # sys.exit(1)
    if is_not_ability(gk_reflexes):
        print('pesmaster 2021 player crawl - gk_reflexes error: ' + str(gk_reflexes))
        return  # continue  # sys.exit(1)
    if is_not_ability(gk_reach):
        print('pesmaster 2021 player crawl - gk_reach error: ' + str(gk_reach))
        return  # continue  # sys.exit(1)

    print('player_name: ' + player_name)
    print('offensive_awareness: ' + offensive_awareness)
    print('finishing: ' + finishing)
    print('kicking_power: ' + kicking_power)
    print('ball_control: ' + ball_control)
    print('dribbling: ' + dribbling)
    print('tight_possession: ' + tight_possession)
    print('balance: ' + balance)
    print('heading: ' + heading)
    print('jump: ' + jump)
    print('defensive_awareness: ' + defensive_awareness)
    print('ball_winning: ' + ball_winning)
    print('aggression: ' + aggression)
    print('low_pass: ' + low_pass)
    print('lofted_pass: ' + lofted_pass)
    print('place_kicking: ' + place_kicking)
    print('curl: ' + curl)
    print('speed: ' + speed)
    print('acceleration: ' + acceleration)
    print('physical_contact: ' + physical_contact)
    print('stamina: ' + stamina)
    print('gk_awareness: ' + gk_awareness)
    print('gk_catching: ' + gk_catching)
    print('gk_clearing: ' + gk_clearing)
    print('gk_reflexes: ' + gk_reflexes)
    print('gk_reach: ' + gk_reach)
    print('pesmaster 2021 player crawl - end')

    KEYS = [offensive_awareness, finishing, kicking_power, ball_control, dribbling, tight_possession, balance, heading,
            jump, defensive_awareness, ball_winning, aggression, low_pass, lofted_pass, place_kicking, curl, speed,
            acceleration, physical_contact, stamina, gk_awareness, gk_catching, gk_clearing, gk_reflexes, gk_reach]

    windowutils.activate(
        activate_window_success_callback,
        (lambda exception: print('cheat engine input - error: ' + exception.__name__ + ' / ' +
                                 str(sys.exc_info()))),
        title_re=CHEAT_ENGINE_WINDOW_TITLE,
        found_index=CHEAT_ENGINE_WINDOW_INDEX)


def activate_window_success_callback(app):
    print('cheat engine input - start')
    dlg = app.top_window()
    dlg.Edit.type_keys("{ENTER}" + "{DOWN}^a".join(KEYS) + "{ENTER}", pause=CHEAT_ENGINE_KEY_DELAY)
    print('cheat engine input - end')


def is_not_ability(value):
    try:
        return True if not value or int(value) < 40 or int(value) > 99 else False
    except ValueError:
        return True


def yaml_load_success(json, json_utils):
    global CHROME_REMOTE_DEBUGGING_PORT
    global CHEAT_ENGINE_KEY_DELAY
    global CHEAT_ENGINE_WINDOW_TITLE
    global CHEAT_ENGINE_WINDOW_INDEX

    print(json)
    CHROME_REMOTE_DEBUGGING_PORT = json_utils.get_value(json, ["chrome", "remote-debugging-port"])
    CHEAT_ENGINE_KEY_DELAY = json_utils.get_value(json, ["cheat-engine", "key-delay"])
    CHEAT_ENGINE_WINDOW_TITLE = json_utils.get_value(json, ["cheat-engine", "title"])
    CHEAT_ENGINE_WINDOW_INDEX = json_utils.get_value(json, ["cheat-engine", "found-index"])


if __name__ == '__main__':
    sys.exit(main())
