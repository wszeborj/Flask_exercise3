from __future__ import annotations
from . import db, ma
from flask_marshmallow import fields
from datetime import datetime


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tittle = db.Column(db.String(length=50), nullable=False)
    description = db.Column(db.String(length=5000), nullable=True)
    comments = db.relationship("Comments", backref="movie", lazy=True)

    def __init__(self, tittle: str, description: str):
        self.tittle = tittle
        self.description = description

    def update(self, modified_movie: Movies) -> None:
        self.tittle = modified_movie.tittle
        self.description = modified_movie.description

    @staticmethod
    def create_from_json(json_body: dict) -> Movies:
        return Movies(tittle=json_body['tittle'],
                     description=json_body['description'],
                    )


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(length=80), nullable=False)
    data = db.Column(db.String(length=5000), nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))

    def __init__(self, nickname, data, movie_id):
        self.nickname = nickname
        self.data = data
        self.date_time = datetime.utcnow()
        self.movie_id = movie_id

    def update(self, modified_comment: Comments) -> None:
        self.nickname = modified_comment.nickname
        self.data = modified_comment.data
        self.date_time = modified_comment.date_time

    @staticmethod
    def create_from_json(json_body: dict) -> Comments:
        return Comments(nickname=json_body['nickname'],
                        movie_id=json_body['movie_id'],
                        data=json_body['data'])


class MovieSchema(ma.Schema):
    id = fields.fields.Integer()
    tittle = fields.fields.Str()
    description = fields.fields.Str()
    comments = fields.fields.Nested('CommentSchema', many=True)



class CommentSchema(ma.Schema):
    id = fields.fields.Integer()
    nickname = fields.fields.Str()
    data = fields.fields.Str()
    date_time = fields.fields.DateTime(format='%d-%m-%y')
    movie_id = fields.fields.Integer()

# movie_schema = MovieSchema()
# comment_schema = CommentSchema()