import os


def load_common_passwords():
    """
    Load common passwords into memory
    """

    file_path = os.path.join(
        os.path.dirname(__file__),
        "../data/common_passwords.txt"
    )

    with open(file_path, "r", encoding="utf-8") as file:

        passwords = {
            line.strip().lower()
            for line in file
        }

    return passwords


# Load passwords once for efficiency
COMMON_PASSWORDS = load_common_passwords()


def is_common_password(password):
    """
    Check if password exists in common password list
    """

    return password.lower() in COMMON_PASSWORDS