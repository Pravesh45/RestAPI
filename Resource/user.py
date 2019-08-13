import sqlite3
from flask_restful import Resource,reqparse
from Models.user import UserModel
from db import db


class user_register(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',
    required=True,
    type=str,
    help="This field is required"
    )
    parser.add_argument('password',
    required=True,
    type=str,
    help="This field is required"
    )
    def post(self):
        data=user_register.parser.parse_args()
        row=UserModel.get_username(data['username'])
        if row:
            return {"message":"User already registered"}
        else:
            user=UserModel(data['username'],data['password'])
            db.session.add(user)
            db.session.commit()
        return {'message':"User registered successfully"}
