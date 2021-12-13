from werkzeug.security import safe_str_cmp
from models.user import UserModel

#Funciones:
#Autenticación:
def authenticate(username,password):
    user=UserModel.find_by_username(username)
    #if user and user.password==password: another way is:
    if user and safe_str_cmp(user.password,password):
        return user 
def identity(payload):
     user_id = payload['identity']
     return UserModel.find_by_Id(user_id)
    
    