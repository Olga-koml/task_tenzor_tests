from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    '''Базовый класс для страницы.'''

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://ya.ru/'

    def find_element(self, locator, time_out=15):
        '''Находит элемент на странице.'''
        return WebDriverWait(self.driver, time_out).until(
            EC.presence_of_element_located(locator),
            message=f'Не найдейн элемент по локатору {locator}'
            )

    def find_elements(self, locator, time_out=15):
        '''Находит элементы на странице.'''
        return WebDriverWait(self.driver, time_out).until(
            EC.presence_of_all_elements_located(locator),
            message=f'Не найднеы элементы по локатору {locator}'
            )

    def go_to_site(self):
        '''Переходит на сайт.'''
        return self.driver.get(self.base_url)

    def page_source(self):
        '''Отображает данные страницы'''
        return self.driver.page_source

    def current_url(self):
        '''Отображает текущий урл.'''
        return self.driver.current_url

    def do_click(self, locator, time_out=15):
        '''Кликает по видимому элементу.'''
        WebDriverWait(self.driver, time_out).until(
            EC.visibility_of_element_located(locator)
            ).click()

    def find_and_click_element(self, locator, time_out=15):
        '''Находит элемент и кликает по видимому элементу'''
        self.find_element(locator, time_out)
        self.do_click(locator, time_out)
