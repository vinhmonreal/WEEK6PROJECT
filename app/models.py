from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from secrets import token_urlsafe

from app import db, login

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable = False)
    email = db.Column(db.String(120), unique=True, nullable = False)
    password = db.Column(db.String(200), nullable = False)
    token = db.Column(db.String(200), index=True, unique=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    character = db.relationship('MarvelCharacter', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    
    def hash_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def add_token(self):
        setattr(self,'token',token_urlsafe(32))
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
        
    def to_dict(self):
        data = {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'date_created': self.date_created,
            'token': self.token
        }
        return data
        
class MarvelCharacter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(500), nullable = False)
    comics_appeared_in = db.Column(db.Integer, nullable = False)
    super_power = db.Column(db.String(100), nullable = False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    owner_id = db.Column(db.String, db.ForeignKey('user.token'), nullable=False)
    
    def __repr__(self):
        return f"MarvelCharacter('{self.name}', '{self.description}', '{self.comics_appeared_in}', '{self.super_power}', '{self.date_created}')"
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
        
    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'comics_appeared_in': self.comics_appeared_in,
            'super_power': self.super_power,
            'date_created': self.date_created,
            'owner_id': self.owner_id
        }
        return data
    
   
class AddDrinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strDrink = db.Column(db.String(100), nullable = False)
    strDrinkThumb = db.Column(db.String(500), nullable = False)
    idDrink = db.Column(db.String(5), nullable = False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    owner_id = db.Column(db.String, db.ForeignKey('user.token'), nullable=False)
    
    def __repr__(self):
        return f"AddDrink('{self.strDrink}', '{self.strDrinkThumb}', '{self.idDrink}', '{self.date_created}')"
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def to_dict(self):
        data = {
            'id': self.id,
            'strDrink': self.strDrink,
            'strDrinkThumb': self.strDrinkThumb,
            'idDrink': self.idDrink,
            'date_created': self.date_created,
            'owner_id': self.owner_id
            
        }
        return data