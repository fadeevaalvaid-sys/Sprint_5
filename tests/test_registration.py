
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helpers import generate_email, generate_password
from locators import NavigationLocators, RegistrationLocators


BASE_URL = "https://qa-stellarburgers.education-services.ru/"


def test_registration_with_short_password(driver):
    wait = WebDriverWait(driver, 15)

    # Открываем главную страницу
    driver.get(BASE_URL)

    # Переходим к форме входа
    wait.until(
        EC.element_to_be_clickable(
            NavigationLocators.LOGIN_BUTTON_HOME
        )
    ).click()

    # Переходим к форме регистрации
    wait.until(
        EC.element_to_be_clickable(
            RegistrationLocators.REGISTER_LINK
        )
    ).click()

    # Заполняем поля регистрации
    wait.until(
        EC.visibility_of_element_located(
            RegistrationLocators.NAME_INPUT
        )
    ).send_keys("Анастасия")

    driver.find_element(
        *RegistrationLocators.EMAIL_INPUT
    ).send_keys(generate_email())

    # Намеренно короткий пароль для проверки валидации
    driver.find_element(
        *RegistrationLocators.PASSWORD_INPUT
    ).send_keys("12345")

    # Убираем фокус с поля пароля
    driver.find_element(
        *RegistrationLocators.NAME_INPUT
    ).click()

    # Проверяем сообщение об ошибке
    password_error = wait.until(
        EC.visibility_of_element_located(
            RegistrationLocators.PASSWORD_ERROR
        )
    )

    assert password_error.text == "Некорректный пароль"

    # Нажимаем кнопку регистрации
    driver.find_element(
        *RegistrationLocators.REGISTER_BUTTON
    ).click()

    # Проверяем, что остались на странице регистрации
    wait.until(EC.url_contains("/register"))
    assert "/register" in driver.current_url


def test_successful_registration(driver):
    wait = WebDriverWait(driver, 15)

    # Генерируем уникальные данные для регистрации
    email = generate_email()
    password = generate_password()

    # Открываем главную страницу
    driver.get(BASE_URL)

    # Переходим к форме входа
    wait.until(
        EC.element_to_be_clickable(
            NavigationLocators.LOGIN_BUTTON_HOME
        )
    ).click()

    # Переходим к форме регистрации
    wait.until(
        EC.element_to_be_clickable(
            RegistrationLocators.REGISTER_LINK
        )
    ).click()

    # Заполняем поля регистрации
    wait.until(
        EC.visibility_of_element_located(
            RegistrationLocators.NAME_INPUT
        )
    ).send_keys("Анастасия")

    driver.find_element(
        *RegistrationLocators.EMAIL_INPUT
    ).send_keys(email)

    driver.find_element(
        *RegistrationLocators.PASSWORD_INPUT
    ).send_keys(password)

    # Нажимаем кнопку регистрации
    driver.find_element(
        *RegistrationLocators.REGISTER_BUTTON
    ).click()

    # Проверяем переход на страницу входа
    wait.until(EC.url_contains("/login"))
    assert "/login" in driver.current_url
