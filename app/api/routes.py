from flask import request

from . import api

from .response_handler import (
    success_response,
    error_response
)

from app.extension import limiter

from app.security.sanitization import (
    sanitize_input
)

from app.services.password_analyser import (
    analyze_password
)

from app.services.password_generator import (
    generate_secure_password
)

from app.security.hash_utils import (
    hash_password,
    verify_password
)

from app.services.password_storage_service import (
    save_password_record,
    get_all_password_records,
    get_password_record_by_id
)


# ===================================
# Health Check API
# ===================================

@api.route('/health', methods=['GET'])
def api_health():

    return success_response(
        "API running successfully"
    )


# ===================================
# Password Analysis API
# ===================================

@api.route('/analyze', methods=['POST'])

@limiter.limit("10 per minute")

def analyze():

    data = request.get_json()

    if not data:

        return error_response(
            "Invalid JSON request",
            400
        )

    password = sanitize_input(
        data.get("password", "")
    )

    # Validation
    if not password:

        return error_response(
            "Password is required",
            400
        )

    if len(password) > 128:

        return error_response(
            "Password too long",
            400
        )

    # Analyze password
    result = analyze_password(password)

    # Hash password
    hashed_password = hash_password(password)

    # Store record
    save_password_record(
        hashed_password=hashed_password,
        strength=result["strength"],
        entropy=result["entropy"],
        crack_time=result["crack_time"]
    )

    return success_response(
        "Password analyzed successfully",
        result
    )


# ===================================
# Password Generator API
# ===================================

@api.route('/generate-password', methods=['GET'])

@limiter.limit("5 per minute")

def generate_password():

    length = request.args.get(
        "length",
        default=16,
        type=int
    )

    if length < 8 or length > 64:

        return error_response(
            "Length must be between 8 and 64",
            400
        )

    password = generate_secure_password(
        length
    )

    return success_response(
        "Password generated successfully",
        {
            "generated_password": password
        }
    )


# ===================================
# Password Verification API
# ===================================

@api.route('/verify-password', methods=['POST'])

@limiter.limit("5 per minute")

def verify_password_route():

    data = request.get_json()

    if not data:

        return error_response(
            "Invalid JSON request",
            400
        )

    record_id = data.get("record_id")

    password = sanitize_input(
        data.get("password", "")
    )

    if not record_id or not password:

        return error_response(
            "Missing required fields",
            400
        )

    record = get_password_record_by_id(
        record_id
    )

    if not record:

        return error_response(
            "Record not found",
            404
        )

    is_valid = verify_password(
        password,
        record.hashed_password
    )

    return success_response(
        "Verification completed",
        {
            "verified": is_valid
        }
    )


# ===================================
# Password History API
# ===================================

@api.route('/history', methods=['GET'])

@limiter.limit("10 per minute")

def password_history():

    records = get_all_password_records()

    data = []

    for record in records:

        data.append({

            "id": record.id,

            "strength": record.strength,

            "entropy": record.entropy,

            "crack_time": record.crack_time,

            "created_at": record.created_at
        })

    return success_response(
        "Password history retrieved",
        data
    )