from app import db
from models.db import Base

class Password(Base):
    __tablename__ = 'passwords'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    platform = db.Column(db.String(), nullable=False)
    password = db.Column(db.Text(), nullable=False)

    def __init__(self, username, platform, password):
        self.username = username
        self.platform = platform
        self.password = password
