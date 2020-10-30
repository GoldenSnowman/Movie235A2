from datetime import date, datetime
from typing import List

import pytest
from covid.domain.model import Director, Actor, Genre, Movie, User, Review
from covid.adapters.repository import RepositoryException


def test_repository_can_add_a_user(in_memory_repo):
    user = User('Dave', '123456789')
    in_memory_repo.add_user(user)

    assert in_memory_repo.get_user('Dave') is user


def test_repository_can_retrieve_a_user(in_memory_repo):
    user = in_memory_repo.get_user('fmercury')
    assert user == User('fmercury', '8734gfe2058v')


def test_repository_does_not_retrieve_a_non_existent_user(in_memory_repo):
    user = in_memory_repo.get_user('prince')
    assert user is None


def test_repository_can_retrieve_movie_count(in_memory_repo):
    number_of_movies = in_memory_repo.get_number_of_movies()

    assert number_of_movies == 1000


def test_repository_can_add_and_get_movie(in_memory_repo):
    movie1 = Movie("super cool movie", 2020)
    in_memory_repo.add_movie(movie1)

    assert in_memory_repo.get_movie(1001) is movie1

def test_repository_does_not_retrieve_a_non_existent_movie(in_memory_repo):
    movie = in_memory_repo.get_movie(2000)
    assert movie is None

def test_repository_can_get_first_movie(in_memory_repo):
    movie = in_memory_repo.get_first_movie()
    assert movie.title == 'Guardians of the Galaxy'


def test_repository_can_get_last_movie(in_memory_repo):
    movie = in_memory_repo.get_last_movie()
    assert movie.title == 'Nine Lives'


def test_repository_can_get_movies_by_ids(in_memory_repo):
    movies = in_memory_repo.get_movies_by_id([2, 5, 6])

    assert len(movies) == 3
    assert movies[0].title == 'Prometheus'
    assert movies[1].title == "Suicide Squad"
    assert movies[2].title == 'The Great Wall'


def test_repository_does_not_retrieve_movie_for_non_existent_id(in_memory_repo):
    movies = in_memory_repo.get_movies_by_id([2,2000])

    assert len(movies) == 1
    assert movies[0].title == 'Prometheus'

def test_repository_returns_an_empty_list_for_non_existent_ids(in_memory_repo):
    movies = in_memory_repo.get_movies_by_id([0, 2000])

    assert len(movies) == 0

def test_repository_can_add_a_review(in_memory_repo):
    user = in_memory_repo.get_user('thorke')
    movie = in_memory_repo.get_movie(2)
    review = Review(movie, "wow this is a super cool movie", user, 8)

    in_memory_repo.add_review(review)

    assert review in in_memory_repo.get_reviews()

def test_repository_can_retrieve_reviews(in_memory_repo):
    assert len(in_memory_repo.get_reviews()) == 3



