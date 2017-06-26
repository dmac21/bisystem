from . import db

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password=db.Column(db.String(64))
    password_hash = db.Column(db.String(128))

    def verify_password(self,password):
        pass
