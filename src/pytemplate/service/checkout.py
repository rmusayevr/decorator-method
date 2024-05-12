from pytemplate.domain.models import Movie
from src.pytemplate.utils.decorator import age_limit_6plus_method, age_limit_13plus_method, age_limit_18plus_method


@age_limit_6plus_method
def buy_ticket_for_children(movie: Movie) -> str:
    return f"You are allowed to watch {movie.name}."


@age_limit_13plus_method
def buy_ticket_for_teens(movie: Movie) -> str:
    return f"You are allowed to watch {movie.name}."


@age_limit_18plus_method
def buy_ticket_for_adults(movie: Movie) -> str:
    return f"You are allowed to watch {movie.name}."
