from flask_restful import Resource
from Models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store=StoreModel.get_store_byname(name)
        if store:
            return store.json()
        return {'message':'Store does not exists'},404

    def post(self,name):
        ans=StoreModel.get_store_byname(name)
        if ans:
            return {'message':'Store with the name {} already exists'.format(name)},400
        store=StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message':'There was a problem posting the store'},500
        return store.json(),201

    def delete(self,name):
        store=StoreModel.get_store_byname(name)
        if store is None:
            return {'message':'store does not exists'}
        store.del_from_db()
        return {'message':'store succesfully deleted'}

class StoreList(Resource):
    def get(self):
        return {'store':[store.json() for store in StoreModel.query.all()]}
