from datetime import date

from covid.domain.model import Director, Actor, Genre, Movie, User, Review
import pytest


def test_director(self):
    director1 = Director("Taika Waititi")
    assert repr(director1) == "<Director Taika Waititi>"

def test_actor(self):
    actor1 = Actor("Taika Waititi")
    assert repr(actor1) == "<Actor Taika Waititi>"

def test_genre(self):
    genre1 = Genre("Action")
    assert repr(genre1) == "<Genre Action>"

def test_movie(self):
    movie1 = Movie("super cool movie", 2020)
    assert repr(movie1) == "<Movie super cool movie, 2020>"

def test_user_construction(self):
    user1 = User("cooldude","ABcd1234")
    assert user1.user_name == 'cooldude'
    assert user1.password == 'ABcd1234'

def test_review(self):
    movie1 = Movie("super cool movie", 2020)
    text="wow this is a super cool movie"
    user1 = User("cooldude","ABcd1234")
    review1 = Review(movie1, text, user1, 8)
    assert review1.review_text == "wow this is a super cool movie"