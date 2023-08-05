from tenzor_search_page import TenzorSearch
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search_tenzor(browser):
    yandex_page = TenzorSearch(browser)
    yandex_page.go_to_site()
    check_search_field = yandex_page.check_search_field()
    assert check_search_field.is_enabled(), 'Строка поиска не найдена'
    yandex_page.enter_word('Тензор')
    suggest = yandex_page.check_suggest_table()
    assert suggest.is_displayed(), (
        'Таблица с подсказками suggest не видна пользователю'
        )
    yandex_page.click_enter()
    body = yandex_page.check_search_result()
    html = body.get_attribute('innerHTML')
    assert body.is_displayed(), 'Cтраница результатов поиска не отобразилась'
    assert 'tensor.ru' in html, 'сайт tensor.ru не найден среди результатов поиска'
    first_link_in_search_results = yandex_page.check_first_link_in_search_results()
    assert 'tensor.ru' == first_link_in_search_results, (
        f'Первая ссылка ведет не на tensor.ru, а на {first_link_in_search_results}'
        )

# def test_search_field_is_exist(browser):
#     yandex_main_page = TenzorSearch(browser)
#     yandex_main_page.go_to_site()
#     check_search_field = yandex_main_page.check_search_field()
#     assert check_search_field.is_enabled(), 'Строка поиска не найдена'
#     yandex_main_page.enter_word('Тензор')
#     yandex_main_page.click_enter()

# def test_suggest_table_is_visible(browser):
#     page = TenzorSearch(browser)
#     page.go_to_site()
#     page.enter_word('Тензор')
#     suggest = page.check_suggest_table()
#     assert suggest.is_displayed(), 'Таблица с подсказками suggest не видна пользователю'
#     page.click_enter()


# def test_check_search_results(browser):
#     page = TenzorSearch(browser)
#     page.go_to_site()
#     page.enter_word('Тензор')
#     page.click_enter()
#     body = page.check_search_result()
#     html = body.get_attribute('innerHTML')
#     assert body.is_displayed(), 'Cтраница результатов поиска не отобразилась'
#     assert 'tensor.ru' in html, 'Тензор не найден'
