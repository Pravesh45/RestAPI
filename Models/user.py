import sqlite3
from db import db
class UserModel(db.Model):
    __tablename__="users"

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    password=db.Column(db.String(50))

    def __init__(self,username,password):
         self.username=username
         self.password=password


    @classmethod
    def get_username(cls,username):
        return cls.query.filter_by(username=username).first()


    @classmethod
    def get_userid(cls,user_id):
        return cls.query.filter_by(id=user_id).first()
