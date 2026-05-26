from app.models.password_model import (
    PasswordEntry
)

from app.security.hash_utils import (
    verify_password
)


def is_password_reused(password):
    """
    Check if password was previously used
    """

    records = PasswordEntry.query.all()

    for record in records:

        if verify_password(
            password,
            record.hashed_password
        ):
            return True

    return False