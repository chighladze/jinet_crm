from flask import Flask
from datetime import datetime
from .extensions import db, migrate, login_manager
from .config import Config

from .routes.dashboard import dashboard
from .routes.users import users
from .routes.login import login


def create_app(config_class=Config):
    app = Flask(__name__)
    app.app_context().push()
    app.config.from_object(config_class)

    app.jinja_env.globals['now'] = datetime.now

    app.register_blueprint(login)
    app.register_blueprint(dashboard)
    app.register_blueprint(users)

    db.init_app(app)
    migrate.init_app(app, db)
    # login_manager.init_app(app)
    #
    # # LOGIN MANAGER
    # login_manager.login_view = 'user.login'
    # login_manager.login_message = "Please login to access this page."
    # login_manager.login_message_category = 'info'

    with app.app_context():
        db.create_all()

    return app
