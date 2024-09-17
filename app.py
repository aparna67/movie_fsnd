from flask import Flask, jsonify, abort, request
import logging
from flask_migrate import Migrate
from models import *
from auth import requires_auth, AuthError

# Congifuration


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object("config")

    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    migrate = Migrate(app, db, compare_type=True)

    # Configure logging to output to console
    logging.basicConfig(level=logging.INFO)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

    @app.route("/")
    def home():
        return "Hello, World!"

    @app.route("/movies")
    @requires_auth("view:movies")
    def retrieve_movies(payload):

        result = Movie.query.order_by(Movie.id).all()
        # logging.info(result)

        if len(result) == 0:
            abort(404)

        return jsonify(
            {"success": True, "movies": [movie.format() for movie in result]}
        )

    @app.route("/movies/<int:movie_id>", methods=["DELETE"])
    @requires_auth("delete:movies")
    def delete_movie(payload, movie_id):

        movie = Movie.query.get(movie_id)

        if movie is None:
            abort(404)
        try:

            # Delete the movie using delete method in Base model inherited by Movie Model
            movie.delete()
            result = Movie.query.order_by(Movie.id).all()

            return jsonify(
                {
                    "success": True,
                    "deleted_id": movie_id,
                    "movies": [movie.format() for movie in result],
                    "total_movies": len(Movie.query.all()),
                }
            )

        except:
            abort(422)

    @app.route("/movies", methods=["POST"])
    @requires_auth("post:movies")
    def create_movie(payload):
        body = request.get_json()

        new_title = body.get("title")
        new_release_date = body.get("release_date")
        new_genres = body.get("genres")
        new_director = body.get("director")

        if not all([new_title, new_release_date, new_genres, new_director]):
            abort(400)

        try:

            movie = Movie(
                title=new_title,
                release_date=new_release_date,
                genres=new_genres,
                director=new_director,
            )
            movie.insert()
            result = Movie.query.order_by(Movie.id).all()

            return jsonify(
                {
                    "success": True,
                    "created_id": movie.id,
                    "movies": [movie.format() for movie in result],
                    "total_movies": len(Movie.query.all()),
                }
            )

        except Exception as e:
            print(f"An error occurred: {e}")
            abort(422)

    @app.route("/movies/<int:movie_id>", methods=["PATCH"])
    @requires_auth("patch:movies")
    def update_movie(payload, movie_id):

        body = request.get_json()
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(404)
        try:

            if "title" in body:
                movie.title = body.get("title")
            if "release_date" in body:
                movie.release_date = body.get("release_date")
            if "genres" in body:
                movie.genres = body.get("genres")
            if "director" in body:
                movie.director = body.get("director")

            movie.update()

            return jsonify({"success": True, "updated_entry": movie.format()})

        except:
            abort(400)

    @app.route("/actors")
    @requires_auth("view:actors")
    def retrieve_actors(payload):

        result = Actor.query.order_by(Actor.id).all()
        if len(result) == 0:
            abort(404)

        return jsonify(
            {"success": True, "actors": [actor.format() for actor in result]}
        )

    @app.route("/actors/<int:actor_id>", methods=["DELETE"])
    @requires_auth("delete:actors")
    def delete_actor(payload, actor_id):

        actor = Actor.query.get(actor_id)

        if actor is None:
            abort(404)

        try:

            # Delete the movie using delete method in Base model inherited by Movie Model
            actor.delete()
            result = Actor.query.order_by(Actor.id).all()

            return jsonify(
                {
                    "success": True,
                    "deleted_id": actor_id,
                    "actors": [actor.format() for actor in result],
                    "total_actors": len(Actor.query.all()),
                }
            )

        except:
            abort(422)

    @app.route("/actors", methods=["POST"])
    @requires_auth("post:actors")
    def create_actor(payload):
        body = request.get_json()

        new_name = body.get("name")
        new_age = body.get("age")
        new_gender = body.get("gender")

        if not all([new_name, new_age, new_gender]):
            abort(400)

        try:

            actor = Actor(name=new_name, age=new_age, gender=new_gender)

            actor.insert()
            result = Actor.query.order_by(Actor.id).all()

            return jsonify(
                {
                    "success": True,
                    "created_id": actor.id,
                    "actors": [actor.format() for actor in result],
                    "total_actors": len(Actor.query.all()),
                }
            )

        except Exception as e:
            print(f"An error occurred: {e}")
            abort(422)

    @app.route("/actors/<int:actor_id>", methods=["PATCH"])
    @requires_auth("patch:actors")
    def update_actor(payload, actor_id):

        body = request.get_json()
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor is None:
            abort(404)
        try:

            if "name" in body:
                actor.name = body.get("name")
            if "age" in body:
                actor.age = body.get("age")
            if "gender" in body:
                actor.gender = body.get("gender")

            actor.update()

            return jsonify({"success": True, "updated_entry": actor.format()})

        except:
            abort(400)

    # Error handlers

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404, "message": "resource not found"}),
            404,
        )

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify(
                {
                    "success": False,
                    "error": 422,
                    "message": "unprocessable",
                    "details": str(error),
                }
            ),
            422,
        )

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "error": 400, "message": "bad request"}), 400

    @app.errorhandler(405)
    def not_allowed(error):
        return (
            jsonify({"success": False, "error": 405, "message": "method not allowed"}),
            405,
        )

    @app.errorhandler(500)
    def server_error(error):
        return (
            jsonify(
                {"success": False, "error": 500, "message": "internal_server_error"}
            ),
            500,
        )

    ## For Auth error
    @app.errorhandler(AuthError)
    def handle_auth_error(e):
        response = jsonify(
            {
                "success": False,
                "error": e.error,
                "message": "Authorization error occurred.",
            }
        )
        response.status_code = e.status_code
        return response

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)  # Start the Flask development server
