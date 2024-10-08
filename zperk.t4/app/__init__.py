from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///locked_in.db"
    db.init_app(app)

    with app.app_context():
        from app.routes import main_bp

        app.register_blueprint(main_bp)
        db.create_all()

    return app
