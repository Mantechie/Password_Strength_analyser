from app.extension import db


class PasswordEntry(db.Model):
    """
    Model for storing password analysis records
    """

    __tablename__ = "password_entries"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    hashed_password = db.Column(
        db.String(255),
        nullable=False
    )

    strength = db.Column(
        db.String(50),
        nullable=False
    )

    entropy = db.Column(
        db.Float,
        nullable=False
    )

    crack_time = db.Column(
        db.String(100),
        nullable=False
    )
    
    is_verified = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    def to_dict(self):
        """
        Convert model to dictionary
        """

        return {
            "id": self.id,
            "strength": self.strength,
            "entropy": self.entropy,
            "crack_time": self.crack_time,
            "created_at": self.created_at
        }