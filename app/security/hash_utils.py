from app.extension import bcrypt


def hash_password(password):
    """
    Generate secure bcrypt hash
    """

    hashed_password = bcrypt.generate_password_hash(
        password
    ).decode("utf-8")

    return hashed_password


def verify_password(password, hashed_password):
    """
    Verify password against bcrypt hash
    """

    return bcrypt.check_password_hash(
        hashed_password,
        password
    )