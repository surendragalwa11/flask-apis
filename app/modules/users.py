from flask_restful import Resource
from flask import request, jsonify, make_response

from app.models.user import User, UserSchema, db


class Users(Resource):
    def get(self):
        print('get request')
        getUsers = User.query.all()
        userschema = UserSchema(many=True)
        user = userschema.dump(getUsers)
        return make_response(jsonify({"users": user}))
        # return {'requestType': 'get'}, 201

    def post(self):
        print('create user')
        data = request.get_json()
        userschema = UserSchema()
        user = userschema.load(data)
        result = userschema.dump(user.create())
        return make_response(jsonify({"users": result}))
        # return {'requestType': 'post'}


class User(Resource):
    def get(self, userId):
        print('get user by Id')
        getUser = User.query.get(userId)
        userschema = UserSchema()
        user = userschema.dump(getUser)
        return make_response(jsonify({"user": user}))
        # return {'requestType': 'get'}, 201


    def put(self, userId):
        print('update user')
        data = request.get_json()
        getUser = User.query.get(userId)
        if data.get('email'):
            getUser.email = data['email']
        if data.get('email'):
            getUser.email = data['email']
        if data.get('password'):
            getUser.password = data['password']
        if data.get('contactNumber'):
            getUser.contactNumber = data['contactNumber']
        if data.get('address'):
            getUser.address = data['address']
        if data.get('role'):
            getUser.address = data['role']

        db.session.add(getUser)
        db.session.commit()

        userschema = UserSchema(only=['id', 'email', 'password', 'contactNumber', 'address', 'role'])
        user = userschema.dump(getUser)

        return make_response(jsonify({"user": user}))
        # return {'requestType': 'put'}

    def delete(self, userId):
        # delete user by id
        print('delete user by Id')
        getUser = User.query.get(userId)
        db.sessio.delete(getUser)
        db.session.commit()
        return {'requestType': 'delete'}