from flask import Blueprint, request, render_template, redirect, url_for, session

import covid.adapters.repository as repo
import covid.utilities.services as services


utilities_blueprint = Blueprint(
    'utilities_bp', __name__)



def get_director_urls():
    director_names = services.get_director_names(repo.repo_instance)
    director_urls = dict()
    for director_name in director_names:
        director_urls[director_name] = url_for('news_bp.movie_by_director', director=director_name)

    return director_urls

def get_actor_urls():
    actor_names = services.get_actor_names(repo.repo_instance)
    actor_urls = dict()
    for actor_name in actor_names:
        actor_urls[actor_name] = url_for('news_bp.movie_by_actor', actor=actor_name)

    return actor_urls

def get_genre_urls():
    genre_names = services.get_genre_names(repo.repo_instance)
    genre_urls = dict()
    for genre_name in genre_names:
        genre_urls[genre_name] = url_for('news_bp.movie_by_genre', genre=genre_name)
    
    return genre_urls