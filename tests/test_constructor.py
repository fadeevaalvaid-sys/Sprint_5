
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import NavigationLocators, LoginLocators


BASE_URL = "https://qa-stellarburgers.education-services.ru/"
EMAIL = "anastasia_fadeeva_51@yandex.ru"
PASSWORD = "123456"


def login_and_open_personal_account(driver):
    """Авторизуется и открывает личный кабинет."""
    wait = WebDriverWait(driver, 15)
    driver.get(BASE_URL)

    # Переходим к форме входа
    wait.until(
        EC.element_to_be_clickable(
            NavigationLocators.LOGIN_BUTTON_HOME
        )
    ).click()

    wait.until(EC.url_contains("/login"))

    # Вводим email и пароль
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

    # Нажимаем «Войти»
    wait.until(
        EC.element_to_be_clickable(
            LoginLocators.LOGIN_BUTTON
        )
    ).click()

    # Открываем личный кабинет
    wait.until(
        EC.element_to_be_clickable(
            NavigationLocators.PERSONAL_ACCOUNT_BUTTON
        )
    ).click()

    # Проверяем, что личный кабинет открыт
    wait.until(
        EC.visibility_of_element_located(
            LoginLocators.LOGOUT_BUTTON
        )
    )


def test_transition_to_constructor(driver):
    """Проверяет переход в конструктор по ссылке «Конструктор»."""
    wait = WebDriverWait(driver, 15)
    login_and_open_personal_account(driver)

    wait.until(
        EC.element_to_be_clickable(
            NavigationLocators.CONSTRUCTOR_LINK
        )
    ).click()

    # Проверяем переход на главную страницу
    wait.until(EC.url_to_be(BASE_URL))


def test_transition_to_constructor_by_logo(driver):
    """Проверяет переход в конструктор по клику на логотип."""
    wait = WebDriverWait(driver, 15)
    login_and_open_personal_account(driver)

    wait.until(
        EC.element_to_be_clickable(
            NavigationLocators.LOGO_LINK
        )
    ).click()

     # Проверяем переход на главную страницу
    wait.until(EC.url_to_be(BASE_URL))