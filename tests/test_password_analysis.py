from app.services.password_analyser import (
    analyze_password
)


def test_weak_password(app):

    with app.app_context():

        result = analyze_password("12345")

        assert result["strength"] in [
            "Weak",
            "Very Weak"
        ]


def test_strong_password(app):

    with app.app_context():

        result = analyze_password(
            "Quantum@Shield2048!"
        )

        assert result["strength"] in [
            "Strong",
            "Very Strong"
        ]


def test_entropy_exists(app):

    with app.app_context():

        result = analyze_password(
            "Secure@Password123"
        )

        assert "entropy" in result


def test_feedback_exists(app):

    with app.app_context():

        result = analyze_password("password")

        assert "feedback" in result