# Автотесты Stellar Burgers

Проект содержит UI-автотесты веб-приложения Stellar Burgers с использованием Selenium и pytest.

## Покрытые сценарии

### Регистрация
- Проверка ошибки при вводе короткого пароля.
- Проверка успешной регистрации с уникальными данными.

### Вход в аккаунт
- Вход через кнопку на главной странице.
- Вход через личный кабинет.
- Вход со страницы регистрации.
- Вход со страницы восстановления пароля.

### Личный кабинет
- Переход в личный кабинет.
- Выход из аккаунта.

### Конструктор
- Переход в конструктор по ссылке «Конструктор».
- Переход в конструктор по логотипу Stellar Burgers.
- Проверка раздела «Булки» по умолчанию.
- Проверка переключения между разделами «Булки», «Соусы» и «Начинки».

## Папки

```text
Sprint_5/
├── tests/
│   ├── test_registration.py
│   ├── test_login.py
│   ├── test_personal_account.py
│   ├── test_constructor.py
│   ├── test_constructor_sections.py
│   └── test_logout.py
├── conftest.py
├── helpers.py
├── locators.py
├── requirements.txt
├── .gitignore
└── README.md
```

### 1. Клонирование репозитория

```bash
git clone https://github.com/fadeevaalvaid-sys/Sprint-5.git
```


### 2. Запуск тестов

Запуск всех тестов:

```bash
python -m pytest -v
```

Запуск тестов регистрации:

```bash
python -m pytest -v tests/test_registration.py
```

