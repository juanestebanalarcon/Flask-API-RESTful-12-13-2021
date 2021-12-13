from flask_restful import Api
from flask import Flask
from flask_jwt import JWT
from security import authenticate,identity 
from resources.user import UserRegister
from resources.Item import*
from resources.store import*
from dbAlchemy import db 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datosDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key='Jeam'
api =Api(app)
@app.before_first_request
def createTables():
    db.create_all()
jwt = JWT(app,authenticate,identity) #/auth
#Replacing @app.route('/item/<string:name>')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister,'/Register')
if __name__=='__main__':
    db.init_app(app)
    app.run(port=5000,debug=True)
