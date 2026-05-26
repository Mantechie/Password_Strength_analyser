import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Base Configuration
    """

    SECRET_KEY = os.getenv("SECRET_KEY")

    BASE_DIR = os.path.abspath(
        os.path.dirname(__file__)
    )

    SQLALCHEMY_DATABASE_URI = (
        os.getenv("DATABASE_URL")
        or
        "sqlite:///" + os.path.join(
            BASE_DIR,
            "database",
            "database.db"
        )
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Security Settings
    SESSION_COOKIE_HTTPONLY = True

    SESSION_COOKIE_SECURE = True

    REMEMBER_COOKIE_SECURE = True

    WTF_CSRF_ENABLED = True