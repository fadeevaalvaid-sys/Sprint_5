from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import (
    NavigationLocators,
    RegistrationLocators,
    LoginLocators,
)


BASE_URL = "https://qa-stellarburgers.education-services.ru/"
EMAIL = "anastasia_fadeeva_51@yandex.ru"
PASSWORD = "123456"


def login(driver):
    """Выполняет вход в аккаунт."""
    wait = WebDriverWait(driver, 15)

    wait.until(
        EC.visibility_of_element_located(
            LoginLocators.EMAIL_INPUT
        )
    ).send_keys(EMAIL)

    wait.until(
        EC.visibility_of_element_located(
            LoginLocators.PASSWORD_INPUT
        )
    ).send_keys(PASSWORD)

    wait.until(
        EC.element_to_be_clickable(
            LoginLocators.LOGIN_BUTTON
        )
    ).click()

    # Ждём появления кнопки «Личный кабинет»
    wait.until(
        EC.element_to_be_clickable(
            NavigationLocators.PERSONAL_ACCOUNT_BUTTON
        )
    )


def logout(driver):
    """Выходит из авторизованного аккаунта."""
    wait = WebDriverWait(driver, 15)

    # Открываем личный кабинет
    wait.until(
        EC.element_to_be_clickable(
            NavigationLocators.PERSONAL_ACCOUNT_BUTTON
        )
    ).click()

    # Находим кнопку «Выход»
    logout_button = wait.until(
        EC.element_to_be_clickable(
            LoginLocators.LOGOUT_BUTTON
        )
    )
    logout_button.click()

    # Ждём перехода на страницу входа
    wait.until(EC.url_contains("/login"))


class TestLogin:

    def test_login_from_home_button(self, driver):
        """Проверяет вход через кнопку на главной странице."""
        wait = WebDriverWait(driver, 15)
        driver.get(BASE_URL)

        wait.until(
            EC.element_to_be_clickable(
                NavigationLocators.LOGIN_BUTTON_HOME
            )
        ).click()

        wait.until(EC.url_contains("/login"))

        login(driver)
        logout(driver)

        assert "/login" in driver.current_url

    def test_login_from_personal_account(self, driver):
        """Проверяет вход через кнопку «Личный кабинет»."""
        wait = WebDriverWait(driver, 15)
        driver.get(BASE_URL)

        wait.until(
            EC.element_to_be_clickable(
                NavigationLocators.PERSONAL_ACCOUNT_BUTTON
            )
        ).click()

        wait.until(EC.url_contains("/login"))

        login(driver)
        logout(driver)

        assert "/login" in driver.current_url

    def test_login_from_registration_form(self, driver):
        """Проверяет вход по ссылке в форме регистрации."""
        wait = WebDriverWait(driver, 15)
        driver.get(BASE_URL + "register")

        wait.until(
            EC.element_to_be_clickable(
                RegistrationLocators.LOGIN_LINK_FROM_REGISTER
            )
        ).click()

        wait.until(EC.url_contains("/login"))

        login(driver)
        logout(driver)

        assert "/login" in driver.current_url

    def test_login_from_forgot_password_form(self, driver):
        """Проверяет вход по ссылке со страницы восстановления пароля."""
        wait = WebDriverWait(driver, 15)
        driver.get(BASE_URL + "forgot-password")

        wait.until(
            EC.element_to_be_clickable(
                LoginLocators.LOGIN_LINK_FROM_FORGOT_PASSWORD
            )
        ).click()

        wait.until(EC.url_contains("/login"))

        login(driver)
        logout(driver)

        assert "/login" in driver.current_url