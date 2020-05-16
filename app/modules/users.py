from flask_restful import Resource

class Users(Resource):
    def get(self):
        print('get request')
        # get all users
        return {'requestType': 'get'}

    def post(self):
        print('create user')
        return {'requestType': 'post'}

    def put(self):
        print('update user')
        return {'requestType': 'put'}

    def delete(self):
        # delete user by id
        print('delete user')
        return {'requestType': 'delete'}