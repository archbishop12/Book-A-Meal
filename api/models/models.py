from flask_sqlalchemy import SQLAlchemy
import datetime
import context
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] =\
 "postgresql://postgres:12345@localhost/book"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

"""
Change to persistent data, using sql alchemy 
Using web tokens
Hashing Password sent to database

creating the models
"""

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))
    role_id = db.Column(db.Integer)
    business_name = db.Column(db.String(50))
    location = db.column(db.String(50))
    created_at = db.Column(db.DateTime(timezone=True),\
    default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime(timezone=True),\
    onupdate=datetime.datetime.utcnow)
    meal = db.relationship('Orders', backref='user', lazy=True) 
    menu = db.relationship('Menu', backref='user', lazy=True)
    
    
"""
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))
    created_at = db.Column(db.DateTime(timezone=True),\
    default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime(timezone=True),\
    onupdate=datetime.datetime.utcnow)
    menu = db.relationship('Menu', backref='admin', lazy=True)
"""    

class Meals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal_name = db.Column(db.String(50), unique=True)
    price = db.Column(db.Integer)
    meal_type = db.Column(db.String(50))
    created_at = db.Column(db.DateTime(timezone=True),\
    default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime(timezone=True),\
    onupdate=datetime.datetime.utcnow)   

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal_name = db.Column(db.String(50))
    price = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    """
    user_id = db.Column(db.Integer)
    """
    process_status = db.Column(db.String(50))
    created_at = db.Column(db.DateTime(timezone=True),\
    default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime(timezone=True),\
    onupdate=datetime.datetime.utcnow)


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    meal_ids = db.Column(db.String(50))
    created_at = db.Column(db.DateTime(timezone=True),\
    default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime(timezone=True),\
    onupdate=datetime.datetime.utcnow)