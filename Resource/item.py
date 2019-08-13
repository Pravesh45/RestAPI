import sqlite3
from flask import request
from flask_jwt import jwt_required
from flask_restful import Resource,reqparse
from Models.items import ItemModel
class Items(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price',
    type=float,
    required=True,
    help="This field is required"
    )
    parser.add_argument('store_id',
    type=int,
    required=True,
    help="Every items requires a store id"
    )
    @jwt_required()
    def get(self,name):
        ans=ItemModel.get_item_byname(name)
        if ans:
            return ans.json()
        return {'message':'item not found'},400

    def post(self,name):
        ans=ItemModel.get_item_byname(name)
        if ans:
            return {'message':'Item with the name already exists'}
        req_data=Items.parser.parse_args()
        item=ItemModel(name,req_data['price'],req_data['store_id'])
        try:
            item.save_to_db()
        except:
            return {'message':'An error occured while inserting the item'},500
        return item.json(),201

    def delete(self,name):
        ans=ItemModel.get_item_byname(name)
        if ans is None:
            return {'message':"Item  not found"},400
        ans.del_from_db()
        return {'message':"item deleted"}

    def put(self,name):
        data=Items.parser.parse_args()
        item=ItemModel.get_item_byname(name)
        if item is None:
            item=ItemModel(name,data['price'],data['store_id'])
        else:
            item.price=data['price']
            item.store_id=data['store_id']
        item.save_to_db()
        return item.json()

class item_list(Resource):
    def get(self):
        return {'items':[item.json() for item in ItemModel.query.all()]}
