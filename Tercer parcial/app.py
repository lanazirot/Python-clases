from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt
from database import db
from encrypt import bcrypt
from flask_migrate import Migrate
from config import BaseConfig
from models import Usuario
from sqlalchemy import exc
from functools import wraps

app = Flask(__name__)
app.config.from_object(BaseConfig)
CORS(app)
bcrypt.init_app(app)
db.init_app(app)

migrate = Migrate(app)
migrate.init_app(app,db)

@app.route('/auth/registro', methods=['POST'])
def registro():
    user = request.get_json()
    userExists = Usuario.query.filter_by(email=user['email']).first()
    if not userExists:
        usuario = Usuario(email=user['email'], password=user['password'])
        try:
            db.session.add(usuario)
            db.session.commit()
            mensaje = "Usuario creado"
        except exc.SQLAlchemyError as e:
            mensaje = e
    else:
        mensaje = "Usuario ya existe"
    return jsonify({"message": mensaje})

@app.route('/auth/login', methods=['POST'])
def login():
    user = request.get_json()
    usuario = Usuario(password=user['password'], email=user['password'])
    search = Usuario.query.filter_by(email=user['email']).first()
    if search:
        validation = bcrypt.check_password_hash(search.password, user['password'])
        if validation:
            auth_token = usuario.encode_auth_token(search.id)
            responseObj = {
                'status': 'exitoso',
                'message': 'Login',
                'token': auth_token
            }
            return jsonify(responseObj)
    return jsonify({"message": 'Login fallido'})


def obtenerInfo(token):
    if token:
        response = Usuario.decode_auth(token)
        user = Usuario.query.filter_by(id=response).first()
        if user:
            usuario = {
                'status': 'exitoso',
                'data': {
                    'user_id': user.id,
                    'email': user.email,
                    'admin': user.admin,
                    'registered_on': user.registered_on
                }
            }
            return usuario
        else:
            return {
                'status': 'error',
                'data': {
                    'message': 'Usuario no encontrado'
                }
            }


def tokenCheck(function):
    @wraps(function)
    def verificar(*args, **kwargs):
        token = None
        if 'token' in request.headers:
            token = request.headers['token']
        
        if not token:
            return jsonify({
                'message': 'Token inexistente'
            })
        
        try:
            info = obtenerInfo(token)
            print(info)
            if info['status'] == 'Fallido':
                return jsonify({
                    'message': 'Token invalido'
                })
        except Exception as ex:
                return jsonify({
                    'message': 'Token invalido'
                })
        return function(info['data'], *args, **kwargs)
    return verificar


@app.route('/usuarios', methods=['GET'])
@tokenCheck
def getUsers(usuario):
    print(usuario)
    if usuario['admin']:
        output = []
        usuarios = Usuario.query.all()
        for u in usuarios:
            r = {}
            r['id'] = u.id
            r['email'] = u.email
            r['password'] = u.password
            r['registered_on'] = u.registered_on
            r['admin'] = u.admin
            output.append(r)
        return jsonify({'usuarios': output})
           
            
            
            
            