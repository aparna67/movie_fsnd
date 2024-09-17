# import os
import unittest
import json

# from flask_sqlalchemy import SQLAlchemy
from settings import DB_USER, DB_PASSWORD

from app import create_app
from models import Movie, Actor
from tokens import tokens


class MovieTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.database_name = "casting_data_test"
        self.app = create_app(
            {
                "SQLALCHEMY_DATABASE_URI": f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/{self.database_name}"
            }
        )

        self.client = self.app.test_client()
        self.headers = {
            "Casting Assistant": {"Authorization": tokens["Casting Assistant"]},
            "Casting Director": {"Authorization": tokens["Casting Director"]},
            "Executive Producer": {"Authorization": tokens["Executive Producer"]},
        }
        self.new_movie = {
            "title": "Dangal",
            "release_date": "2016-12-23",
            "genres": ["Sport", "Action"],
            "director": "Nitesh Tiwari",
        }

        self.new_actor = {"name": "Kajol", "age": 50, "gender": "F"}

    def tearDown(self):
        """Executed after each test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    ## Test for movies

    ## Success endpoints

    def test_retrieval_movies(self):
        """Test _____________"""
        res = self.client.get("/movies", headers=self.headers["Casting Assistant"])
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movies"])

    def test_create_new_movie(self):
        res = self.client.post(
            "/movies", json=self.new_movie, headers=self.headers["Executive Producer"]
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

        self.assertIn("created_id", data)

        self.assertTrue(data["movies"])
        self.assertTrue(data["total_movies"])

    def test_delete_movie(self):
        with self.app.app_context():

            res = self.client.delete(
                "/movies/5", headers=self.headers["Executive Producer"]
            )
            data = json.loads(res.data)

            movie = Movie.query.filter(Movie.id == 5).one_or_none()

            self.assertEqual(res.status_code, 200)
            self.assertEqual(data["success"], True)
            self.assertEqual(data["deleted_id"], 5)
            self.assertTrue(data["total_movies"])
            self.assertTrue(len(data["movies"]))
            self.assertEqual(movie, None)

    def test_update_movie(self):
        res = self.client.patch(
            "/movies/1",
            json={"director": "Karan Johar"},
            headers=self.headers["Executive Producer"],
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["updated_entry"])

    ## Error for endpoints

    def test_401_retrieval_movies(self):
        res = self.client.get("/movies")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"]["code"], "authorization_header_missing")
        self.assertEqual(
            data["error"]["description"], "Authorization header is expected."
        )

    def test_create_new_movie_fails(self):
        self.new_movie_err = {
            "title": "Dangal",
            "release_date": "2016-12-23",
            "genres": ["Sport", "Action"],
            "director": "",
        }
        res = self.client.post(
            "/movies",
            json=self.new_movie_err,
            headers=self.headers["Executive Producer"],
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "bad request")

    def test_401_for_failed_update(self):
        res = self.client.patch(
            "/movies/1",
            json={"director": "Yash Chopra"},
            # headers=self.headers["Executive Producer"],
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"]["code"], "authorization_header_missing")
        self.assertEqual(
            data["error"]["description"], "Authorization header is expected."
        )

    ##Test for actors

    ## Success endpoints

    def test_retrieval_actors(self):
        """Test _____________"""
        res = self.client.get("/actors", headers=self.headers["Casting Assistant"])
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    def test_create_new_actor(self):
        res = self.client.post(
            "/actors", json=self.new_actor, headers=self.headers["Executive Producer"]
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

        self.assertIn("created_id", data)

        self.assertTrue(data["actors"])
        self.assertTrue(data["total_actors"])

    def test_delete_actor(self):
        with self.app.app_context():

            res = self.client.delete(
                "/actors/5", headers=self.headers["Executive Producer"]
            )
            data = json.loads(res.data)

            actor = Actor.query.filter(Actor.id == 5).one_or_none()

            self.assertEqual(res.status_code, 200)
            self.assertEqual(data["success"], True)
            self.assertEqual(data["deleted_id"], 5)
            self.assertTrue(data["total_actors"])
            self.assertTrue(len(data["actors"]))
            self.assertEqual(actor, None)

    def test_update_actor(self):
        res = self.client.patch(
            "/actors/1",
            json={"age": 42},
            headers=self.headers["Executive Producer"],
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["updated_entry"])

    ## Error endpoints

    def test_401_retrieval_actor(self):
        res = self.client.get("/actors")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"]["code"], "authorization_header_missing")
        self.assertEqual(
            data["error"]["description"], "Authorization header is expected."
        )

    def test_create_new_actor_fails(self):
        self.new_actor_err = {"name": "Varun Dhawan", "age": 37, "gender": ""}
        res = self.client.post(
            "/actors",
            json=self.new_actor_err,
            headers=self.headers["Executive Producer"],
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "bad request")

    def test_404_if_actor_does_not_exist(self):
        res = self.client.delete(
            "/actors/1000", headers=self.headers["Casting Director"]
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_401_for_failed_update(self):
        res = self.client.patch(
            "/actors/1",
            json={"age": 76},
            # headers=self.headers["Executive Producer"],
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"]["code"], "authorization_header_missing")
        self.assertEqual(
            data["error"]["description"], "Authorization header is expected."
        )

    def test_delete_actor_unauthorised(self):

        res = self.client.delete("/actors/1", headers=self.headers["Casting Assistant"])
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"]["code"], "unauthorized")
        self.assertEqual(data["error"]["description"], "Permission not found.")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
