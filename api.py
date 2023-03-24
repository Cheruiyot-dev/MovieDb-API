from flask import request
from flask_restful import Resource
from models import db, Movie
from schemas import MovieSchema

class MovieListResource(Resource):
    def get(self):
        movies = Movie.query.all()
        movie_schema = MovieSchema(many=True)
        return movie_schema.dump(movies)

    def post(self):
        movie_schema = MovieSchema()
        try:
            movie = movie_schema.load(request.json, session=db.session)
            db.session.add(movie)
            db.session.commit()
            return movie_schema.dump(movie), 201
        except ValidationError as e:
            return e.messages, 400

class MovieResource(Resource):
    def get(self, movie_id):
        movie_schema = MovieSchema()
        movie = Movie.query.get(movie_id)
        if movie:
            return movie_schema.dump(movie)
        else:
            return {'message': 'Movie not found'}, 404

    def put(self, movie_id):
        movie_schema = MovieSchema()
        movie = Movie.query.get(movie_id)
        if movie:
            try:
                movie = movie_schema.load(request.json, instance=movie, session=db.session)
                db.session.commit()
                return movie_schema.dump(movie), 200
            except ValidationError as e:
                return e.messages, 400
        else:
            return {'message': 'Movie not found'}, 404

    def delete(self, movie_id):
        movie = Movie.query.get(movie_id)
        if movie:
            db.session.delete(movie)
            db.session.commit()
            return '', 204
        else:
            return {'message': 'Movie not found'}, 404
