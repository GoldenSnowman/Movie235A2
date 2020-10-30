from datetime import date

from flask import Blueprint
from flask import request, render_template, redirect, url_for, session

from better_profanity import profanity
from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError

import covid.adapters.repository as repo
import covid.utilities.utilities as utilities
import covid.news.services as services

from covid.authentication.authentication import login_required

from covid.utilities import utilities

news_blueprint = Blueprint(
    'news_bp', __name__)


@news_blueprint.route('/movies_by_id', methods=['GET'])
def movies_by_id():
    movies_per_page = 3

    cursor = request.args.get('cursor')
    movie_to_show_reviews = request.args.get('view_reviews_for')

    if movie_to_show_reviews is None:
        movie_to_show_reviews = -1
    else:
        movie_to_show_reviews = int(movie_to_show_reviews)

    if cursor is None:
        cursor = 0
    else:
        cursor = int(cursor)

    movie_ids = []
    for i in range(1, services.get_number_of_movies(repo.repo_instance)+1):
        movie_ids.append(i)
    movies = services.get_movies_by_id(movie_ids[cursor:cursor + movies_per_page], repo.repo_instance)

    first_movie_url = None
    last_movie_url = None
    next_movie_url = None
    prev_movie_url = None

    if cursor > 0:
        prev_movie_url = url_for('news_bp.movies_by_id', cursor=cursor - movies_per_page)
        first_movie_url = url_for('news_bp.movies_by_id')

    if cursor + movies_per_page < len(movie_ids):
        next_movie_url = url_for('news_bp.movies_by_id',  cursor=cursor + movies_per_page)

        last_cursor = movies_per_page * int(len(movie_ids) / movies_per_page)
        if len(movie_ids) % movies_per_page == 0:
            last_cursor -= movies_per_page
        last_movie_url = url_for('news_bp.movies_by_id', cursor=last_cursor)

    for movie in movies:
        movie['view_review_url'] = url_for('news_bp.movies_by_id', cursor=cursor, view_reviews_for=movie['id'])
        movie['add_review_url'] = url_for('news_bp.review_on_movie', movie=movie['id'])


    return render_template(
        'news/movies.html',
        title='Movies',
        articles_title="All Movies",
        movies=movies,
        first_movie_url=first_movie_url,
        last_movie_url=last_movie_url,
        prev_movie_url=prev_movie_url,
        next_movie_url=next_movie_url,
        show_reviews_for_movie=movie_to_show_reviews
    )

    return redirect(url_for('home_bp.home'))


@news_blueprint.route('/movie_by_director', methods=['GET'])
def movie_by_director():
    movies_per_page = 3

    director_name = request.args.get('director')
    cursor = request.args.get('cursor')
    movie_to_show_reviews = request.args.get('view_reviews_for')

    if movie_to_show_reviews is None:
        movie_to_show_reviews = -1
    else:
        movie_to_show_reviews = int(movie_to_show_reviews)

    if cursor is None:
        cursor = 0
    else:
        cursor = int(cursor)

    movie_ids = services.get_movie_ids_for_director(director_name, repo.repo_instance)

    movies = services.get_movies_by_id(movie_ids[cursor:cursor + movies_per_page], repo.repo_instance)

    first_movie_url = None
    last_movie_url = None
    next_movie_url = None
    prev_movie_url = None

    if cursor > 0:
        prev_movie_url = url_for('news_bp.movie_by_director', director=director_name, cursor=cursor - movies_per_page)
        first_movie_url = url_for('news_bp.movie_by_director', director=director_name)

    if cursor + movies_per_page < len(movie_ids):
        next_movie_url = url_for('news_bp.movie_by_director', director=director_name, cursor=cursor + movies_per_page)

        last_cursor = movies_per_page * int(len(movie_ids) / movies_per_page)
        if len(movie_ids) % movies_per_page == 0:
            last_cursor -= movies_per_page
        last_movie_url = url_for('news_bp.movie_by_director', director=director_name, cursor=last_cursor)

    for movie in movies:
        movie['view_review_url'] = url_for('news_bp.movie_by_director', director=director_name, cursor=cursor, view_reviews_for=movie['id'])
        movie['add_review_url'] = url_for('news_bp.review_on_movie', movie=movie['id'])

    return render_template(
        'news/movies.html',
        title='Movies',
        articles_title="All Movies",
        movies=movies,
        first_movie_url=first_movie_url,
        last_movie_url=last_movie_url,
        prev_movie_url=prev_movie_url,
        next_movie_url=next_movie_url,
        show_reviews_for_movie=movie_to_show_reviews
    )

@news_blueprint.route('/directors', methods=['GET'])
def directors():
    director_urls=utilities.get_director_urls()
    return render_template(
        'news/directors.html',
        director_urls=director_urls
    )
@news_blueprint.route('/movie_by_actor', methods=['GET'])
def movie_by_actor():
    movies_per_page = 3

    actor_name = request.args.get('actor')
    cursor = request.args.get('cursor')
    movie_to_show_reviews = request.args.get('view_reviews_for')

    if movie_to_show_reviews is None:
        movie_to_show_reviews = -1
    else:
        movie_to_show_reviews = int(movie_to_show_reviews)

    if cursor is None:
        cursor = 0
    else:
        cursor = int(cursor)

    movie_ids = services.get_movie_ids_for_actor(actor_name, repo.repo_instance)

    movies = services.get_movies_by_id(movie_ids[cursor:cursor + movies_per_page], repo.repo_instance)

    first_movie_url = None
    last_movie_url = None
    next_movie_url = None
    prev_movie_url = None

    if cursor > 0:
        prev_movie_url = url_for('news_bp.movie_by_actor', actor=actor_name, cursor=cursor - movies_per_page)
        first_movie_url = url_for('news_bp.movie_by_actor', actor=actor_name)

    if cursor + movies_per_page < len(movie_ids):
        next_movie_url = url_for('news_bp.movie_by_actor', actor=actor_name, cursor=cursor + movies_per_page)

        last_cursor = movies_per_page * int(len(movie_ids) / movies_per_page)
        if len(movie_ids) % movies_per_page == 0:
            last_cursor -= movies_per_page
        last_movie_url = url_for('news_bp.movie_by_actor', actor=actor_name, cursor=last_cursor)

    for movie in movies:
        movie['view_review_url'] = url_for('news_bp.movie_by_actor', actor=actor_name, cursor=cursor, view_reviews_for=movie['id'])
        movie['add_review_url'] = url_for('news_bp.review_on_movie', movie=movie['id'])

    return render_template(
        'news/movies.html',
        title='Movies',
        articles_title="All Movies",
        movies=movies,
        first_movie_url=first_movie_url,
        last_movie_url=last_movie_url,
        prev_movie_url=prev_movie_url,
        next_movie_url=next_movie_url,
        show_reviews_for_movie=movie_to_show_reviews
    )

@news_blueprint.route('/actors', methods=['GET'])
def actors():
    actor_urls=utilities.get_actor_urls()
    return render_template(
        'news/actors.html',
        actor_urls=actor_urls
    )

@news_blueprint.route('/movie_by_genre', methods=['GET'])
def movie_by_genre():
    movies_per_page = 3

    genre_name = request.args.get('genre')
    cursor = request.args.get('cursor')
    movie_to_show_reviews = request.args.get('view_reviews_for')

    if movie_to_show_reviews is None:
        movie_to_show_reviews = -1
    else:
        movie_to_show_reviews = int(movie_to_show_reviews)

    if cursor is None:
        cursor = 0
    else:
        cursor = int(cursor)

    movie_ids = services.get_movie_ids_for_genre(genre_name, repo.repo_instance)

    movies = services.get_movies_by_id(movie_ids[cursor:cursor + movies_per_page], repo.repo_instance)

    first_movie_url = None
    last_movie_url = None
    next_movie_url = None
    prev_movie_url = None

    if cursor > 0:
        
        prev_movie_url = url_for('news_bp.movie_by_genre', genre=genre_name, cursor=cursor - movies_per_page)
        first_movie_url = url_for('news_bp.movie_by_genre', genre=genre_name)

    if cursor + movies_per_page < len(movie_ids):
       
        next_movie_url = url_for('news_bp.movie_by_genre', genre=genre_name, cursor=cursor + movies_per_page)

        last_cursor = movies_per_page * int(len(movie_ids) / movies_per_page)
        if len(movie_ids) % movies_per_page == 0:
            last_cursor -= movies_per_page
        last_movie_url = url_for('news_bp.movie_by_genre', genre=genre_name, cursor=last_cursor)

    for movie in movies:
        movie['view_review_url'] = url_for('news_bp.movie_by_genre', genre=genre_name, cursor=cursor, view_reviews_for=movie['id'])
        movie['add_review_url'] = url_for('news_bp.review_on_movie', movie=movie['id'])

    return render_template(
        'news/movies.html',
        title='Movies',
        articles_title="All Movies",
        movies=movies,
        first_movie_url=first_movie_url,
        last_movie_url=last_movie_url,
        prev_movie_url=prev_movie_url,
        next_movie_url=next_movie_url,
        show_reviews_for_movie=movie_to_show_reviews
    )

@news_blueprint.route('/genres', methods=['GET'])
def genres():
    genre_urls=utilities.get_genre_urls()
    return render_template(
        'news/genres.html',
        genre_urls=genre_urls
    )

@news_blueprint.route('/review', methods=['GET', 'POST'])
@login_required
def review_on_movie():
    username = session['username']

    form = ReviewForm()

    if form.validate_on_submit():

        movie_id = int(form.movie_id.data)

        services.add_review(movie_id, form.review.data, username, form.rating.data, repo.repo_instance)

        movie = services.get_movie(movie_id, repo.repo_instance)

        return redirect(url_for('news_bp.movies_by_id', view_reviews_for=movie_id))

    if request.method == 'GET':
        movie_id = int(request.args.get('movie'))

        form.movie_id.data = movie_id
    else:
        movie_id = int(form.movie_id.data)

    movie = services.get_movie(movie_id, repo.repo_instance)
    return render_template(
        'news/review_on_movie.html',
        title='Edit Movie',
        movie=movie,
        form=form,
        handler_url=url_for('news_bp.review_on_movie'),
    )


class ProfanityFree:
    def __init__(self, message=None):
        if not message:
            message = u'Field must not contain profanity'
        self.message = message

    def __call__(self, form, field):
        if profanity.contains_profanity(field.data):
            raise ValidationError(self.message)


class ReviewForm(FlaskForm):
    rating = IntegerField('Rating',{
        DataRequired()
    })
    review = TextAreaField('Review', [
        DataRequired(),
        Length(min=4, message='Your review is too short'),
        ProfanityFree(message='Your review must not contain profanity')])
    movie_id = HiddenField("Movie id")
    submit = SubmitField('Submit')