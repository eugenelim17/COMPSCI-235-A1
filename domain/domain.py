import csv
from datetime import datetime

class Actor:
    def __init__(self, actor_full_name: str):
        self._colleague = list()
        if actor_full_name == "" or type(actor_full_name) is not str:
            self._actor_full_name = None
        else:
            self._actor_full_name = actor_full_name.strip()

    @property
    def actor_full_name(self) -> str:
        return self._actor_full_name

    def __repr__(self):
        return f"<Actor {self._actor_full_name}>"

    def __eq__(self, other) -> bool:
        return other._actor_full_name == self._actor_full_name

    def __lt__(self, other):
        return self._actor_full_name < other._actor_full_name

    def __hash__(self):
        return hash(self._actor_full_name)

    def add_actor_colleague(self, colleague):
        colleague._colleague.append(self)
        self._colleague.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        return colleague in self._colleague


class Genre:
    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self._genre_name = None
        else:
            self._genre_name = genre_name.strip()

    @property
    def genre_name(self) -> str:
        return self._genre_name

    def __repr__(self):
        return f"<Genre {self._genre_name}>"

    def __eq__(self, other) -> bool:
        return other._genre_name == self._genre_name

    def __lt__(self, other):
        return self._genre_name < other._genre_name

    def __hash__(self):
        return hash(self._genre_name)


class Director:
    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self._director_full_name = None
        else:
            self._director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self._director_full_name

    def __repr__(self):
        return f"<Director {self._director_full_name}>"

    def __eq__(self, other) -> bool:
        return other._director_full_name == self._director_full_name

    def __lt__(self, other):
        return self._director_full_name < other._director_full_name

    def __hash__(self):
        return hash(self._director_full_name)


class Movie:
    def __init__(self, title=None, release_year=None, description=None, director=None, actors=[], genres=[],
                 runtime_minutes=None):
        self._actors = actors
        self._genres = genres
        self._description = description
        self._runtime_minutes = runtime_minutes
        self._director = director
        # title
        if title == "" or type(title) is not str or title == None:
            self._title = None
        else:
            self._title = title.strip()
        # release_year
        if type(release_year) != int or release_year == None or release_year <= 0:
            self._release_year = None
        else:
            self._release_year = release_year

    @property
    def movie(self, title, release_year) -> str:
        return self

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if description == "" or description == None or type(description) != str:
            self._description = None
        else:
            self._description = description.strip()

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, director):
        if self._director is None:
            if type(director) == Director:
                self._director = director
            else:
                self._director = None

    @property
    def actors(self):
        return self._actors

    @actors.setter
    def actors(self, actors):
        if type(actors) == list:
            self._actors = actors
        else:
            self._actors = []

    @property
    def genres(self):
        return self._genres

    @genres.setter
    def genres(self, genres):
        if type(genres) == list:
            self._genres = genres
        else:
            self._genres = []

    @property
    def runtime_minutes(self):
        return self._runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes):
        if type(runtime_minutes) != int or runtime_minutes is None or int(
                runtime_minutes) <= 0 or runtime_minutes == "":
            raise ValueError()
        else:
            self._runtime_minutes = runtime_minutes

    def __repr__(self):
        return f"<Movie {self._title}, {self._release_year}>"

    def __eq__(self, other) -> bool:
        result = (self._title, self._release_year) == \
                 (other._title, other._release_year)
        return result

    def __lt__(self, other):
        result = (self._title, self._release_year) < (other._title, other._release_year)
        return result

    def __hash__(self):
        value = hash((self._title, self._release_year))
        return value

    def add_actor(self, actor):
        if type(actor) == Actor:
            self._actors.append(actor)

    def remove_actor(self, actor):
        if type(actor) == Actor:
            if actor in self._actors:
                self._actors.remove(actor)

    def add_genre(self, genre):
        if type(genre) == Genre:
            self._genres.append(genre)

    def remove_genre(self, genre):
        if type(genre) == Genre:
            if genre in self._genres:
                self._genres.remove(genre)


class MovieFileCSVReader:
    def __init__(self, file_name: str):
        self.__file_name = file_name

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            index = 0
            for row in movie_file_reader:
                rank = row['Rank']
                movie = Movie(row['Title'], int(row['Year']))
                movie.runtime_minutes = row['Runtime (Minutes)']
                genre = row['Genre']
                description = row['Description']
                director = row['Director']
                actors = row['Actors']
                year = row['Year']
                rating = row['Rating']
                votes = row['Votes']
                revenue = row['Revenue (Millions)']
                metascore = row['Metascore']
                #print(f"Movie {index} with title: {title}, release year {release_year}")
                index += 1
            return movie_file_reader

    @property
    def dataset_of_movies(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            movies = []
            for row in movie_file_reader:
                movie = Movie(row['Title'], int(row['Year']))
                movie.runtime_minutes = row['Runtime (Minutes)']
                movies += [movie]
            return movies

    @property
    def dataset_of_directors(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            directors = set()
            for row in movie_file_reader:
                director = Director(str(row['Director'].strip()))
                if director not in directors:
                    directors.add(director)
            return directors

    @property
    def dataset_of_actors(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            actors = set()
            for row in movie_file_reader:
                i = row['Actors'].split(",")
                for actor in i:
                    actor = Actor(actor.strip())
                    if actor not in actors:
                        actors.add(actor)
            return actors

    @property
    def dataset_of_genres(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            genres = set()
            for row in movie_file_reader:
                i = row['Genre'].split(",")
                for genre in i:
                    genre = Genre(genre.strip())
                    if genre not in genres:
                        genres.add(genre)
            return genres



class Review:
    def __init__(self, movie = None, review_text = None, rating = None):
        self._timestamp = datetime.today()
        if (type(rating) == int and rating >= 1 and rating <= 10):
            self._rating = rating
        else:
            self._rating = None
        if type(review_text) == str and review_text != "":
            self._review_text = review_text.strip()
        else:
            self._review_text = None
        if type(movie) == Movie:
            self._movie = movie
        else:
            self._movie = None


    @property
    def timestamp(self):
        return self._timestamp

    @property
    def movie(self):
        return self._movie

    @movie.setter
    def movie(self, movie):
        if type(movie) == Movie:
            self._movie = movie
        else:
            self._movie = None

    @property
    def review_text(self):
        return self._review_text

    @review_text.setter
    def review_text(self, review_text):
        if type(review_text) == str and review_text != "":
            self._review_text = review_text.strip()
        else:
            self._review_text = None

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        if (type(rating) == int and rating >= 1 and rating <= 10):
            self._rating = rating
        else:
            self._rating = None


    def __repr__(self):
        return f"<Review: {self._review_text}, Rating: {self._rating}, Time: {self._timestamp}>"

    def __eq__(self, other) -> bool:
        result = (self._rating, self._review_text) == (other._rating, other._review_text)
        return result


class User:
    def __init__(self, user_name: str, password: str, watched_movies = None, reviews = None, time_spent_watching_movies_minutes = None):
        if type(user_name) == str and user_name != "":
            self._user_name = user_name.strip().lower()
        else:
            self._user_name = None
        if type(password) == str and password != "":
            self._password = password
        else:
            self._password = None
        if type(watched_movies) == list:
            self._watched_movies = watched_movies
        else:
            self._watched_movies = []
        if type(reviews) == list:
            self._reviews = reviews
        else:
            self._reviews = []
        if type(time_spent_watching_movies_minutes) == int and time_spent_watching_movies_minutes >= 0:
            self._time_spent_watching_movies_minutes = time_spent_watching_movies_minutes
        else:
            self._time_spent_watching_movies_minutes = 0
        if type(watch_later) == list:
            self._watch_later = watch_later;

    @property
    def user_name(self) -> str:
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        if type(user_name) == str and user_name != "":
            self._user_name = user_name.strip().lower()
        else:
            self._user_name = None

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, password):
        if type(password) == str and password != "":
            self._password = password
        else:
            self._password = None

    @property
    def watched_movies(self):
        return self._watched_movies

    @watched_movies.setter
    def watched_movies(self, watched_movies):
        if type(watched_movies) == list:
            self._watched_movies = watched_movies
        else:
            self._watched_movies = None

    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self, reviews):
        if type(reviews) == list:
            self._reviews = reviews
        else:
            self._reviews = None

    @property
    def time_spent_watching_movies_minutes(self):
        return self._time_spent_watching_movies_minutes

    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self, time_spent_watching_movies_minutes):
        if type(time_spent_watching_movies_minutes) == int and time_spent_watching_movies_minutes >= 0:
            self._time_spent_watching_movies_minutes = time_spent_watching_movies_minutes
        else:
            self._time_spent_watching_movies_minutes = 0

    def __repr__(self) -> str:
        return f'<User {self._user_name}>'

    def __eq__(self, other) -> bool:
        if not isinstance(other, User):
            return False
        return other._user_name == self._user_name

    def __lt__(self, other):
        return self._user_name < other._user_name

    def __hash__(self):
        return hash(self._user_name)

    def watch_movie(self, movie):
        if type(movie) is Movie:
            if movie not in self._watched_movies:

                self._watched_movies.append(movie)
                self._time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if type(review) is Review:
            if review not in self._reviews:
                self._reviews.append(review)


class WatchList:
    def __init__(self, watchlist = []):
        self.i = 0
        if type(watchlist) == list:
            self._watchlist = watchlist

    @property
    def watchlist(self):
        return self._watchlist

    def add_movie(self, movie):
        if type(movie) == Movie:
            if movie not in self._watchlist:
                self._watchlist.append(movie)

    def remove_movie(self, movie):
        if type(movie) == Movie:
            if movie in self._watchlist:
                self._watchlist.remove(movie)

    def size(self):
        return len(self._watchlist)

    def first_movie_in_watchlist(self):
        if len(self._watchlist) == 0:
            return None
        else:
            return self._watchlist[0]

    def select_movie_to_watch(self, index):
        if len(self._watchlist) >= index:
            return self._watchlist[index]
        else:
            return None

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self._watchlist):
            raise StopIteration
        else:
            item_required=self._watchlist[self.i]
            self.i += 1
            return item_required






