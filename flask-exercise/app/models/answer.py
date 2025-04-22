from app.database import db
from datetime import datetime, timezone
# Import true() for server-side boolean default
from sqlalchemy import true as sql_true

class Answer(db.Model):
    __tablename__ = 'answers'

    answer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    content = db.Column(db.Text(), nullable=False)

    active = db.Column(db.Boolean, nullable=False, server_default=sql_true())
    create_date = db.Column(db.DateTime(), nullable=False, default=datetime.now(timezone.utc))
    update_date =db.Column(db.DateTime(), nullable=True, onupdate=datetime.now(timezone.utc))

    # 역참조
    ref_question = db.relationship('Question', backref=db.backref('answers', lazy='dynamic'))
    ref_user = db.relationship('User', backref=db.backref('user_answers', lazy='dynamic')) # Added User relationship, added lazy='dynamic'

    # Optional: Add __repr__
    def __repr__(self):
        return f'<Answer {self.answer_id}>'
