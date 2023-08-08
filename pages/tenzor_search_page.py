from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class TenzorSeacrhLocator:
    '''Вспомогательны класс с данными для поиска элементов.'''

    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, 'text')
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_SUGGEST_TABLE = (By.CSS_SELECTOR, 'ul[class*=mini-suggest]')
    LOCATOR_SEARCH_RESULTS_BY_TAG = (By.TAG_NAME, 'body')
    LOCATOR_SEARCH_RESULTS_BY_CSS = (
        By.CSS_SELECTOR, 'ul[class*=serp-list]>li>div>div>div>a>b'
        )


class TenzorSearchPage(BasePage):
    '''Класс для поиска Тензор.'''

    def __init__(self, driver):
        super().__init__(driver)

    def enter_word(self, word):
        '''Метод вводит слово в поисковую строку.'''
        search_field = self.find_element(
            TenzorSeacrhLocator.LOCATOR_YANDEX_SEARCH_FIELD
            )
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_enter(self):
        '''Нажимает на кнопку ентер.'''
        search_field = self.find_element(
            TenzorSeacrhLocator.LOCATOR_YANDEX_SEARCH_FIELD
            )
        search_field.send_keys(Keys.RETURN)
        return search_field

    def check_search_field(self):
        '''Находит поле поиска для проверки.'''
        search_field = self.find_element(
            TenzorSeacrhLocator.LOCATOR_YANDEX_SEARCH_FIELD
            )
        return search_field

    def check_suggest_table(self):
        '''Находит таблицу с подсказками для проверки.'''
        suggest = self.find_element(TenzorSeacrhLocator.LOCATOR_SUGGEST_TABLE)
        return suggest

    def check_search_result(self):
        '''Находит результаты поиска для проверки.'''
        body = self.find_element(
            TenzorSeacrhLocator.LOCATOR_SEARCH_RESULTS_BY_TAG
            )
        return body

    def check_first_link_in_search_results(self):
        '''Находит первую ссылку среди реультатов поиска для проверки.'''
        search_results = self.find_elements(
            TenzorSeacrhLocator.LOCATOR_SEARCH_RESULTS_BY_CSS
            )
        first_link = search_results[0].text
        return first_link
