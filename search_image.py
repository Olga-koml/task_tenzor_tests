import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys
 

def get_attributes(driver, element) -> dict:
    return driver.execute_script(
        """
        let attr = arguments[0].attributes;
        let items = {}; 
        for (let i = 0; i < attr.length; i++) {
            items[attr[i].name] = attr[i].value;
        }
        return items;
        """,
        element
    )

options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--incognito')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window() 
driver.get('https://ya.ru/')
time.sleep(10)
search_bar = driver.find_element(By.NAME, 'text')
search_bar.click()


time.sleep(2)
# results = driver.find_element(By.TAG_NAME, 'html')
time.sleep(1)
menu_bar = driver.find_element(By.CSS_SELECTOR, 'a[title*="Все сервисы"]')
time.sleep(2)
# try:
#     assert "Все сервисы" in results
#     print('Кнопка все сервисы есть в результатах')
# except:
#     print('Кнопки все серверы нет')

menu_bar.click()
time.sleep(2)

images = driver.find_element(By.LINK_TEXT, "Картинки")
time.sleep(1)
images.click()
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])
current_url_site = driver.current_url
try:
    assert 'https://ya.ru/images/' == current_url_site
    print("Текущий урл соответсвует")
except:
    print("НЕ соответсвует", current_url_site)
print(f'Switch to title: "{driver.title}"')

time.sleep(1)

# первый результат поиска
images = driver.find_elements(By.CSS_SELECTOR, 'div[class*=PopularRequestList]>div')

time.sleep(1)
# images = driver.find_elements(By.CLASS_NAME, 'cl-teaser__link')

first_category_images = images[0]
name_first_category_images = first_category_images.text.lower()
# print('00000000000000000', first_category_images.get_attribute('data-grid-text'))
first_category_images.click()
time.sleep(2)


input_field = driver.find_element(By.CSS_SELECTOR, 'input[class*=input]')
# text_1 = get_attributes(driver, search_string)
input_field_text = input_field.get_attribute('value').lower()

try:
    assert name_first_category_images == input_field_text
    print(f'{name_first_category_images} совпадает {input_field_text}')
except:
    print(f'{name_first_category_images} не совпадает с введенным значением {input_field_text}')


# pic = driver.find_elements(By.CSS_SELECTOR, 'div[class*="serp-list"]>div') # так если реклама сверху открывает ее
pic = driver.find_element(By.CSS_SELECTOR, 'div[class*="serp-item_pos_0"]') # нахожу первую картинку
pic.click()
time.sleep(2)
picture_prev = driver.find_element(By.CLASS_NAME, 'MMImage-Origin')
picture_size = picture_prev.size.get('height')
try:
    assert picture_size > 0
    print('SIZEE', picture_size)
except:
    print('Картинка не отобразилась')
picture_prev = picture_prev.get_attribute('src')
print('PICTURE11', picture_prev)
button_next = driver.find_element(By.CSS_SELECTOR, 'div[class*=CircleButton_type_next]')
time.sleep(1)
button_next.click()
picture_next = driver.find_element(By.CLASS_NAME, 'MMImage-Origin')
picture_next = picture_next.get_attribute('src')
print('PICTURE22', picture_next)
try:
    assert picture_next != picture_prev
    print( 'Картинка сменилась')
except:
    print(f'Картинка не сменилась: {picture_next} совпадает с предыдующей картинкой{picture_prev}')


time.sleep(1)
button_prev = driver.find_element(By.CSS_SELECTOR, 'div[class*=CircleButton_type_prev]')
time.sleep(1)
button_prev.click()
picture_before = driver.find_element(By.CLASS_NAME, 'MMImage-Origin')
picture_before = picture_before.get_attribute('src')
print('PICTURE_BEFORE', picture_before)
try:
    assert picture_before == picture_prev
    print( 'Картинка при нажатии назад остается прежней')
except:
    print(f'Картинка не сменилась: {picture_before} не совпадает с прежней картинкой{picture_prev}')
time.sleep(3)

driver.quit()
