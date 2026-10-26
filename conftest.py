
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """Создаёт браузер Chrome и закрывает его после теста."""
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()
