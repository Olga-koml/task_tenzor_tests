import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager  # для фаерфокс


@pytest.fixture(scope="session")
def browser():

    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--incognito')
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
        )
    driver.maximize_window()
    # driver.get('https://ya.ru/')
    yield driver
    driver.quit()

    # Код для случаев если нужно качать драйвер

    # binary_yandex_driver_file = './yandexdriver/yandexdriver.exe' # path to driver
    # service = Service(executable_path=binary_yandex_driver_file)
    # options = webdriver.ChromeOptions()
    # driver = webdriver.Chrome(service=service, options=options)
    # driver.maximize_window()
    # # driver.get('https://ya.ru/')
    # yield driver
    # driver.quit()
