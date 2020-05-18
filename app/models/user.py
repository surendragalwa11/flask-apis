from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20))
    password = db.Column(db.String(20))
    contactNumber = db.Column(db.Integer)
    address = db.Column(db.String(25))
    role = db.Column(db.String(20))
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, email, password, contactNumber, address, role):
        self.email = email
        self.password = password
        self.contactNumber = contactNumber
        self.address = address
        self.role = role

    def __repr__(self):
        return '' % self.id

class UserSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = User
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
    contactNumber = fields.Number(required=True)
    address = fields.String(required=True)
    role = fields.String(required=True)

