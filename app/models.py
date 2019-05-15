from app import db
from datetime import datetime


class User(db.Model):
    # name of database
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    phone_number = db.Column(db.String(16), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<\nusername = {}\nemail = {}\ncreate_time = {}\n>'.format(self.username, self.email, self.create_time)
