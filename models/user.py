import sqlite3
from dbAlchemy import db
class UserModel(db.Model):
    #Implementación con SQL_Alchemy
    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(12))
    password=db.Column(db.String(10))
    #Se omite el id porque es autoincrementable
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()
        '''
        conn=sqlite3.connect("datosDB.db")
        cursor_=conn.cursor()
        resultset = cursor_.execute("select* from users where username=?",(username,))
        laFila = resultset.fetchone()
        if laFila:
            user=cls(*laFila) #(laFila[0],laFila[1],laFila[2])
        else: 
            user=None
        conn.close()
        return user 
        '''
    @classmethod
    def find_by_Id(cls,_id):
        return cls.query.filter_by(id=_id).first()
        '''
        conn=sqlite3.connect("datosDB.db")
        cursor_=conn.cursor()
        resultset = cursor_.execute("select* from users where id=?",(_id,))
        suFila = resultset.fetchone()
        if suFila:
            usuario=cls(*suFila) #(laFila[0],laFila[1],laFila[2])
        else:
            usuario=None
        conn.close()
        return usuario 
        '''