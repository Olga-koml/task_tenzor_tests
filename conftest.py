import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def browser():
    # код для случаев если нужно качать драйвер
    # driver = webdriver.Chrome(executable_path="./chromedriver")
    # yield driver
    # driver.quit()


    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--incognito')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    # driver.get('https://ya.ru/')
    yield driver
    driver.quit()