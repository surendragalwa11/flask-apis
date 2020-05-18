from flask import Flask
from app.models.user import db



def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    from app.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from app.models.user import db
    db.init_app(app)
    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/
    with app.app_context():
        db.create_all()
    return app

