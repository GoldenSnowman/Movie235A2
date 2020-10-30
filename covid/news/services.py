from typing import List, Iterable

from covid.adapters.repository import AbstractRepository
from covid.domain.model import Review, Movie, Director, Actor, Genre


class NonExistentArticleException(Exception):
    pass


class UnknownUserException(Exception):
    pass


def add_review(movie_id: int, review_text: str, username: str, rating: int, repo: AbstractRepository):
    movie = repo.get_movie(movie_id)
    if movie is None:
        raise NonExistentArticleException
    user = repo.get_user(username)
    if user is None:
        raise UnknownUserException

    review = Review(movie, review_text, user, rating)
    review.movie = movie
    movie.add_review(review)
    user.add_review(review)
    repo.add_review(review)


def get_movie(movie_id: int, repo: AbstractRepository):
    movie = repo.get_movie(movie_id)

    if movie is None:
        raise NonExistentArticleException

    return movie_to_dict(movie)

def get_number_of_movies(repo: AbstractRepository):
        number =repo.get_number_of_movies()
        return number
        
def get_first_movie(repo: AbstractRepository):

    movie = repo.get_first_movie()

    return movie_to_dict(movie)


def get_last_movie(repo: AbstractRepository):

    movie = repo.get_last_movie()
    return movie_to_dict(movie)

def get_movie_ids_for_director(director_name, repo: AbstractRepository):
    movie_ids = repo.get_movie_ids_for_director(director_name)
    return movie_ids

def get_movie_ids_for_actor(actor_name, repo: AbstractRepository):
    movie_ids = repo.get_movie_ids_for_actor(actor_name)

    return movie_ids

def get_movie_ids_for_genre(genre_name, repo: AbstractRepository):
    movie_ids = repo.get_movie_ids_for_genre(genre_name)

    return movie_ids

def get_movies_by_id(id_list, repo: AbstractRepository):
    movies = repo.get_movies_by_id(id_list)

    movies_as_dict = movies_to_dict(movies)

    return movies_as_dict


def get_review_for_movie(movie_id, repo: AbstractRepository):
    movie = repo.get_movie(movie_id)

    if movie is None:
        raise NonExistentArticleException

    return reviews_to_dict(movie.reviews)


def movie_to_dict(movie: Movie):
    movie_dict = {
        'id': movie.id,
        'year': movie.year,
        'title': movie.title,
        'description': movie.description,
        'reviews': reviews_to_dict(movie.reviews),
        'director': movie.director,
        'actors': movie.actors,
        'genres': movie.genres
    }
    return movie_dict


def movies_to_dict(movies: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movies]


def review_to_dict(review: Review):
    review_dict = {
        'username': review.user.user_name,
        'movie_id': review.movie.id,
        'review_text': review.review_text,
        'timestamp': review.timestamp,
        'rating': review.rating
    }
    return review_dict


def reviews_to_dict(reviews: Iterable[Review]):
    return [review_to_dict(review) for review in reviews]

def dict_to_movie(dict):
    movie = Movie(dict.title, dict.year)
    movie.id = dict.id
    movie.description = dict.descrption
    movie.reviews = dict.reviews
    movie.director = dict.director
    movie.acotrs = dict.actors
    movie.genres = dict.genres
    return movie
