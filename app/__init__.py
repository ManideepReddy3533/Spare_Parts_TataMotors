from flask import Flask
from config import Config
from .models import db 



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    print("DB URI:", app.config.get("SQLALCHEMY_DATABASE_URI"))  # Debug print

    db.init_app(app)
    
    from .routes import main
    app.register_blueprint(main)

    return app
