from selenium.webdriver.common.by import By

from pages.images_page import ImageSearchPage


class Locator:
    '''Вспомогательны класс с данными для поиска картинок.'''

    LOCATOR_YANDEX_SEARCH_FIELD = (By.NAME, 'text')
    LOCATOR_YANDEX_MENU = (By.CSS_SELECTOR, 'a[title*="Все сервисы"]')
    LOCATOR_YANDEX_PICTURES = (By.LINK_TEXT, "Картинки")
    LOCATOR_IMAGE_CATEGORY = (
        By.CSS_SELECTOR, 'div[class*=PopularRequestList]>div'
        )
    LOCATOR_INPUT_FIELD = (By.CSS_SELECTOR, 'input[class*=input]')
    LOCATOR_FIRST_PICTURE = (By.CSS_SELECTOR, 'div[class*="serp-item_pos_0"]')
    LOCATOR_PICTURE_PREVIEW = (By.CLASS_NAME, 'MMImage-Origin')
    LOCATOR_BUTTON_NEXT = (
        By.CSS_SELECTOR, 'div[class*=CircleButton_type_next]'
        )
    LOCATOR_BUTTON_PREV = (
        By.CSS_SELECTOR, 'div[class*=CircleButton_type_prev]'
        )
    PICTURES_URL = 'https://ya.ru/images/'
    NUMDER_OF_SECOND_WINDOW = 1


def test_search_image(browser):
    '''Тестирующая функция для проверки поиска и отображения картинок.'''

    page = ImageSearchPage(browser)
    page.go_to_site()
    page.find_and_click_element(Locator.LOCATOR_YANDEX_SEARCH_FIELD)
    menu_bar = page.check_menu_bar_on_page()

    assert menu_bar is not None, (
        'Кнопка меню(все сервисы) не видна на странице'
        )

    page.do_click(Locator.LOCATOR_YANDEX_MENU)
    page.find_and_click_element(Locator.LOCATOR_YANDEX_PICTURES)
    page.switch_to_window(Locator.NUMDER_OF_SECOND_WINDOW)
    current_url_site = page.current_url()

    assert Locator.PICTURES_URL == current_url_site, (
        f'Текущий урл страницы {current_url_site} не соответсвует '
        f'необходимому - {Locator.PICTURES_URL}'
    )

    images_category = page.find_elements(Locator.LOCATOR_IMAGE_CATEGORY)
    first_category_images = images_category[0]
    name_first_category_images = first_category_images.text.lower()
    first_category_images.click()
    input_field = page.find_element(Locator.LOCATOR_INPUT_FIELD)
    input_field_text = input_field.get_attribute('value').lower()

    assert name_first_category_images == input_field_text, (
        f'{name_first_category_images} не совпадает '
        f'с введенным значением в поле ввода {input_field_text}'
    )

    page.find_and_click_element(Locator.LOCATOR_FIRST_PICTURE)
    picture_prev = page.find_element(Locator.LOCATOR_PICTURE_PREVIEW)
    picture_size = picture_prev.size.get('height')

    assert picture_size > 0, ('Картинка не отобразилась')

    picture_prev = picture_prev.get_attribute('src')
    page.find_and_click_element(Locator.LOCATOR_BUTTON_NEXT)
    picture_next = page.find_element(Locator.LOCATOR_PICTURE_PREVIEW)
    picture_next = picture_next.get_attribute('src')

    assert picture_next != picture_prev, (
        f'Картинка не сменилась последующаяй картинка: {picture_next} '
        f'совпадает с предыдующей картинкой{picture_prev}'
    )

    page.find_and_click_element(Locator.LOCATOR_BUTTON_PREV)
    picture_before = page.find_element(Locator.LOCATOR_PICTURE_PREVIEW)
    picture_before = picture_before.get_attribute('src')

    assert picture_before == picture_prev, (
        f'Картинка не сменилась: {picture_before} '
        f'не совпадает с прежней картинкой{picture_prev}'
    )
