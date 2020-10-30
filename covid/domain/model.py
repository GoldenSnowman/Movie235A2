from datetime import date, datetime
from typing import List, Iterable


class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    @director_full_name.setter
    def director_full_name(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        return self.__director_full_name == other.__director_full_name

    def __lt__(self, other):
        return self.__director_full_name < other.__director_full_name

    def __hash__(self):
        return hash(self.__director_full_name)


class Actor:
    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self.__colleague = []
        self.__movies = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    @actor_full_name.setter
    def actor_full_name(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        return self.__actor_full_name == other.__actor_full_name

    def __lt__(self, other):
        return self.__actor_full_name < other.__actor_full_name

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        self.__colleague.append(colleague)
    
    def check_if_this_actor_worked_with(self, colleague):
        if colleague in self.__colleague:
            return True
        else:
            return False


class Genre:
    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    @genre_name.setter
    def genre_name(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        return self.__genre_name == other.__genre_name

    def __lt__(self, other):
        return self.__genre_name < other.__genre_name

    def __hash__(self):
        return hash(self.__genre_name)


class Movie:
    def __init__(self, title: str, year: int):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()
        if year <= 1900 or type(year) is not int:
            self.__year = None
        else:
            self.__year = year

        self.__id = None
        self.__description = None
        self.__director = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = None
        self.__similar_movies = []
        self.__reviews = []

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        if year <= 1900 or type(year) is not int:
            self.__year = None
        else:
            self.__year = year

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        if description == "" or type(description) is not str:
            self.__description = None
        else:
            self.__description = description.strip()

    @property
    def director(self) -> Director:
        return self.__director

    @director.setter
    def director(self, director: Director):
        if type(director) is not Director:
            self.__director = None
        else:
            self.__director = director

    @property
    def actors(self) -> list:
        return self.__actors

    @actors.setter
    def actors(self, actors: list):
        if type(actors) is not list:
            self.__actors = []
        else:
            self.__actors = actors

    @property
    def genres(self) -> list:
        return self.__genres

    @genres.setter
    def genres(self, genres: list):
        if type(genres) is not list:
            self.__genres = []
        else:
            self.__genres = genres
    
    @property
    def reviews(self) -> list:
        return self.__reviews

    @reviews.setter
    def reviews(self, reviews: list):
        if type(reviews) is not list:
            self.__reviews = []
        else:
            self.__reviews = reviews

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes: int):
        if runtime_minutes <= 0:
            raise ValueError
        else:
            self.__runtime_minutes = runtime_minutes
    
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        if id <= 0:
            raise ValueError
        else:
            self.__id = id

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__year}>"

    def __eq__(self, other):
        return (self.__title, self.__year) == (other.__title, other.__year)

    def __lt__(self, other):
        return (self.__title, self.__year) < (other.__title, other.__year)

    def __hash__(self):
        return hash((self.__title, self.__year))

    def add_actor(self, actor: Actor):
        if type(actor) is Actor:
            self.__actors.append(actor)

    def remove_actor(self, actor: Actor):
        if actor in self.__actors:
            self.__actors.remove(actor)

    def add_genre(self, genre: Genre):
        if type(genre) is Genre:
            self.__genres.append(genre)

    def remove_genre(self, genre: Genre):
        if genre in self.__genres:
            self.__genres.remove(genre)

    def add_similar_movies(self, movie):
        if movie not in self.__similar_movies:
            self.__similar_movies.append(movie)

    def similar_movies(self):
        return self.__similar_movies
    
    def add_review(self, review: 'Review'):
        self.__reviews.append(review)


class User:
    def __init__(self, user_name: str, password: str):
        if user_name == "" or type(user_name) is not str:
            self.__user_name = None
        else:
            self.__user_name = user_name.strip().lower()
        if password == "" or type(password) is not str:
            self.__password = None
        else:
            self.__password = password.strip()
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    @property
    def user_name(self) -> str:
        return self.__user_name

    @user_name.setter
    def user_name(self, user_name: str):
        if user_name == "" or type(user_name) is not str:
            self.__user_name = None
        else:
            self.__user_name = user_name.strip().lower()

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        if password == "" or type(password) is not str:
            self.__password = None
        else:
            self.__password = password.strip()

    @property
    def watched_movies(self) -> list:
        return self.__watched_movies

    @watched_movies.setter
    def watched_movies(self, watched_movies: list):
        if watched_movies == "" or type(watched_movies) is not list:
            self.__watched_movies = []
        else:
            self.__watched_movies = watched_movies

    @property
    def reviews(self) -> list:
        return self.__reviews

    @reviews.setter
    def reviews(self, reviews: list):
        if reviews == "" or type(reviews) is not list:
            self.__reviews = []
        else:
            self.__reviews = reviews

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__time_spent_watching_movies_minutes

    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self, time_spent_watching_movies_minutes: int):
        if time_spent_watching_movies_minutes < 0:
            raise ValueError
        else:
            self.__time_spent_watching_movies_minutes = time_spent_watching_movies_minutes

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        return self.__user_name == other.__user_name

    def __lt__(self, other):
        return self.__user_name < other.__user_name

    def __hash__(self):
        return hash(self.__user_name)

    def watch_movie(self, movie: Movie):
        self.__watched_movies.append(movie)
        self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review: 'Review'):
        self.__reviews.append(review)


class Review:
    def __init__(self, movie: Movie, review_text: str,user: User, rating: int):
        self.__movie = movie
        self.__review_text = review_text.strip()
        if rating < 1 or rating > 10:
            self.__rating = None
        else:
            self.__rating = rating
        self.__timestamp = datetime.now()
        self.__user = user

    @property
    def movie(self) -> Movie:
        return self.__movie

    @movie.setter
    def movie(self, movie: Movie):
        self.__movie = movie

    @property
    def review_text(self) -> str:
        return self.__review_text

    @review_text.setter
    def review_text(self, review_text: str):
        self.__review_text = review_text.strip()

    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, rating: int):
        if rating < 1 or rating > 10:
            self.__rating = None
        else:
            self.__rating = rating

    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        self.__timestamp = timestamp
    
    @property
    def user(self) -> User:
        return self.__user

    @user.setter
    def user(self, user: User):
        self.__user = user

    def __repr__(self):
        return f"<Review {self.__movie}, {self.__review_text}, {self.__rating }, {self.__timestamp}>"

    def __eq__(self, other):
        return (self.__movie, self.__review_text, self.__rating, self.__timestamp) == (other.__movie, other.__review_text, other.__rating, other.__timestamp)


class WatchList:
    def __init__(self):
        self.__watchlist = []

    def add_movie(self, movie: Movie):
        if movie in self.__watchlist or type(movie) is not Movie:
            pass
        else:
            self.__watchlist.append(movie)

    def remove_movie(self, movie: Movie):
        if movie in self.__watchlist:
            self.__watchlist.remove(movie)

    def select_movie_to_watch(self, index):
        if len(self.__watchlist) <= index:
            return None
        else:
            return self.__watchlist[index]

    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self):
        if len(self.__watchlist) == 0:
            return None
        else:
            return self.__watchlist[0]

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.size():
            result = self.__watchlist.index(self.n)
            self.n += 1
            return result
        else:
            raise StopIteration


class ModelException(Exception):
    pass
