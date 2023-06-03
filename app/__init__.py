from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .constants import DB_PATH

db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'

    db.init_app(app)
    ma.init_app(app)
    app.debug = True

    from .main import add_movie_blueprint, get_movies_blueprint, \
        get_movie_blueprint, update_movie_blueprint, delete_movie_blueprint, \
        add_comment_blueprint, get_comments_blueprint, get_comment_blueprint, \
        update_comment_blueprint, delete_comment_blueprint

    app.register_blueprint(add_movie_blueprint)
    app.register_blueprint(get_movies_blueprint)
    app.register_blueprint(get_movie_blueprint)
    app.register_blueprint(update_movie_blueprint)
    app.register_blueprint(delete_movie_blueprint)

    app.register_blueprint(add_comment_blueprint)
    app.register_blueprint(get_comments_blueprint)
    app.register_blueprint(get_comment_blueprint)
    app.register_blueprint(update_comment_blueprint)
    app.register_blueprint(delete_comment_blueprint)

    return app
