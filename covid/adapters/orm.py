from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, DateTime,
    ForeignKey
)
from sqlalchemy.orm import mapper, relationship

from covid.domain import model

metadata = MetaData()
users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('username', String(255), unique=True, nullable=False),
    Column('password', String(255), nullable=False)
)

reviews = Table(
    'reviews', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', ForeignKey('users.id')),
    Column('movie_id', ForeignKey('movies.id')),
    Column('review', String(1024), nullable=False),
    Column('timestamp', DateTime, nullable=False),
    Column('rating', Integer, nullable=False)
)

movies = Table(
    'movies', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('year', Integer, nullable=False),
    Column('title', String(255), nullable=False),
    Column('description', String(1024), nullable=False)
)

directors = Table(
    'directors', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(64), nullable=False)
)

movie_directors = Table(
    'movie_directors', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('movie_id', ForeignKey('movies.id')),
    Column('director_id', ForeignKey('directors.id'))
)

actors = Table(
    'actors', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(64), nullable=False)
)

movie_actors = Table(
    'movie_actors', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('movie_id', ForeignKey('movies.id')),
    Column('actor_id', ForeignKey('actors.id'))
)

genres = Table(
    'genres', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(64), nullable=False)
)

movie_genres = Table(
    'movie_genres', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('movie_id', ForeignKey('movies.id')),
    Column('genre_id', ForeignKey('genres.id'))
)


def map_model_to_tables():
    mapper(model.User, users, properties={
        '_User__user_name': users.c.username,
        '_User__password': users.c.password,
        '_User__reviews': relationship(model.Review, backref='_Review__user')
    })
    mapper(model.Review, reviews, properties={
        '_Review__review_text': reviews.c.review,
        '_Review__timestamp': reviews.c.timestamp,
        '_Review__rating': reviews.c.rating
    })
    mapper(model.Movie, movies, properties={
        '_Movie__id': movies.c.id,
        '_Movie__year': movies.c.year,
        '_Movie__title': movies.c.title,
        '_Movie__description': movies.c.description,
        '_Movie__reviews': relationship(model.Review, backref='_Review__movie'),
        '_Movie__director': relationship(model.Director, secondary=movie_directors),
        '_Movie__actors': relationship(model.Actor, secondary=movie_actors),
        '_Movie__genres': relationship(model.Genre, secondary=movie_genres)
    })
    mapper(model.Director, directors, properties={
        '_Director__director_full_name': directors.c.name
    })

    mapper(model.Actor, actors, properties={
        '_Actor__actor_full_name': actors.c.name
    })

    mapper(model.Genre, genres, properties={
        '_Genre__genre_name': genres.c.name
    })
