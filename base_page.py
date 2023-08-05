from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://ya.ru/'

    def find_element(self, locator, time_out=15):
        return WebDriverWait(self.driver, time_out).until(
            EC.presence_of_element_located(locator),
            message=f'Не найдейн элемент по локатору {locator}'
            )

    def find_elements(self, locator, time_out=15):
        return WebDriverWait(self.driver, time_out).until(
            EC.presence_of_all_elements_located(locator),
            message=f'Не найднеы элементы по локатору {locator}'
            )

    def go_to_site(self):
        return self.driver.get(self.base_url)
    
    # def click_enter(self, locator, time=10):
    #     return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator)).send_keys(Keys.RETURN)
    
        # def click_enter(self):
    #     return self.send_keys(Keys.RETURN))