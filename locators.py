
from selenium.webdriver.common.by import By


class NavigationLocators:
    # Кнопка «Войти в аккаунт» на главной странице
    LOGIN_BUTTON_HOME = (
        By.XPATH,
        "//button[normalize-space()='Войти в аккаунт']"
    )

    # Текст «Личный Кабинет» в шапке сайта
    PERSONAL_ACCOUNT_BUTTON = (
        By.XPATH,
        "//p[normalize-space()='Личный Кабинет']"
    )

    # Ссылка «Конструктор»
    CONSTRUCTOR_LINK = (
        By.XPATH,
        "//a[@href='/' and .//p[normalize-space()='Конструктор']]"
    )

    # Ссылка на логотип Stellar Burgers
    LOGO_LINK = (
        By.XPATH,
        "//div[contains(@class, 'header__logo')]//a[@href='/']"
    )


class RegistrationLocators:
    # Поле ввода имени
    NAME_INPUT = (
        By.XPATH,
        "//label[normalize-space()='Имя']/following-sibling::input"
    )

    # Поле ввода email
    EMAIL_INPUT = (
        By.XPATH,
        "//label[normalize-space()='Email']/following-sibling::input"
    )

    # Поле ввода пароля
    PASSWORD_INPUT = (
        By.CSS_SELECTOR,
        "input[type='password']"
    )

    # Кнопка «Зарегистрироваться» в форме регистрации
    REGISTER_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Зарегистрироваться']"
    )

    # Ссылка «Зарегистрироваться» на форме входа
    REGISTER_LINK = (
        By.CSS_SELECTOR,
        "a[href='/register']"
    )

    # Ссылка «Войти» под формой регистрации
    LOGIN_LINK_FROM_REGISTER = (
        By.CSS_SELECTOR,
        "a[href='/login']"
    )

    # Сообщение об ошибке при коротком пароле
    PASSWORD_ERROR = (
        By.XPATH,
        "//*[normalize-space()='Некорректный пароль']"
    )


class LoginLocators:
    # Поле email на форме входа
    EMAIL_INPUT = (
        By.XPATH,
        "//label[normalize-space()='Email']/following-sibling::input"
    )

    # Поле пароля на форме входа
    PASSWORD_INPUT = (
        By.CSS_SELECTOR,
        "input[type='password']"
    )

    # Кнопка «Войти» на форме входа
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Войти']"
    )

    # Ссылка «Восстановить пароль»
    FORGOT_PASSWORD_LINK = (
        By.CSS_SELECTOR,
        "a[href='/forgot-password']"
    )

    # Ссылка «Войти» на странице восстановления пароля
    LOGIN_LINK_FROM_FORGOT_PASSWORD = (
        By.CSS_SELECTOR,
        "a[href='/login']"
    )

    # Кнопка «Конструктор» после успешного входа
    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Конструктор']"
    )

    # Кнопка «Выход» в личном кабинете
    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Выход']"
    )


class ConstructorLocators:
    # Раздел «Булки»
    BUNS_TAB = (
        By.XPATH,
        "//div[contains(@class, 'tab_tab')][.//span[normalize-space()='Булки']]"
    )

    # Раздел «Соусы»
    SAUCES_TAB = (
        By.XPATH,
        "//div[contains(@class, 'tab_tab')][.//span[normalize-space()='Соусы']]"
    )

    # Раздел «Начинки»
    FILLINGS_TAB = (
        By.XPATH,
        "//div[contains(@class, 'tab_tab')][.//span[normalize-space()='Начинки']]"
    )

    # Активная вкладка. Не зависит от окончания сгенерированного хэша
    ACTIVE_TAB = (
        By.CSS_SELECTOR,
        "[class*='tab_tab_type_current']"
    )
