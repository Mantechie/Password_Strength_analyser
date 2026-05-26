import secrets
import string


def generate_secure_password(length=16):
    """
    Generate a cryptographically secure password
    """

    # Minimum secure length
    if length < 8:
        length = 8

    # Character pools
    lowercase = string.ascii_lowercase

    uppercase = string.ascii_uppercase

    digits = string.digits

    symbols = "!@#$%^&*()-_=+[]{}<>?"

    # Combined pool
    all_characters = (
        lowercase +
        uppercase +
        digits +
        symbols
    )

    # Ensure password contains at least one
    # character from each category
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    # Fill remaining characters
    for _ in range(length - 4):

        password.append(
            secrets.choice(all_characters)
        )

    # Shuffle securely
    secrets.SystemRandom().shuffle(password)

    return "".join(password)