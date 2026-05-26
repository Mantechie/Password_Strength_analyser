import math
import re


def calculate_entropy(password):
    """
    Calculate password entropy
    """

    pool_size = 0

    # Lowercase
    if re.search(r"[a-z]", password):
        pool_size += 26

    # Uppercase
    if re.search(r"[A-Z]", password):
        pool_size += 26

    # Numbers
    if re.search(r"\d", password):
        pool_size += 10

    # Symbols
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        pool_size += 32

    if pool_size == 0:
        return {
            "entropy": 0,
            "crack_time": "Instantly"
        }

    # Entropy Formula
    entropy = len(password) * math.log2(pool_size)

    entropy = round(entropy, 2)

    crack_time = estimate_crack_time(entropy)

    return {
        "entropy": entropy,
        "crack_time": crack_time
    }


def estimate_crack_time(entropy):
    """
    Estimate brute-force cracking time
    """

    if entropy < 28:
        return "Instantly"

    elif entropy < 36:
        return "Few Minutes"

    elif entropy < 60:
        return "Several Years"

    elif entropy < 80:
        return "Millions of Years"

    else:
        return "Practically Uncrackable"