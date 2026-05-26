from app.security.header import (
    apply_security_headers
)


def register_security_middleware(app):
    """
    Register application security middleware
    """

    @app.after_request
    def secure_response(response):

        return apply_security_headers(response)
    