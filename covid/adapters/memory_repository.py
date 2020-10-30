import csv
import os
from datetime import date, datetime
from typing import List

from bisect import bisect, bisect_left, insort_left

from werkzeug.security import generate_password_hash

from covid.adapters.repository import AbstractRepository, RepositoryException
from covid.domain.model import Director, Actor, Genre, Movie, User, Review


class MemoryRepository(AbstractRepository):

    def __init__(self):
        self._movies = list()
        self._movies_index = dict()
        self._directors = list()
        self._actors = list()
        self._genres = list()
        self._users = list()
        self._reviews = list()

    def add_user(self, user: User):
        self._users.append(user)

    def get_user(self, username: str) -> User:
        return next((user for user in self._users if str(user.user_name) == username), None)

        return super().get_directors()
    def add_movie(self, movie: Movie):
        insort_left(self._movies, movie)
        self._movies_index[movie.id] = movie

    def get_movie(self, id: int) -> Movie:
        movie = None

        try:
            movie = self._movies_index[id]
        except KeyError:
            pass  # Ignore exception and return None.

        return movie

    def get_number_of_movies(self):
        return len(self._movies)

    def get_first_movie(self):
        movie = None

        if len(self._movies) > 0:
            movie = self._movies[0]
        return movie

    def get_last_movie(self):
        movie = None

        if len(self._movies) > 0:
            movie = self._movies[-1]
        return movie

    def get_movies_by_id(self, id_list):
        existing_ids = [id for id in id_list if id in self._movies_index]

        movies = [self._movies_index[id] for id in existing_ids]
        return movies

    def get_movie_ids_for_director(self, director_full_name: str):
        movie_list=[]
        for movie in self._movies:
            if movie.director.director_full_name == director_full_name:
                movie_list.append(movie.id)
        return movie_list

    def get_movie_ids_for_actor(self, actor_full_name: str):
        movie_list=[]
        for movie in self._movies:
            for actor in movie.actors:
                if actor.actor_full_name == actor_full_name:
                    movie_list.append(movie.id)
        return movie_list
    
    def get_movie_ids_for_genre(self, genrel_name: str):
        movie_list=[]
        for movie in self._movies:
            for genre in movie.genres:
                if genre.genre_name == genrel_name:
                    movie_list.append(movie.id)
        return movie_list

    def add_director(self, director: Director):
        self._directors.append(director)

    def add_actor(self, actor: Actor):
        self._actors.append(actor)

    def add_genre(self, genre: Genre):
        self._genres.append(genre)

    def get_directors(self) -> List[Director]:
        return self._directors

    def get_actors(self) -> List[Actor]:
        return self._actors

    def get_genres(self) -> List[Genre]:
        return self._genres

    def add_review(self, review: Review):
        super().add_review(review)
        self._reviews.append(review)

    def get_review(self):
        return self._reviews

    def movie_index(self, movie: Movie):
        index = bisect_left(self._movies, movie)
        if index != len(self._movies) and self._movies[index].year == movie.year:
            return index
        raise ValueError


def load_data(data_path: str, repo: MemoryRepository):
    with open(os.path.join(data_path, 'Data1000Movies.csv'), mode='r', encoding='utf-8-sig') as csvfile:
        movie_file_reader = csv.DictReader(csvfile)

        index = 0
        for row in movie_file_reader:
            title = row['Title']
            release_year = int(row['Year'])
            movie = Movie(title, release_year)
            movie.id = int(row['Rank'])
            movie.description = row['Description']
            director = row["Director"]
            d = Director(director)
            repo.add_director(d)
            movie.director = d
            genres = row["Genre"]
            for genre in genres.split(","):
                g = Genre(genre)
                repo.add_genre(g)
                movie.add_genre(g)
            actors = row["Actors"]
            for actor in actors.split(","):
                a = Actor(actor)
                repo.add_actor(a)
                movie.add_actor(a)

            repo.add_movie(movie)

            index += 1

def load_users(data_path: str, repo: MemoryRepository):
    with open(os.path.join(data_path, 'users.csv'), mode='r', encoding='utf-8-sig') as csvfile:
        movie_file_reader = csv.DictReader(csvfile)

        users=dict()
        index = 0
        for row in movie_file_reader:
            user = User(
                user_name=row['username'],
                password=row['password']
            )
            repo.add_user(user)
            users[row['id']] = user
            index+=1
    return users


def load_reviews(data_path: str, repo: MemoryRepository, users):
    with open(os.path.join(data_path, 'reviews.csv'), mode='r', encoding='utf-8-sig') as csvfile:
        movie_file_reader = csv.DictReader(csvfile)

        index = 0
        for row in movie_file_reader:
            r = Review(movie = None, review_text=row['text'],user = None, rating = int(row['rating']))
            r.timestamp = row['timestamp']
            user = repo.get_user(users[row['author-id']].user_name)
            user.add_review(r)
            r.user = user
            m = repo.get_movie(int(row['movie-id']))
            m.add_review(r)
            r.movie = m
            repo.add_review(r)

            index+=1


def populate(data_path: str, repo: MemoryRepository):
    load_data(data_path, repo)
    users = load_users(data_path, repo)
    load_reviews(data_path, repo, users)
