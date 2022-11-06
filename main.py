from flask import Flask
from flask_restx import Api

import app
from app import models
from app import config
from app.config import db

from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns


def create_app():
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


def configure_app():
    db.init_app(application)
    api = Api(app)

    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


def load_data():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
