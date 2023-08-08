from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class TenzorSeacrhLocator:

    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, 'text')
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    # LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")  # пока не используется
    LOCATOR_SUGGEST_TABLE = (By.CSS_SELECTOR, 'ul[class*=mini-suggest]')
    LOCATOR_SEARCH_RESULTS_BY_TAG = (By.TAG_NAME, 'body')
    LOCATOR_SEARCH_RESULTS_BY_CSS = (
        By.CSS_SELECTOR, 'ul[class*=serp-list]>li>div>div>div>a>b'
        )


class TenzorSearchPage(BasePage):

    def __init__(self, driver):  # lskdjfls
        super().__init__(driver)  # введены недавно

    def enter_word(self, word):
        search_field = self.find_element(
            TenzorSeacrhLocator.LOCATOR_YANDEX_SEARCH_FIELD
            )
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(
            TenzorSeacrhLocator.LOCATOR_YANDEX_SEARCH_BUTTON, time=2
            ).click()

    # def check_navigation_bar(self):  # проверить, не используется вроде
    #     all_list = self.find_elements(
    #         TenzorSeacrhLocator.LOCATOR_YANDEX_NAVIGATION_BAR, time=2
    #         )
    #     nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
    #     return nav_bar_menu

    def click_enter(self):
        search_field = self.find_element(
            TenzorSeacrhLocator.LOCATOR_YANDEX_SEARCH_FIELD
            )
        search_field.send_keys(Keys.RETURN)
        return search_field

    def check_search_field(self):
        search_field = self.find_element(
            TenzorSeacrhLocator.LOCATOR_YANDEX_SEARCH_FIELD
            )
        return search_field

    def check_suggest_table(self):
        suggest = self.find_element(TenzorSeacrhLocator.LOCATOR_SUGGEST_TABLE)
        return suggest

    def check_search_result(self):
        body = self.find_element(
            TenzorSeacrhLocator.LOCATOR_SEARCH_RESULTS_BY_TAG
            )
        return body

    def check_first_link_in_search_results(self):
        search_results = self.find_elements(
            TenzorSeacrhLocator.LOCATOR_SEARCH_RESULTS_BY_CSS
            )
        first_link = search_results[0].text
        return first_link
