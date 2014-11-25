import hashlib
from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), index = True, unique = True)
    is_enabled = db.Column(db., index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    mobilephone = db.Column(db.Interger(11, index = True, unique = True)
    password = db.Column(db.String(32), unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)

    def __init__(self,username,email,password,role)
        self.username = username
        self.email = email
        self.password = hashlib.md5(password)

    def __repr__(self):
        return '<User %r>' % (self.nickname)


