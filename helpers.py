
import secrets
import string


def generate_email():
    """Генерирует уникальный email для регистрации."""
    unique_part = secrets.token_hex(8)
    return f"student_{unique_part}@yandex.ru"


def generate_password(length=10):
    """Генерирует случайный пароль заданной длины."""
    if length < 6:
        raise ValueError("Длина пароля должна быть не менее 6 символов")

    characters = string.ascii_letters + string.digits
    return "".join(
        secrets.choice(characters)
        for _ in range(length)
    )
