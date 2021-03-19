import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main() -> int:
    positions = []
    ranks = []
    names = []
    clubs = []

    urls = [
        'https://www.footballcritic.com/top-players/attackers',
        'https://www.footballcritic.com/top-players/wingers',
        'https://www.footballcritic.com/top-players/attacking-midfielders',
        'https://www.footballcritic.com/top-players/defensive-midfielders',
        'https://www.footballcritic.com/top-players/backs',
        'https://www.footballcritic.com/top-players/defenders',
        'https://www.footballcritic.com/top-players/goalkeepers'
    ]
    types = ['CF', 'WF/SMF', 'AMF', 'CMF/DMF', 'SB', 'CB', 'GK']

    for url_index in range(len(urls)):
    # for url_index in range(2):
        print(urls[url_index] + " request - start")
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(executable_path="resource/chromedriver", options=options)
        driver.get(url=urls[url_index])

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'name'))
            )
            name_elements = driver.find_elements_by_class_name('name')
            club_elements = driver.find_elements_by_class_name('club-name')
            for index in range(13):
                positions.append(types[url_index])
                ranks.append(index + 1)
                names.append(name_elements[index].text)
                clubs.append(club_elements[index].text)
        finally:
            print(urls[url_index] + " request - end")
            driver.quit()

    print('POSITION\tRANK\tNAME\tTEAM')
    for index in range(len(positions)):
        print(positions[index] + '\t' + str(ranks[index]) + '\t' + names[index] + '\t' + clubs[index])
    return 0


if __name__ == '__main__':
    sys.exit(main())
