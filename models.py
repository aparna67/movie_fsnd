from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ARRAY, String

db = SQLAlchemy()

##Using abstract class, to avoid duplication of methods


class BaseModel(db.Model):
    __abstract__ = True

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class Movie(BaseModel):
    __tablename__ = "Movie"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    release_date = db.Column(db.Date)
    genres = Column(ARRAY(String))
    director = db.Column(db.String)

    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date,
            "genres": self.genres,
            "director": self.director,
        }


class Actor(BaseModel):
    __tablename__ = "Actor"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
        }
