from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import ConstructorLocators


BASE_URL = "https://qa-stellarburgers.education-services.ru/"


def click_section_and_check(driver, section_locator, section_name):
    """Переключает раздел и проверяет, что он стал активным."""
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.element_to_be_clickable(section_locator)
    ).click()

    def expected_section_is_active(d):
        active_tab = d.find_element(*ConstructorLocators.ACTIVE_TAB)
        return section_name in active_tab.text

    wait.until(expected_section_is_active)
    return True


class TestConstructorSections:

    def test_buns_section_opened_by_default(self, driver):
        driver.get(BASE_URL)

        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.visibility_of_element_located(ConstructorLocators.BUNS_TAB)
        )

        active_tab = wait.until(
            EC.visibility_of_element_located(ConstructorLocators.ACTIVE_TAB)
        )

        assert "Булки" in active_tab.text

    def test_buns_to_sauces(self, driver):
        driver.get(BASE_URL)

        assert click_section_and_check(
            driver, ConstructorLocators.SAUCES_TAB, "Соусы"
        )

    def test_buns_to_fillings(self, driver):
        driver.get(BASE_URL)

        assert click_section_and_check(
            driver, ConstructorLocators.FILLINGS_TAB, "Начинки"
        )

    def test_sauces_to_buns(self, driver):
        driver.get(BASE_URL)
        click_section_and_check(
            driver, ConstructorLocators.SAUCES_TAB, "Соусы"
        )

        assert click_section_and_check(
            driver, ConstructorLocators.BUNS_TAB, "Булки"
        )

    def test_sauces_to_fillings(self, driver):
        driver.get(BASE_URL)
        click_section_and_check(
            driver, ConstructorLocators.SAUCES_TAB, "Соусы"
        )

        assert click_section_and_check(
            driver, ConstructorLocators.FILLINGS_TAB, "Начинки"
        )

    def test_fillings_to_buns(self, driver):
        driver.get(BASE_URL)
        click_section_and_check(
            driver, ConstructorLocators.FILLINGS_TAB, "Начинки"
        )

        assert click_section_and_check(
            driver, ConstructorLocators.BUNS_TAB, "Булки"
        )

    def test_fillings_to_sauces(self, driver):
        driver.get(BASE_URL)
        click_section_and_check(
            driver, ConstructorLocators.FILLINGS_TAB, "Начинки"
        )

        assert click_section_and_check(
            driver, ConstructorLocators.SAUCES_TAB, "Соусы"
        )