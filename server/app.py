from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from server.controllers import auth_controller, guest_controller, episode_controller, appearance_controller
    app.register_blueprint(auth_controller.bp)
    app.register_blueprint(guest_controller.bp)
    app.register_blueprint(episode_controller.bp)
    app.register_blueprint(appearance_controller.bp)

    return app