from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import ConstructorLocators


BASE_URL = "https://qa-stellarburgers.education-services.ru/"


def click_section_and_check(driver, section_locator):
    """Переключает раздел и ожидает, что вкладка станет активной."""
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.element_to_be_clickable(section_locator)
    ).click()

    wait.until(
        lambda d: "tab_tab_type_current"
        in d.find_element(*section_locator).get_attribute("class")
    )

    return (
        "tab_tab_type_current"
        in driver.find_element(*section_locator).get_attribute("class")
    )


class TestConstructorSections:

    def test_buns_section_opened_by_default(self, driver):
        driver.get(BASE_URL)

        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.visibility_of_element_located(ConstructorLocators.BUNS_TAB)
        )

        active_class = driver.find_element(
            *ConstructorLocators.BUNS_TAB
        ).get_attribute("class")

        assert "tab_tab_type_current" in active_class

    def test_buns_to_sauces(self, driver):
        driver.get(BASE_URL)

        assert click_section_and_check(
            driver, ConstructorLocators.SAUCES_TAB
        )

    def test_buns_to_fillings(self, driver):
        driver.get(BASE_URL)

        assert click_section_and_check(
            driver, ConstructorLocators.FILLINGS_TAB
        )

    def test_sauces_to_buns(self, driver):
        driver.get(BASE_URL)
        click_section_and_check(driver, ConstructorLocators.SAUCES_TAB)

        assert click_section_and_check(
            driver, ConstructorLocators.BUNS_TAB
        )

    def test_sauces_to_fillings(self, driver):
        driver.get(BASE_URL)
        click_section_and_check(driver, ConstructorLocators.SAUCES_TAB)

        assert click_section_and_check(
            driver, ConstructorLocators.FILLINGS_TAB
        )

    def test_fillings_to_buns(self, driver):
        driver.get(BASE_URL)
        click_section_and_check(driver, ConstructorLocators.FILLINGS_TAB)

        assert click_section_and_check(
            driver, ConstructorLocators.BUNS_TAB
        )

    def test_fillings_to_sauces(self, driver):
        driver.get(BASE_URL)
        click_section_and_check(driver, ConstructorLocators.FILLINGS_TAB)

        assert click_section_and_check(
            driver, ConstructorLocators.SAUCES_TAB
        )