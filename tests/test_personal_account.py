from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import NavigationLocators, LoginLocators


BASE_URL = "https://qa-stellarburgers.education-services.ru/"
EMAIL = "anastasia_fadeeva_51@yandex.ru"
PASSWORD = "123456"


class TestPersonalAccount:

    def test_transition_to_personal_account(self, driver):
        """Проверяет переход в личный кабинет после авторизации."""
        wait = WebDriverWait(driver, 15)
        driver.get(BASE_URL)

        # Переходим к форме входа
        wait.until(
            EC.element_to_be_clickable(
                NavigationLocators.LOGIN_BUTTON_HOME
            )
        ).click()

        wait.until(EC.url_contains("/login"))

        # Вводим email
        wait.until(
            EC.visibility_of_element_located(
                LoginLocators.EMAIL_INPUT
            )
        ).send_keys(EMAIL)

        # Вводим пароль
        wait.until(
            EC.visibility_of_element_located(
                LoginLocators.PASSWORD_INPUT
            )
        ).send_keys(PASSWORD)

        # Нажимаем «Войти»
        wait.until(
            EC.element_to_be_clickable(
                LoginLocators.LOGIN_BUTTON
            )
        ).click()

        # Ждём успешной авторизации и перехода в личный кабинет
        wait.until(
            EC.element_to_be_clickable(
                NavigationLocators.PERSONAL_ACCOUNT_BUTTON
            )
        ).click()

        # Проверяем наличие кнопки «Выход»
        logout_button = wait.until(
            EC.visibility_of_element_located(
                LoginLocators.LOGOUT_BUTTON
            )
        )

        assert logout_button.is_displayed()