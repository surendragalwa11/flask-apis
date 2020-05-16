from flask import Flask

from app.routes import initRoutes

app = Flask(__name__)

initRoutes(app)

