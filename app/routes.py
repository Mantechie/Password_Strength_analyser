from flask import (
    Blueprint,
    render_template,
    jsonify,
    request
)

from .services.password_analyser import analyze_password

from .services.password_generator import (
    generate_secure_password
)

from .security.hash_utils import hash_password

from .services.password_storage_service import (
    save_password_record,
    get_all_password_records
)

from .security.hash_utils import (
    hash_password,
    verify_password
)

from .security.sanitization import (
    sanitize_input
)

from .services.password_storage_service import (
    save_password_record,
    get_all_password_records,
    get_password_record_by_id,
    mark_password_as_verified,
    get_password_history
)

from .extension import limiter

main = Blueprint('main', __name__)

@main.route('/')
def home():
    """
    Render homepage
    """

    return render_template('index.html')


@main.route('/health')
def health_check():
    """
    Health check endpoint
    """

    return jsonify({
        "status": "running"
    })


@main.route('/analyze', methods=['POST'])
@limiter.limit("10 per minute")
def analyze():
    """
    Analyze and store password
    """

    data = request.get_json()

    password = sanitize_input(
        data.get("password", "")
    )
    
    # Length restriction
    if len(password) > 128:

        return jsonify({
            "error": "Password too long"
        }), 400

    # Validation
    if not password:

        return jsonify({
            "error": "Password is required"
        }), 400

    # Analyze password
    result = analyze_password(password)

    # Hash password
    hashed_password = hash_password(password)

    # Save analysis record
    save_password_record(
        hashed_password=hashed_password,
        strength=result["strength"],
        entropy=result["entropy"],
        crack_time=result["crack_time"]
    )

    return jsonify(result)

@main.route('/generate-password', methods=['GET'])
@limiter.limit("5 per minute")
def generate_password():
    """
    Generate secure password endpoint
    """

    length = request.args.get(
        "length",
        default=16,
        type=int
    )

    password = generate_secure_password(length)

    return jsonify({
        "generated_password": password
    })
    
@main.route('/records', methods=['GET'])
def records():
    """
    Return stored password analysis records
    """

    records = get_all_password_records()

    return jsonify([
        record.to_dict()
        for record in records
    ])
    
@main.route('/verify-password', methods=['POST'])
@limiter.limit("10 per minute")
def verify_password_route():
    """
    Verify password against stored hash
    """

    data = request.get_json()

    record_id = data.get("record_id")

    password = sanitize_input(
        data.get("password", "")
    )

    # Validate request
    if not record_id or not password:

        return jsonify({
            "error": "Missing required fields"
        }), 400

    # Retrieve record
    record = get_password_record_by_id(record_id)

    if not record:

        return jsonify({
            "error": "Record not found"
        }), 404

    # Verify password
    is_valid = verify_password(
        password,
        record.hashed_password
    )

    # Mark verified if valid
    if is_valid:
        mark_password_as_verified(record)

    return jsonify({
        "verified": is_valid
    })
    
@main.route('/password-history', methods=['GET'])
def password_history():
    """
    Return recent password history
    """

    history = get_password_history()

    return jsonify([
        {
            "id": record.id,
            "strength": record.strength,
            "entropy": record.entropy,
            "created_at": record.created_at
        }

        for record in history
    ])