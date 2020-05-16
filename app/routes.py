from flask_restful import Api

# from app import app
from app.modules.users import Users

def initRoutes(app):
    api = Api(app)
    # add user routes
    api.add_resource(Users, '/user')