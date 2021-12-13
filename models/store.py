#import sqlite3
from dbAlchemy import db 
class StoreModel(db.Model):
    #SQL_Alchemy properties
    __tablename__="stores"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(10))
    items=db.relationship('ItemModel',lazy='dynamic')
    def __init__(self,name):
        self.name = name
    def json(self):
        return {'name':self.name,'items':[item.json() for item in self.items.all()]}
    @classmethod
    def findByName(cls,name):
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