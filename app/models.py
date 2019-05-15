from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


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

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # for api usage
    def to_dict(self, include_email=False, include_phone_num=False):
        data = {
            'id': self.id,
            'username': self.username,
            'create_time': self.create_time
        }
        if include_email is True:
            data['email'] = self.email
        if include_phone_num is True:
            data['phone_number'] = self.phone_number

        return data

