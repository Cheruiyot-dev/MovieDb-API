from marshmallow import Schema, fields, ValidationError
from models import db, Movie

class MovieSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    director = fields.String(required=True)
    release_year = fields.Integer(required=True)

    def make_object(self, data):
        return Movie(**data)

    def load(self, data, session=None):
        obj = super().load(data)
        if session is not None:
            session.add(obj)
        return obj

    def dump(self, obj):
        data = super().dump(obj)
        data['uri'] = f'/movies/{obj.id}'
        return data

    @staticmethod
    def get_movie(id):
        movie = Movie.query.get(id)
        if not movie:
            raise ValidationError('Movie not found')
        return movie
