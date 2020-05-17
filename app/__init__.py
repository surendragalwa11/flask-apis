from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes import initRoutes
from app.models.user import db

app = Flask(__name__)

app.config['SQL_ALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin@123@127.0.0.1:3306/flask_db'

db.init_app(app)
# db = SQLAlchemy(app)

initRoutes(app)
# initModels(db)

