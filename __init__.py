from flask import Flask
from flask_login import LoginManager
from flask_pagedown import PageDown

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"


def create_app():
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    
    pagedown.init_app(app)
    return app
