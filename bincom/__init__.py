from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from config import DevConfig

load_dotenv(".env")

migrate = Migrate()
db = SQLAlchemy()

def create_app():
    app = Flask('bincom')
    app.config.from_object(DevConfig)
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        from bincom import routes
        db.create_all()

    return app
