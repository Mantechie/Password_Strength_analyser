from app.security.sanitization import (
    sanitize_input
)

from app.security.hash_utils import (
    hash_password,
    verify_password
)


def test_xss_sanitization():

    malicious_input = (
        "<script>alert(1)</script>"
    )

    clean_input = sanitize_input(
        malicious_input
    )

    assert "<script>" not in clean_input


def test_password_hashing():

    password = "Secure@123"

    hashed = hash_password(password)

    assert hashed != password


def test_password_verification():

    password = "Secure@123"

    hashed = hash_password(password)

    assert verify_password(
        password,
        hashed
    ) is True