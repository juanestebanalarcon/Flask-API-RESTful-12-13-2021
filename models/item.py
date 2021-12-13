#import sqlite3
from dbAlchemy import db 
class ItemModel(db.Model):
    #SQL_Alchemy properties
    __tablename__="items"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(10))
    price = db.Column(db.Float(precision=2))
    store_id=db.Column(db.Integer,db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')
    def __init__(self,name,price,store_id):
        self.name = name
        self.price = price
        self.store_id=store_id
    def json(self):
        return {'name':self.name,'price':self.price,'store_id':self.store_id}
    @classmethod
    def findItemByName(cls,name):
        #ItemModel == cls
        return cls.query.filter_by(name=name).first() #first() / all() #select* from __tablename__ where name=name
        '''
        conn=sqlite3.connect("datosDB.db")
        curs=conn.cursor()
        res=curs.execute("select* from items where name=?",(name,))
        suF=res.fetchone()
        conn.close()
        if suF:
            return cls(*suF) #suF[0],suF[1]
    '''
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        '''
        conne=sqlite3.connect('datosDB.db')
        curs=conne.cursor()
        curs.execute("INSERT INTO items VALUES(?,?)",(self.name,self.price))
        conne.commit()
        conne.close()
        
        '''
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    '''
    #This method is replaced by save_to_db.   
    def update(self):
        conne = sqlite3.connect('datosDB.db')
        crsor = conne.cursor()
        crsor.execute("update items set price=? where name=?",(self.name,self.price))
        conne.commit()
        conne.close()
    '''