from flask import Flask

from .config import Config

from .extension import (
    db,
    bcrypt,
    limiter
)

from .middleware.security_middleware import (
    register_security_middleware
)

from .api import api

from .api.routes import *

from .routes import main

def create_app():
    """
    Application Factory Function
    """

    app = Flask(__name__)

    # Load configurations
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    limiter.init_app(app)

    # Register routes
    from .routes import main
    app.register_blueprint(main)
    # Register security middleware
    register_security_middleware(app)
    
    app.register_blueprint(api)

    # Create database tables
    with app.app_context():
        db.create_all()
    
    # Global Error Handlers

    @app.errorhandler(404)
    def not_found(error):

        return {
            "error": "Resource not found"
        }, 404


    @app.errorhandler(500)
    def internal_error(error):

        return {
            "error": "Internal server error"
        }, 500


    @app.errorhandler(429)
    def rate_limit_error(error):

        return {
            "error": "Too many requests"
        }, 429

    return app
