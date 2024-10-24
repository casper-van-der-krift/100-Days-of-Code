import time

from typing import NoReturn

from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color


class CookieBooster:
    """

    The cookie clicker website has several cookie boosters that can be purchased with cookies.
    This class represents these boosters with the attributes that are relevant for the game flow.

    Attributes:
        name (str): name
        driver (webdriver object): webdriver object (for the cookie clicker website)
        css_selector (str): the CSS Selector of the booster element of the cookie clicker website.
            This is the key attribute, by which all other attributes are obtained.
        price (int): the price of the booster object. Will be updated by calling the update() method.
        background_color (str): background color in hex format (i.e. #xxxxxxx).
            Background color indicates the availability of the object.
        is_available (bool): indicates if the booster is available or not. Booster is available if cookie count > price.

    """

    def __init__(self, name, driver, css_selector):
        self.name = name
        self.driver = driver
        self.css_selector = css_selector
        self.price = self.get_price()
        self.background_color = self.get_background_color()
        self.is_available = self.get_availability()

    def update(self) -> NoReturn:
        self.price = self.get_price()
        self.background_color = self.get_background_color()
        self.is_available = self.get_availability()

    def get_price(self) -> int:
        price_str = self.driver.find_element(By.CSS_SELECTOR, value=f'{self.css_selector} b').text
        price_num_str_list = [i for i in price_str if i.isnumeric()]
        cursor_price = int(''.join(price_num_str_list))
        return cursor_price

    def get_background_color(self) -> str:
        booster_object = self.driver.find_element(By.CSS_SELECTOR, value=f'{self.css_selector}')
        booster_color_rgb = booster_object.value_of_css_property('background-color')
        booster_color_hex = Color.from_string(booster_color_rgb).hex
        return booster_color_hex

    def click(self) -> NoReturn:
        booster_object = self.driver.find_element(By.CSS_SELECTOR, value=f'{self.css_selector}')
        booster_object.click()
        print(f"Clicked {self.name}!")

    def get_availability(self) -> NoReturn:
        if self.background_color == "#666666":
            return False
        else:
            return True

    def click_till_unavailable(self) -> NoReturn:
        self.update()
        time.sleep(0.1)
        while self.is_available:
            time.sleep(0.1)
            self.click()
            time.sleep(0.1)
            self.update()
