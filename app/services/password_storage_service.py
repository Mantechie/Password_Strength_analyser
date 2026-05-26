from app.extension import db

from app.models.password_model import (
    PasswordEntry
)


def save_password_record(
    hashed_password,
    strength,
    entropy,
    crack_time
):
    """
    Save password record
    """

    record = PasswordEntry(

        hashed_password=hashed_password,

        strength=strength,

        entropy=entropy,

        crack_time=crack_time
    )

    db.session.add(record)

    db.session.commit()

    return record


def get_all_password_records():
    """
    Retrieve all password records
    """

    return PasswordEntry.query.order_by(
        PasswordEntry.created_at.desc()
    ).all()


def get_password_record_by_id(record_id):
    """
    Get password record by ID
    """

    return PasswordEntry.query.get(record_id)


def mark_password_as_verified(record):
    """
    Mark password record as verified
    """

    record.is_verified = True

    db.session.commit()
    
def get_password_history(limit=10):
    """
    Retrieve recent password history
    """

    return PasswordEntry.query.order_by(
        PasswordEntry.created_at.desc()
    ).limit(limit).all()