from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage


class ImageSearchPage(BasePage):
    '''Класс для поиска картинок.'''

    def switch_to_window(self, win_number):
        '''Переходин на заданную по номеру вкладку.'''
        return self.driver.switch_to.window(
            self.driver.window_handles[win_number]
            )

    def check_menu_bar_on_page(self):
        '''Проверяет наличие кнопки меню на странице.'''
        try:
            menu = self.driver.find_element(
                By.CSS_SELECTOR, 'a[title*="Все сервисы"]'
                )
            return menu
        except NoSuchElementException:
            return None
