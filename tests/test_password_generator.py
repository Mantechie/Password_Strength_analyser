from app.services.password_generator import (
    generate_secure_password
)


def test_password_length():

    password = generate_secure_password(20)

    assert len(password) == 20


def test_password_contains_uppercase():

    password = generate_secure_password()

    assert any(char.isupper()
               for char in password)


def test_password_contains_lowercase():

    password = generate_secure_password()

    assert any(char.islower()
               for char in password)


def test_password_contains_digits():

    password = generate_secure_password()

    assert any(char.isdigit()
               for char in password)