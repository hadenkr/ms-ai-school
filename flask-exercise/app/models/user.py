from app.database import db
from datetime import datetime, timezone
# Import true() for server-side boolean default
from sqlalchemy import true as sql_true

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(160), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

    active = db.Column(db.Boolean, nullable=False, server_default=sql_true())
    create_date = db.Column(db.DateTime(), nullable=False, default=datetime.now(timezone.utc))
    update_date =db.Column(db.DateTime(), nullable=True, onupdate=datetime.now(timezone.utc))

    # Optional: Add __repr__
    def __repr__(self):
        return f'<User {self.user_id}:{self.username}>'
