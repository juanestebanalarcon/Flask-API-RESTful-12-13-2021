from flask_restful import Resource
from models.store import StoreModel
class Store(Resource):
    def get(self,name):
        store = StoreModel.findByName(name)
        if store:
            return store.json()
        else:
            return {'message':'store not found'},404
    def post(self,name):
        if StoreModel.findByName(name):
            return {'message':'A store with name {} already exists'.format(name)},409
        nStore = StoreModel(name)
        try:
            nStore.save_to_db()
        except:
            return {'message':'An error occurred while creating the store'},500
        return nStore.json(),201 
    def delete(self,name):
        tienda = StoreModel.findByName(name)
        if tienda:
            tienda.delete_from_db()
            return {'message':'store deleted'},200
        return {'message':'store not found'},404
class StoreList(Resource):
    def get(self):
        return {'Stores':list(map(lambda z: z.json(),StoreModel.query.all()))},200
