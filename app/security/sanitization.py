import bleach


def sanitize_input(user_input):
    """
    Sanitize user input to prevent XSS
    """

    if not isinstance(user_input, str):
        return ""

    sanitized = bleach.clean(
        user_input,
        tags=[],
        attributes={},
        strip=True
    )

    return sanitized.strip()