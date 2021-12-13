import sqlite3
connection_ = sqlite3.connect('datosDB.db')
#El cursor es el encargado de realizar funciones crud entre la app y la db,
cursor_ = connection_.cursor()
cursor_.execute("create table if not exists users (id integer primary key,username text,password text)")
cursor_.execute("create table if not exists items (id integer primary key,name text,price float)")
'''
uInsert = [
    (1,"Juanes","JEAM"),
    (2,"Jose","Jeam"),
    (3,"Juan","JEA")
]
iInsert =[
    ("Piano",50.00),
    ("Violin",100.00),
    ("iPhone",1.000)
]
cursor_.executemany("insert into users values(?,?,?)",uInsert)
cursor_.executemany("insert into items values(?,?)",iInsert)
'''
connection_.commit()
connection_.close()