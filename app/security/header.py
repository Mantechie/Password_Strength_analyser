def apply_security_headers(response):
    """
    Apply secure HTTP headers
    """

    # Prevent MIME sniffing
    response.headers[
        "X-Content-Type-Options"
    ] = "nosniff"

    # Prevent clickjacking
    response.headers[
        "X-Frame-Options"
    ] = "DENY"

    # Enable browser XSS filtering
    response.headers[
        "X-XSS-Protection"
    ] = "1; mode=block"

    # Referrer policy
    response.headers[
        "Referrer-Policy"
    ] = "strict-origin-when-cross-origin"

    # Content Security Policy
    response.headers[
        "Content-Security-Policy"
    ] = (
        "default-src 'self'; "
        "script-src 'self'; "
        "style-src 'self';"
    )

    return response

