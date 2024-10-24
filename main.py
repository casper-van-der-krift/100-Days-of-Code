from selenium import webdriver
from selenium.webdriver.common.by import By

from typing import NoReturn

from cookie_booster import CookieBooster


def get_cookie_count(driver) -> int:
    """Takes a webdriver object (of the cookie clicker website) and searches for the element that counts the cookies.
    Takes the text string of that object, filters the numeric values and returns the cookie count as an integer."""
    cookie_count_str = driver.find_element(By.ID, value='money').text
    cookie_count_str_list = [i for i in cookie_count_str if i.isnumeric()]
    cookie_count_int = int(''.join(cookie_count_str_list))
    return cookie_count_int


# 1. SETUP

# ids of the website objects that contain the cookie boosters
cursor_id = '#buyCursor'
grandma_id = '#buyGrandma'
factory_id = '#buyFactory'
mine_id = '#buyMine'
shipment_id = '#buyShipment'

# Chrome settings for webdriver
chrome_settings = webdriver.ChromeOptions()
chrome_settings.add_experimental_option("detach", value=True)
chrome_settings.add_argument("--disable-search-engine-choice-screen")

# Setup webdriver for cookie clicker website
my_driver = webdriver.Chrome(options=chrome_settings)
my_driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Store the main button (i.e. Big Cookie Button)
big_cookie_button = my_driver.find_element(By.ID, value="cookie")

# Create booster objects
cursor = CookieBooster(name='cursor', driver=my_driver, css_selector=cursor_id)
grandma = CookieBooster(name='grandma', driver=my_driver, css_selector=grandma_id)
factory = CookieBooster(name='factory', driver=my_driver, css_selector=factory_id)
mine = CookieBooster(name='mine', driver=my_driver, css_selector=mine_id)
shipment = CookieBooster(name='shipment', driver=my_driver, css_selector=shipment_id)

booster_objects = [shipment, mine, factory, grandma, cursor]

# 2. GAMEPLAY: click until a certain score is reached, then click available booster from best to worst, then repeat.

score_steps = [60, 100, 250, 300, 500, 1000, 1500, 2500, 4000, 5500, 7000, 10000]


def play_until_score(cookie_score: int) -> NoReturn:
    """Takes a target score as input. Keeps clicking the main cookie button until this score is reached.
    Then all CookieBoosters objects are clicked until no longer available (i.e. insufficient cookie balance).
    CookieBoosters are clicked from most expensive to least expensive."""
    while get_cookie_count(driver=my_driver) < cookie_score:
        big_cookie_button.click()

    for booster in booster_objects:
        booster.click_till_unavailable()


for score in score_steps:
    play_until_score(score)
