import jwt
import datetime
from config import BaseConfig
from app import db, bcrypt

class Usuario(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    email = db.Column(db.String(255), unique = True, nullable = False)
    password = db.Column(db.String(255), nullable = False)
    registered_on = db.Column(db.DateTime, nullable = False)
    admin = db.Column(db.Boolean, nullable = False, default=False)
    
    
    def __init__(self, email, password, admin=False) -> None:
        self.email = email
        self.admin = admin
        self.password = bcrypt.generate_password_hash(password, BaseConfig.BCRYPT_LOG_ROUNDS).decode('utf-8')
        self.registered_on = datetime.datetime.now()
    
    def encode_auth_token(self, user_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=10),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(payload, BaseConfig.SECRET_KEY, algorithm='HS256')
        except Exception as ex:
            return ex
    
    @staticmethod
    def decode_auth(token):
        try:
            return jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=['HS256'])['sub']
        except jwt.ExpiredSignatureError as se:
            return "Expired token", se
        except jwt.InvalidTokenError as it:
            return "Invalid token", it
    