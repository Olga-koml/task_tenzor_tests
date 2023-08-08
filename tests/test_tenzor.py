from pages.tenzor_search_page import TenzorSearchPage


SEARCH_WORD = 'Тензор'
SITE_TENZOR = 'tensor.ru'
NOT_FOUND = 'Ничего не нашли'


def test_search_tenzor(browser):
    '''Функция тестирующая поиск по слову Тензор.'''

    yandex_page = TenzorSearchPage(browser)
    yandex_page.go_to_site()
    check_search_field = yandex_page.check_search_field()
    assert check_search_field.is_enabled(), 'Строка поиска не найдена'

    yandex_page.enter_word(SEARCH_WORD)
    suggest = yandex_page.check_suggest_table()
    assert suggest.is_displayed(), (
        'Таблица с подсказками suggest не видна пользователю'
        )

    yandex_page.click_enter()
    assert NOT_FOUND not in yandex_page.page_source(), (
        f'По данному запросу - {SEARCH_WORD} - ничего не нашли'
        )

    body = yandex_page.check_search_result()
    assert body.is_displayed(), 'Cтраница результатов поиска не отобразилась'

    html = body.get_attribute('innerHTML')
    assert SITE_TENZOR in html, (
        f'Сайт {SITE_TENZOR} не найден среди результатов поиска'
        )

    first_link_in_results = yandex_page.check_first_link_in_search_results()
    assert SITE_TENZOR == first_link_in_results, (
        f'Первая ссылка ведет не на tensor.ru, '
        f'а на {first_link_in_results}'
        )
