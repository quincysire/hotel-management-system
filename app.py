from flask import Flask, current_app
from models.dbconfig import db
from ext import migrate, CORS, jwt
from config import Config
from flask_mail import Mail
import os
from routes.register_routes import register_routes

from datetime import datetime, timezone


def create_app():
    app = Flask(__name__, static_url_path='/swagger-ui',
                static_folder='swagger_ui')
    app.config.from_object(Config)

    basedir = os.path.abspath(os.path.dirname(__file__))
    db_dir = os.path.join(basedir, 'instance')
    try:
        if not os.path.exists(db_dir):
            os.makedirs(db_dir, exist_ok=True)
    except Exception as e:
        print(f"Error creating directory: {e}")

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Assign JWT configurations from config.py
    jwt.secret_key = app.config['JWT_SECRET_KEY']
    jwt.blacklist_enabled = app.config['JWT_BLACKLIST_ENABLED']
    jwt.blacklist_token_checks = app.config['JWT_BLACKLIST_TOKEN_CHECKS']

    # Initialize Flask-Mail
    mail = Mail()
    app.config['MAIL_SERVER'] = Config.MAIL_SERVER
    app.config['MAIL_PORT'] = Config.MAIL_PORT
    app.config['MAIL_USERNAME'] = Config.MAIL_USERNAME
    app.config['MAIL_PASSWORD'] = Config.MAIL_PASSWORD
    app.config['MAIL_USE_TLS'] = Config.MAIL_USE_TLS
    app.config['MAIL_USE_SSL'] = Config.MAIL_USE_SSL
    mail.init_app(app)

    return app


app = create_app()

# Initialize JWTManager with the app
jwt.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        jwt_key = current_app.config['JWT_SECRET_KEY']
        register_routes(app, db)
        db.create_all()
        port = int(os.environ.get('PORT', 5000))
        print(f"Running on port: {port}")
        app.run(debug=True, host="0.0.0.0", port=port)