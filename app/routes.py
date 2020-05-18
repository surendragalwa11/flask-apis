from flask_restful import Api
from flask import Blueprint

from app.modules.users import Users, User

api_bp = Blueprint('api', __name__)

api = Api(api_bp)
# add user routes
api.add_resource(Users, '/users')
api.add_resource(User, '/user/<int:userId>')