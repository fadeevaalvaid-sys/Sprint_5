
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import NavigationLocators, LoginLocators


BASE_URL = "https://qa-stellarburgers.education-services.ru/"
EMAIL = "anastasia_fadeeva_51@yandex.ru"
PASSWORD = "123456"


def test_logout_from_personal_account(driver):
    """Проверяет выход из аккаунта по кнопке «Выйти»."""

    wait = WebDriverWait(driver, 15)

    # Открываем главную страницу
    driver.get(BASE_URL)

    # Переходим к форме входа
    wait.until(
        EC.element_to_be_clickable(
            NavigationLocators.LOGIN_BUTTON_HOME
        )
    ).click()

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

    # Переходим в личный кабинет
    wait.until(
        EC.element_to_be_clickable(
            NavigationLocators.PERSONAL_ACCOUNT_BUTTON
        )
    ).click()

    # Ожидаем появления кнопки «Выйти»
    wait.until(
        EC.visibility_of_element_located(
            LoginLocators.LOGOUT_BUTTON
        )
    )

    # Нажимаем «Выйти»
    wait.until(
        EC.element_to_be_clickable(
            LoginLocators.LOGOUT_BUTTON
        )
    ).click()

    # Проверяем, что после выхода открылась страница входа
    wait.until(EC.url_contains("/login"))

    # Проверяем, что отображается поле email
    wait.until(
        EC.visibility_of_element_located(
            LoginLocators.EMAIL_INPUT
        )
    )
