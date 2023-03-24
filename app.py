from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from api import MovieListResource, MovieResource
from models import db
from schemas import MovieSchema
import os

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:hippo@localhost:5432/MovieDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ.get('SECRET_KEY', 'my_secret_key')

# Initialize database and migration engine
db.init_app(app)
migrate = Migrate(app, db)

# Register API resources
api = Api(app)
api.add_resource(MovieListResource, '/movies')
api.add_resource(MovieResource, '/movies/<int:movie_id>')

if __name__ == '__main__':
    app.run(debug=True)
