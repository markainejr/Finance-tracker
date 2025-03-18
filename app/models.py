from database import db
from sqlalchemy import text

class Transaction(db.Model):
 __tablename__ = "transactions"
id = db.Column(db.Integer, primary_key=True)
description = db.Column(db.String(100), nullable=False)
amount = db.Column(db.Float, nullable=False)
date = db.Column(db.DateTime, nullable=False)
category = db.Column(db.String(50))
created_at = db.Column(db.TIMESTAMP(timezone= True), server_default = text('now()')) # New field

def __repr__(self):
    return f'<Transaction {self.description}>'
    
  
class User(db.Model):
    __tablename__ = "users"
    id =db.Column(db.integer,primary_key=True)
    username = db.Column(db.string, nullable=False, unique=True)
    password = db.Column(db.string, nullable=False)
    created_at = db.Column(db.TIMESTAMP(timezone= True), server_default = text('now()'))

    def __repr__(self):
        return f'<Transaction {self.username}>'