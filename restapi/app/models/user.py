from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(128))

    def __init__(self, username,email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)


    def __repr__(self):
        return '<User {}>'.format(self.username)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
  