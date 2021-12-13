from flask_restful import Resource,reqparse
#import sqlite3
from flask_jwt import jwt_required
from models.item import ItemModel
class Item(Resource):
    parser = reqparse.RequestParser()
    #reqparse ayuda a definir el tipo de dato que debe recibir, si es o no obligatorio y darle una guía al usuario
    parser.add_argument('price',type=float,required=True,help="This field cannot be left blank.")
    parser.add_argument('store_id',type=int,required=True,help="This field cannot be left blank.")
    #reqparse reemplaza request.get_jason() -->
    @jwt_required()
    def get(self,name):
        i=ItemModel.findItemByName(name)
        if i:
            return i.json() 
        return {'message':'Item not found'},404

        '''
        item = next(filter(lambda i: i['name']==name,items),None)
        return {'item':item},200 if item else 404
        for item in items:
            if item['name']==name:
                return item,200
        return {'error':'Item not found','status':404},404
        '''
   
    def post(self,name):
        data = Item.parser.parse_args()  
        #Validar que no ingrese duplicados:
        #if next(filter(lambda i: i['name']==name,items),None):
        if ItemModel.findItemByName(name):
             return {'message': "An item with name '{}' already exists.".format(name)},400
        i = ItemModel(name, data['price'],data['store_id'])
        try:
            i.save_to_db()  #insert()
        except:
            return {'message':'An error occurred inserting the item.'},500
        return i.json(),201 
    
    
    def delete(self,name):
        elI=ItemModel.findItemByName(name)
        if elI:
            elI.delete_from_db()
            '''
            conn = sqlite3.connect('datosDB.db')
            cur = conn.cursor()
            cur.execute("delete from items where name=?",(name,))    
            conn.commit()
            conn.close()   
            '''
            return {'message':'Item deleted'},200
        return {'message':"Item with name '{}' doesn't exist".format(name)},400
    def put(self,name):
        datos = Item.parser.parse_args()
        elItem =ItemModel.findItemByName(name)
        if elItem:
             elItem.price = datos['price']
        else:
            elItem = ItemModel(name,datos['price'],datos['store_id'])   
        elItem.save_to_db()
        return elItem.json()
        '''
        updatedI=ItemModel(name, datos['price'])
        if  elItem is None:
            try:
                updatedI.insert()
            except:
                return {'message':'An error occurred inserting the item'},500
        else:
            try:
                updatedI.update()
            except:
                return {'message':'An error occurred updating the item.'},500
        return updatedI.json()            
        '''
class ItemList(Resource):
    def get(self):
        '''
        conne = sqlite3.connect('datosDB.db')
        crsor = conne.cursor()
        rs=crsor.execute("select* from items")
        items=[]
        for row in rs:
            items.append({'name':row[0],'price':row[1]})
        conne.close() 
        '''
        return {'Items':list(map(lambda z: z.json(),ItemModel.query.all()))},200