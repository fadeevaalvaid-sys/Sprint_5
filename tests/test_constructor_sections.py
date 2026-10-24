from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import ConstructorLocators


BASE_URL = "https://qa-stellarburgers.education-services.ru/"


def click_section_and_check(driver, section_locator):
    """Переключает раздел и проверяет, что он стал активным."""
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.element_to_be_clickable(section_locator)
    ).click()

    # Ожидаем, что выбранный раздел станет активным
    wait.until(
        lambda d: "tab_tab_type_current__2BEPc" in
        d.find_element(*section_locator).get_attribute("class").split()
    )


def test_buns_section_opened_by_default(driver):
    """Проверяет, что при открытии конструктора выбраны «Булки»."""
    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 10)

    buns_tab = wait.until(
        EC.visibility_of_element_located(
            ConstructorLocators.BUNS_TAB
        )
    )

    assert "tab_tab_type_current__2BEPc" in buns_tab.get_attribute(
        "class"
    ).split()


def test_buns_to_sauces(driver):
    """Проверяет переход из «Булок» в «Соусы»."""
    driver.get(BASE_URL)

    click_section_and_check(
        driver,
        ConstructorLocators.SAUCES_TAB
    )


def test_buns_to_fillings(driver):
    """Проверяет переход из «Булок» в «Начинки»."""
    driver.get(BASE_URL)

    click_section_and_check(
        driver,
        ConstructorLocators.FILLINGS_TAB
    )


def test_sauces_to_buns(driver):
    """Проверяет переход из «Соусов» в «Булки»."""
    driver.get(BASE_URL)

    click_section_and_check(
        driver,
        ConstructorLocators.SAUCES_TAB
    )
    click_section_and_check(
        driver,
        ConstructorLocators.BUNS_TAB
    )


def test_sauces_to_fillings(driver):
    """Проверяет переход из «Соусов» в «Начинки»."""
    driver.get(BASE_URL)

    click_section_and_check(
        driver,
        ConstructorLocators.SAUCES_TAB
    )
    click_section_and_check(
        driver,
        ConstructorLocators.FILLINGS_TAB
    )


def test_fillings_to_buns(driver):
    """Проверяет переход из «Начинок» в «Булки»."""
    driver.get(BASE_URL)

    click_section_and_check(
        driver,
        ConstructorLocators.FILLINGS_TAB
    )
    click_section_and_check(
        driver,
        ConstructorLocators.BUNS_TAB
    )


def test_fillings_to_sauces(driver):
    """Проверяет переход из «Начинок» в «Соусы»."""
    driver.get(BASE_URL)

    click_section_and_check(
        driver,
        ConstructorLocators.FILLINGS_TAB
    )
    click_section_and_check(
        driver,
        ConstructorLocators.SAUCES_TAB
    )
