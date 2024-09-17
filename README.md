# Capstone Full Stack Nano Degree Project

This is the final project in a series of mini projects as part of the Udacity Full Stack Developer Nanodegree program. In this project, all the skills learned up to now, such as Flask, SQLAlchemy, API authentication, app headers, etc., have been applied. The project is deployed on Render Cloud (https://movie-fsnd.onrender.com/)

## Movie App

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

The application has two databases Movies and Actors and the following actions can be done on the database :

1. Display all the data
2. Delete any movie/actor entry by id.
3. Add a new movie/actor entry
4. Modify any exsiting entry

There are three authentication levels in the application: Casting Assistant, Casting Director and Executive Producer.They have the following roles associated :

1. Casting Assistant

- Can view actors and movies

2. Casting Director

- All permissions a Casting Assistant has and…
- Add or delete an actor from the database
- Modify actors or movies

3. Executive Producer

- All permissions a Casting Director has and…
- Add or delete a movie from the database

## Setting up the application

### Install Dependencies

1. **Python 3.11** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

### Run the Server

First ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Documenting Endpoints

{{host}} is localhost:5000. The endpoints are retrieved using Postman.

`GET '/movies'`

- Fetches a dictionary of movies which have attributes: id, title, release_date, genres and director
- Request Arguments: None
- Requires `view:movies` permission
- {{host}}/movies (ran in Postman)

```json
{
  "movies": [
    {
      "director": "Karan Malhotra",
      "genres": ["Action", "Drama"],
      "id": 1,
      "release_date": "Thu, 26 Jan 2012 00:00:00 GMT",
      "title": "Agneepath"
    },
    {
      "director": "Aditya Sarpotdar",
      "genres": ["Comedy", "Horror"],
      "id": 2,
      "release_date": "Fri, 07 Jun 2024 00:00:00 GMT",
      "title": "Munjya"
    },
    {
      "director": "Siddharth Anand",
      "genres": ["Action", "Thriller"],
      "id": 3,
      "release_date": "Thu, 25 Jan 2024 00:00:00 GMT",
      "title": "Fighter"
    },
    {
      "director": "Homi Adajania",
      "genres": ["Comedy", "Romance"],
      "id": 5,
      "release_date": "Fri, 13 Jul 2012 00:00:00 GMT",
      "title": "Cocktail"
    },
    {
      "director": "Yash Chopra",
      "genres": ["Musical", "Romance"],
      "id": 6,
      "release_date": "Fri, 12 Nov 2004 00:00:00 GMT",
      "title": "Veer Zara"
    }
  ],
  "success": true
}
```

`GET '/actors'`

- Fetches a dictionary of actors which have attributes: id, age, gender, name
- Request Arguments: None
- Requires `view:actors` permission
- {{host}}/actors (ran in Postman)

```json
{
  "actors": [
    {
      "age": 41,
      "gender": "M",
      "id": 1,
      "name": "Ranbir Kapoor"
    },
    {
      "age": 39,
      "gender": "M",
      "id": 2,
      "name": "Ranveer singh"
    },
    {
      "age": 41,
      "gender": "F",
      "id": 3,
      "name": "Katrina Kaif"
    },
    {
      "age": 43,
      "gender": "F",
      "id": 4,
      "name": "Kareena Kapoor"
    },
    {
      "age": 57,
      "gender": "F",
      "id": 7,
      "name": "Madhuri Dixit"
    },
    {
      "age": 41,
      "gender": "M",
      "id": 8,
      "name": "Ranbir Kapoor"
    },
    {
      "age": 39,
      "gender": "M",
      "id": 9,
      "name": "Ranveer singh"
    },
    {
      "age": 41,
      "gender": "F",
      "id": 10,
      "name": "Katrina Kaif"
    },
    {
      "age": 43,
      "gender": "F",
      "id": 11,
      "name": "Kareena Kapoor"
    },
    {
      "age": 36,
      "gender": "M",
      "id": 12,
      "name": "Vicky Kaushal"
    }
  ],
  "success": true
}
```

---

`DELETE '/actors/${id}'`

- Deletes a specified actor using the id of the actor
- Request Arguments: `id` - integer
- Returns: Returns the id of the actor that was deleted, remaining actors, total number of actors.
- {{host}}/actors/12

```json
{
  "actors": [
    {
      "age": 41,
      "gender": "M",
      "id": 1,
      "name": "Ranbir Kapoor"
    },
    {
      "age": 39,
      "gender": "M",
      "id": 2,
      "name": "Ranveer singh"
    },
    {
      "age": 41,
      "gender": "F",
      "id": 3,
      "name": "Katrina Kaif"
    },
    {
      "age": 43,
      "gender": "F",
      "id": 4,
      "name": "Kareena Kapoor"
    },
    {
      "age": 57,
      "gender": "F",
      "id": 7,
      "name": "Madhuri Dixit"
    },
    {
      "age": 41,
      "gender": "M",
      "id": 8,
      "name": "Ranbir Kapoor"
    },
    {
      "age": 39,
      "gender": "M",
      "id": 9,
      "name": "Ranveer singh"
    },
    {
      "age": 41,
      "gender": "F",
      "id": 10,
      "name": "Katrina Kaif"
    },
    {
      "age": 43,
      "gender": "F",
      "id": 11,
      "name": "Kareena Kapoor"
    }
  ],
  "deleted_id": 12,
  "success": true,
  "total_actors": 9
}
```

---

`DELETE '/movies/${id}'`

- Deletes a specified movie using the id of the movie
- Request Arguments: `id` - integer
- Returns: Returns the id of the movie that was deleted, remaining movies, total number of movies.
- {{host}}/movies/3

```json
{
  "deleted_id": 3,
  "movies": [
    {
      "director": "Karan Malhotra",
      "genres": ["Action", "Drama"],
      "id": 1,
      "release_date": "Thu, 26 Jan 2012 00:00:00 GMT",
      "title": "Agneepath"
    },
    {
      "director": "Aditya Sarpotdar",
      "genres": ["Comedy", "Horror"],
      "id": 2,
      "release_date": "Fri, 07 Jun 2024 00:00:00 GMT",
      "title": "Munjya"
    },
    {
      "director": "Homi Adajania",
      "genres": ["Comedy", "Romance"],
      "id": 5,
      "release_date": "Fri, 13 Jul 2012 00:00:00 GMT",
      "title": "Cocktail"
    },
    {
      "director": "Yash Chopra",
      "genres": ["Musical", "Romance"],
      "id": 6,
      "release_date": "Fri, 12 Nov 2004 00:00:00 GMT",
      "title": "Veer Zara"
    }
  ],
  "success": true,
  "total_movies": 4
}
```

---

`POST '/movies'`

- Sends a post request in order to add a new movie
- Request Body:

```json
{
  "title": "Welcome",
  "release_date": "2007-12-21",
  "genres": ["Comedy", "Drama"],
  "director": "Anees Bazmee"
}
```

- Returns: created movie id, movies ,total_movies
- {{host}}/movies
- In Body Select raw and paste the movie in json format above and press send

```json
{
  "created_id": 7,
  "movies": [
    {
      "director": "Karan Malhotra",
      "genres": ["Action", "Drama"],
      "id": 1,
      "release_date": "Thu, 26 Jan 2012 00:00:00 GMT",
      "title": "Agneepath"
    },
    {
      "director": "Aditya Sarpotdar",
      "genres": ["Comedy", "Horror"],
      "id": 2,
      "release_date": "Fri, 07 Jun 2024 00:00:00 GMT",
      "title": "Munjya"
    },
    {
      "director": "Homi Adajania",
      "genres": ["Comedy", "Romance"],
      "id": 5,
      "release_date": "Fri, 13 Jul 2012 00:00:00 GMT",
      "title": "Cocktail"
    },
    {
      "director": "Yash Chopra",
      "genres": ["Musical", "Romance"],
      "id": 6,
      "release_date": "Fri, 12 Nov 2004 00:00:00 GMT",
      "title": "Veer Zara"
    },
    {
      "director": "Anees Bazmee",
      "genres": ["Comedy", "Drama"],
      "id": 7,
      "release_date": "Fri, 21 Dec 2007 00:00:00 GMT",
      "title": "Welcome"
    }
  ],
  "success": true,
  "total_movies": 5
}
```

---

`POST '/actors'`

- Sends a post request in order to add a new actor
- Request Body:

```json
{
  "age": 36,
  "gender": "M",
  "id": 12,
  "name": "Vicky Kaushal"
}
```

- Returns: created actor id, actors ,total_actors
- {{host}}/actors
- In Body Select raw and paste the actor in json format above and press send

```json
{
  "actors": [
    {
      "age": 41,
      "gender": "M",
      "id": 1,
      "name": "Ranbir Kapoor"
    },
    {
      "age": 39,
      "gender": "M",
      "id": 2,
      "name": "Ranveer singh"
    },
    {
      "age": 41,
      "gender": "F",
      "id": 3,
      "name": "Katrina Kaif"
    },
    {
      "age": 43,
      "gender": "F",
      "id": 4,
      "name": "Kareena Kapoor"
    },
    {
      "age": 57,
      "gender": "F",
      "id": 7,
      "name": "Madhuri Dixit"
    },
    {
      "age": 41,
      "gender": "M",
      "id": 8,
      "name": "Ranbir Kapoor"
    },
    {
      "age": 39,
      "gender": "M",
      "id": 9,
      "name": "Ranveer singh"
    },
    {
      "age": 41,
      "gender": "F",
      "id": 10,
      "name": "Katrina Kaif"
    },
    {
      "age": 43,
      "gender": "F",
      "id": 11,
      "name": "Kareena Kapoor"
    },
    {
      "age": 36,
      "gender": "M",
      "id": 13,
      "name": "Vicky Kaushal"
    }
  ],
  "created_id": 13,
  "success": true,
  "total_actors": 10
}
```

---

`PATCH '/movies/${id}'`

- Sends a patch request in order to modify a specific movie by id
- Request Body:

```json
{
  "genres": ["Comedy"]
}
```

- Returns: the modified movie entry
- {{host}}/movies/7

```json
{
  "success": true,
  "updated_entry": {
    "director": "Anees Bazmee",
    "genres": ["Comedy"],
    "id": 7,
    "release_date": "Fri, 21 Dec 2007 00:00:00 GMT",
    "title": "Welcome"
  }
}
```

---

`PATCH '/actors/${id}'`

- Sends a patch request in order to modify a specific actor by id
- Request Body:

```json
{
  "age": 56
}
```

- Returns: the modified actor entry
- {{host}}/actors/7

```json
{
  "success": true,
  "updated_entry": {
    "age": 56,
    "gender": "F",
    "id": 7,
    "name": "Madhuri Dixit"
  }
}
```

## Testing

The test cases has been been wrtiten for following error codes which return error in json format:

- 404: Resource Not Found
- 500: Internal Server Error
- 405: Method Not Allowed
- 400: Bad Request
- 422: Unprocessable Entity
- 401: Unauthorized
- 403: Forbidden

To run execute the following command:

```bash
python test_app.py
```
