from functools import wraps

from pytemplate.domain.models import Movie


def age_limit_6plus_method(func):
    @wraps(func)
    def wrapper(movie: Movie):
        if movie.customer_age >= 6:
            return func(movie)
        else:
            return f"Sorry, you are not old enough to watch {movie.name}."

    return wrapper


def age_limit_13plus_method(func):
    @wraps(func)
    def wrapper(movie: Movie):
        if movie.customer_age >= 13:
            return func(movie)
        else:
            return f"Sorry, you are not old enough to watch {movie.name}."

    return wrapper


def age_limit_18plus_method(func):
    @wraps(func)
    def wrapper(movie):
        if movie.customer_age >= 18:
            return func(movie)
        else:
            return f"Sorry, you are not old enough to watch {movie.name}."

    return wrapper
