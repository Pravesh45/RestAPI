from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from Resource.user import user_register
from Resource.item import Items,item_list
from Resource.store import Store,StoreList

app=Flask(__name__)
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///example.db'
app.secret_key='lol'
api=Api(app)


jwt=JWT(app,authenticate,identity)

api.add_resource(Items,"/item/<string:name>")
api.add_resource(item_list,"/items")
api.add_resource(user_register,"/register")
api.add_resource(Store,"/store/<string:name>")
api.add_resource(StoreList,"/stores")

if __name__=="__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)
