from flask import Flask
from flask.ext.bootstrap import Bootstrap

from flask.ext.moment import Moment

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import config

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    #import auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    #import main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #import post blueprint
    from .post import post as post_blueprint
    app.register_blueprint(post_blueprint)

    #import freesiwtch blueprint
    from .freeswitch import auth as freeswitch_blueprint
    app.register_blueprint(freeswitch_blueprint)

    return app
