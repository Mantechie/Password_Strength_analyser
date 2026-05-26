import re

from .entropy_calculator import calculate_entropy

from .common_password_checker import (
    is_common_password
)

from .password_reuse_checker import (
    is_password_reused
)

def analyze_password(password):
    """
    Analyze password strength
    """

    score = 0

    weaknesses = []
    
    # -----------------------------
    # Password Reuse Detection
    # -----------------------------
    if is_password_reused(password):
        weaknesses.append(
            "Password was previously used"
        )
    
        return {
            "score": 0,
            "strength": "Very Weak",
            "entropy": 0,
            "crack_time": "Instantly",
            "feedback": weaknesses
        }
     
    # -----------------------------
    # Common Password Detection
    # -----------------------------
    if is_common_password(password):

        weaknesses.append(
            "This password is extremely common and unsafe"
        )

        return {
            "score": 0,
            "strength": "Very Weak",
            "entropy": 0,
            "crack_time": "Instantly",
            "feedback": weaknesses
        }

    # -----------------------------
    # Length Check
    # -----------------------------
    if len(password) >= 12:
        score += 2

    elif len(password) >= 8:
        score += 1

    else:
        weaknesses.append(
            "Password is too short"
        )

    # -----------------------------
    # Uppercase Check
    # -----------------------------
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        weaknesses.append(
            "Add uppercase letters"
        )

    # -----------------------------
    # Lowercase Check
    # -----------------------------
    if re.search(r"[a-z]", password):
        score += 1
    else:
        weaknesses.append(
            "Add lowercase letters"
        )

    # -----------------------------
    # Number Check
    # -----------------------------
    if re.search(r"\d", password):
        score += 1
    else:
        weaknesses.append(
            "Include numbers"
        )

    # -----------------------------
    # Special Character Check
    # -----------------------------
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        weaknesses.append(
            "Use special characters"
        )

    # -----------------------------
    # Sequential Pattern Detection
    # -----------------------------
    sequential_patterns = [
        "12345",
        "abcdef",
        "qwerty",
        "password"
    ]

    lower_password = password.lower()

    for pattern in sequential_patterns:

        if pattern in lower_password:

            weaknesses.append(
                f"Contains predictable pattern: {pattern}"
            )

            score -= 1

    # -----------------------------
    # Repeated Character Detection
    # -----------------------------
    if re.search(r"(.)\1{2,}", password):

        weaknesses.append(
            "Contains repeated characters"
        )

        score -= 1

    # -----------------------------
    # Entropy Calculation
    # -----------------------------
    entropy_data = calculate_entropy(password)

    entropy = entropy_data["entropy"]

    crack_time = entropy_data["crack_time"]

    # Entropy-Based Bonus
    if entropy >= 80:
        score += 2

    elif entropy >= 60:
        score += 1

    # Prevent negative score
    if score < 0:
        score = 0

    # -----------------------------
    # Final Strength Classification
    # -----------------------------
    if score <= 2:
        strength = "Weak"

    elif score <= 4:
        strength = "Moderate"

    elif score <= 6:
        strength = "Strong"

    else:
        strength = "Very Strong"

    return {
        "score": score,
        "strength": strength,
        "entropy": entropy,
        "crack_time": crack_time,
        "feedback": weaknesses
    }