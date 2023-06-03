from flask import Blueprint, request, jsonify
from . import db
from .models import Movies, MovieSchema, Comments, CommentSchema

add_movie_blueprint = Blueprint('add_movie', __name__)
get_movies_blueprint = Blueprint('get_movies', __name__)
get_movie_blueprint = Blueprint('get_movie', __name__)
update_movie_blueprint = Blueprint('update_movie', __name__)
delete_movie_blueprint = Blueprint('delete_movie', __name__)

add_comment_blueprint = Blueprint('add_comment', __name__)
get_comments_blueprint = Blueprint('get_comments', __name__)
get_comment_blueprint = Blueprint('get_comment', __name__)
update_comment_blueprint = Blueprint('update_comment', __name__)
delete_comment_blueprint = Blueprint('delete_comment', __name__)

get_movie_comments_blueprint = Blueprint('get_movie_comments', __name__)


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


def add_movie_to_db(new_movie: Movies) -> None:
    db.session.add(new_movie)
    db.session.commit()


def delete_movie_from_db(movie_to_delete: Movies) -> None:
    db.session.delete(movie_to_delete)
    db.session.commit()


comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)


def add_comment_to_db(new_comment: Comments) -> None:
    db.session.add(new_comment)
    db.session.commit()


def delete_comment_from_db(comment_to_delete: Comments) -> None:
    db.session.delete(comment_to_delete)
    db.session.commit()


@add_movie_blueprint.route('/movies', methods=['POST'])
def add_movie() -> str:
    body = request.json
    new_movie = Movies.create_from_json(json_body=body)
    add_movie_to_db(new_movie)

    return movie_schema.jsonify(new_movie)


@get_movies_blueprint.route('/movies', methods=['GET'])
def get_movies() -> str:
    all_movies = Movies.query.all()
    return movies_schema.jsonify(all_movies)


@get_movie_blueprint.route('/movies/<int:id>', methods=['GET'])
def get_movie_by_id(id: int) -> str:
    found_movie = Movies.query.get(id)
    return movie_schema.jsonify(found_movie)


@update_movie_blueprint.route('/movies/<int:id>', methods=['PATCH'])
def update_movie(id: int) -> str:
    found_movie = Movies.query.get(id)
    body = request.json
    found_movie.update(Movies.create_from_json(json_body=body))
    db.session.commit()

    return movie_schema.jsonify(found_movie)


@delete_movie_blueprint.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id: int) -> str:
    movie_to_delete = Movies.query.get(id)
    delete_movie_from_db(movie_to_delete)

    return movie_schema.jsonify(movie_to_delete)


@add_comment_blueprint.route('/comments', methods=['POST'])
def add_comment() -> str:
    body = request.json
    new_comment = Comments.create_from_json(json_body=body)
    add_comment_to_db(new_comment)

    return comment_schema.jsonify(new_comment)


@get_comments_blueprint.route('/comments', methods=['GET'])
def get_comments() -> str:
    all_comments = Comments.query.all()
    return comments_schema.jsonify(all_comments)


@get_comment_blueprint.route('/comments/<int:id>', methods=['GET'])
def get_comment_by_id(id: int) -> str:
    found_comment = Comments.query.get(id)
    return comment_schema.jsonify(found_comment)


@update_comment_blueprint.route('/comments/<int:id>', methods=['PATCH'])
def update_comment(id: int) -> str:
    found_comment = Comments.query.get(id)
    body = request.json
    found_comment.update(Comments.create_from_json(json_body=body))
    db.session.commit()

    return comment_schema.jsonify(found_comment)


@delete_comment_blueprint.route('/comments/<int:id>', methods=['DELETE'])
def delete_comment(id: int) -> str:
    comment_to_delete = Comments.query.get(id)
    delete_comment_from_db(comment_to_delete)

    return comment_schema.jsonify(comment_to_delete)
