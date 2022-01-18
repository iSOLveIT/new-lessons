
"""
    File containing used to declare models
"""
from app_example import db
from .helper import PkModel


class User(PkModel):
    username: str = db.Column(db.String(80), unique=True, nullable=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False)
    description: str = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

