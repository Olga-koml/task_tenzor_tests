# Рабочий код для начала работы. 
# Автоматизация и проверки: открывает сайт ya.ru - проверяется есть ли строка поиска, 
# в поиск вводит Тензор, проверяет появляется ли таблица с подсказками, нажимает ентер,
# проверяет нашлось ли что-то, отобразилась ли страница результатов поиска, есть ли сайт 
# tensor.ru в результатах поиска, ведет ли первая ссылка на этот сайт


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
 

options = Options()
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
# time.sleep(10)

search_string.send_keys('Тензор')

try:
    suggest= driver.find_element(By.CSS_SELECTOR, 'ul[class*=mini-suggest]')
    assert suggest.is_displayed()
    print('Таблица с подсказками suggest появилась')
except:
    print('Таблица с подсказками suggest не видна пользователю')

search_string.send_keys(Keys.RETURN)
time.sleep(10)

# with open('filename.txt', 'w') as f:
#     sys.stdout = f # Change the standard output to the file we created.
#     print(driver.page_source)
    # sys.stdout = original_stdout 
try:
    assert "Ничего не нашли" not in driver.page_source
    print('что-то нашлось')
except:
    print('NOTFOUND')

body = driver.find_element(By.TAG_NAME, 'body')
html = body.get_attribute('innerHTML')


try:
    assert body.is_displayed()
    print('Cтраница результатов поиска отобразилась')
except:
    print('Cтраница результатов поиска не отобразилась')


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