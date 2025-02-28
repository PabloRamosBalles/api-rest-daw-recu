from flask import Flask, request
from flask_mysqldb import MySQL
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from os import getenv

load_dotenv()
app = Flask(__name__)
mysql = MySQL(app)
# mongo = PyMongo(app)

app.config['MYSQL_DB'] = getenv('MYSQL_DB')
app.config['MYSQL_HOST'] = getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = getenv('MYSQL_PASSWORD')
#app.secret_key['SECRET_KEY'] = '1234'

#app.config['MONGO_URI'] = 'mongodb://localhost:27017'

@app.route('/users')
def getUsers():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM persona')
    data = cur.fetchall()
    return {"personas": data}

@app.route('/users/<string:id>')
def getUser(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM persona where id=%s',(id,))
    data = cur.fetchall()
    return {"personas": data}

@app.route('/users/add', methods=['POST'])
def addUser():
    nombre = request.get_json('nombre')
    apellido = request.get_json('apellido')
    edad = request.get_json('edad')
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO persona (id, nombre, apellido, edad ) values (null, %s, %s, %s)',(nombre, apellido, edad))
    mysql.connection.commit()
    return {"message": nombre+" añadid@"}

@app.route('/users/edit/<string:id>', methods=['POST'])
def editUser(id):
    nombre = request.get_json('nombre')
    apellido = request.get_json('apellido')
    edad = request.get_json('edad')
    cur = mysql.connection.cursor()
    cur.execute('UPDATE persona (id, nombre, apellido, edad ) values (null, %s, %s, %s) where id=%s',(nombre, apellido, edad, id))
    mysql.connection.commit()
    return {"message": nombre+" editad@"}

@app.route('/users/delete/<string:id>', methods=['POST'])
def deleteUser(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE from persona where id=%s',(id,))
    mysql.connection.commit()
    return {"message": "perona borrad@"}


#MONGO

# @app.route('/mongo/users')
# def mongoGetUsers():
#     data = mongo.examen.find()
#     return {"personas": data}

# @app.route('/mongo/user/<string:_id>')
# def mongoGetUsers(_id):
#     data = mongo.examen.findOne({"_id":_id})
#     return {"persona": data}

# @app.route('/mongo/add_user')
# def mongoAddUsers():
#     nombre = request.get_json('nombre')
#     apellido = request.get_json('apellido')
#     edad = request.get_json('edad')
#     data = mongo.examen.createOne({"nombre": nombre, "apellido": apellido, "edad":edad})
#     return {"persona añadida": data}

# @app.route('/mongo/delete_user/<string:_id>')
# def mongoDeleteUsers(_id):
#     data = mongo.examen.DeleteOne({"_id":_id})
#     return {"persona borrada": data}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')