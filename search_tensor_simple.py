import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 


options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--incognito')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window() # увеличивает окно браузера
driver.get('https://ya.ru/')

time.sleep(10)

search_string = driver.find_element(By.NAME, 'text')

try:
    assert search_string.is_enabled()
    print('Строка поиска найдена')
except:
    print('Строка поиска не доступна')
time.sleep(10)

search_string.send_keys('Тензор')
try:
    suggest= driver.find_element(By.CSS_SELECTOR, 'ul[class*=mini-suggest]')
    assert suggest.is_displayed()
    print('Таблица с подсказками suggest появилась')
except:
    print('Таблица с подсказками suggest не видна пользователю')


search_string.send_keys(Keys.RETURN)
# time.sleep(10)
# WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located)

body = driver.find_element(By.TAG_NAME, 'body')
html = body.get_attribute('innerHTML')

try:
    assert body.is_displayed()
    print('Cтраница результатов поиска отобразилась')
except:
    print('Cтраница результатов поиска отобразилась')


try:
    assert 'tensor.ru' in html
    print('Есть ссылка на Тензор')
except:
    print('Тензор не найден')
time.sleep(3)
search_results = driver.find_elements(By.CSS_SELECTOR, 'ul[class*=serp-list]>li>div>div>div>a>b')
first_link = search_results[0].text
print(first_link)
try:
    assert 'tensor.ru' == first_link
    print('Первая ссылка ведет на tensor.ru')
except:
    print(f'Первая ссылка ведет не на tensor.ru, а на {first_link}')

driver.close()