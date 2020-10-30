from datetime import date

import pytest

from covid.authentication.services import AuthenticationException
from covid.news import services as news_services
from covid.authentication import services as auth_services
from covid.news.services import NonExistentArticleException


def test_can_add_user(in_memory_repo):
    new_username = 'jz'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    user_as_dict = auth_services.get_user(new_username, in_memory_repo)
    assert user_as_dict['username'] == new_username

    # Check that password has been encrypted.
    assert user_as_dict['password'].startswith('pbkdf2:sha256:')


def test_cannot_add_user_with_existing_name(in_memory_repo):
    username = 'thorke'
    password = 'abcd1A23'

    with pytest.raises(auth_services.NameNotUniqueException):
        auth_services.add_user(username, password, in_memory_repo)


def test_authentication_with_valid_credentials(in_memory_repo):
    new_username = 'pmccartney'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    try:
        auth_services.authenticate_user(new_username, new_password, in_memory_repo)
    except AuthenticationException:
        assert False


def test_authentication_with_invalid_credentials(in_memory_repo):
    new_username = 'pmccartney'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    with pytest.raises(auth_services.AuthenticationException):
        auth_services.authenticate_user(new_username, '0987654321', in_memory_repo)

def test_can_get_movie(in_memory_repo):
    movie_id = 1

    movie = news_services.get_movie(movie_id, in_memory_repo)

    assert movie['id'] == movie_id
    assert movie['title'] == 'Guardians of the Galaxy'

def test_get_first_movie(in_memory_repo):
    movie = news_services.get_first_movie(in_memory_repo)

    assert movie['id'] == 1


def test_get_last_movie(in_memory_repo):
    movie = news_services.get_last_movie(in_memory_repo)

    assert movie['id'] == 1000

def test_get_movie_by_id(in_memory_repo):
    target_movie_ids = [5, 6, 7, 8]
    movies_as_dict = news_services.get_movies_by_id(target_movie_ids, in_memory_repo)

    assert len(movies_as_dict) == 4
    movie_ids = [movie['id'] for movie in movies_as_dict]
    assert set([5, 6, 7, 8]).issubset(movie_ids)
