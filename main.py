from flask import Flask
from flask_restx import Api

from app.db_init import db

from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns


def create_app():
    application = Flask(__name__)
    application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    application.app_context().push()
    return application


def configure_app():
    app = create_app()
    db.init_app(app)
    api = Api(app)

    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    return app


def load_data():
    db.create_all()


app = configure_app()
if __name__ == '__main__':
    app.run(debug=True)
