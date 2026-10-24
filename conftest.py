
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    # Указываем путь к установленному ChromeDriver напрямую
    service = Service(
        r"D:\IT\WebDriver\bin\chromedriver.exe"
    )

    # Запускаем Google Chrome
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    yield driver

    # Закрываем браузер после завершения теста
    driver.quit()
