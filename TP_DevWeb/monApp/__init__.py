from flask import Flask

from .app import db
from monApp.auteurs import auteurs_bp
from monApp.livres import livres_bp
from monApp.menu import menu_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    db.init_app(app)

    app.register_blueprint(livres_bp)
    app.register_blueprint(auteurs_bp)
    app.register_blueprint(menu_bp)

    from .commands import register_commands
    register_commands(app)

    from flask_bootstrap5 import Bootstrap
    Bootstrap(app)

    return app
