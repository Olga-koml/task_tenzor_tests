from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для страницы."""

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

    def page_source(self):
        return self.driver.page_source

    def current_url(self):
        return self.driver.current_url

    # def do_click(self, locator, time_out=15):
    #     WebDriverWait(self.driver, time_out).until(
    #         EC.visibility_of_element_located(locator)
    #         ).click()


# c site video
    # def do_click(self, locator, time_out=10):
    #     WebDriverWait(self.driver, time_out).until(
    #         EC.visibility_of_element_located(locator)
    #         ).click()

    # def send_keys(self, locator, time_out=10, text):
    #     WebDriverWait(self.driver, time_out).until(
    #         EC.visibility_of_element_located(locator)
    #         ).send_keys(text)

    # def get_element_text(self, locator, time_out=10):
    #     element = WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located(locator))
    #     return element.text

    # def is_visible(self, locator, time_out=10):
    #     element = WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located(locator))
    #     return bool(element)

    # def get_title(self, title, time_out=10):
    #     WebDriverWait(self.driver, time_out).until(EC.title_is(title))
    #     return self.driver.title
