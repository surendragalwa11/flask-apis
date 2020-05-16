from flask_restful import Resource

class Users(Resource):
    def get(self):
        # get all users
        return {'username': '1'}

    def getById(self):
        # get user by id
        print('getById')

    def create(self, studentInfo):
        # create user by id
        print('create')

    def update(self, studentInfo):
        # update user by id
        print('update')

    def delete(self, studentInfo):
        # delete user by id
        print('delete')