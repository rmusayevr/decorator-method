from io import StringIO
from unittest.mock import patch

from pytemplate.entrypoints.cli.main import main
from src.pytemplate.domain.models import Movie, movie_factory
from src.pytemplate.utils.decorator import age_limit_6plus_method, age_limit_13plus_method, age_limit_18plus_method


def test_init_movie():
    movie = Movie("The Matrix", 15)
    assert movie.name == "The Matrix"
    assert movie.customer_age == 15


def test_movie_factory():
    name, customer_age = "Dune: Part Two", 21
    movie = movie_factory(name, customer_age)
    assert isinstance(movie, Movie)
    assert movie.name == name
    assert movie.customer_age == customer_age


def test_allowed_6plus_decorator():
    @age_limit_6plus_method
    def check_age_limit(movie: Movie):
        return f"You are allowed to watch {movie.name}."

    movie = Movie("Frozen", 9)
    assert check_age_limit(movie) == "You are allowed to watch Frozen."


def test_not_allowed_6plus_decorator():
    @age_limit_6plus_method
    def check_age_limit(movie: Movie):
        return f"You are allowed to watch {movie.name}."

    movie = Movie("Frozen", 4)
    assert check_age_limit(movie) == "Sorry, you are not old enough to watch Frozen."


def test_allowed_13plus_decorator():
    @age_limit_13plus_method
    def check_age_limit(movie: Movie):
        return f"You are allowed to watch {movie.name}."

    movie = Movie("Lady Bird", 15)
    assert check_age_limit(movie) == "You are allowed to watch Lady Bird."


def test_not_allowed_13plus_decorator():
    @age_limit_13plus_method
    def check_age_limit(movie: Movie):
        return f"You are allowed to watch {movie.name}."

    movie = Movie("Lady Bird", 10)
    assert check_age_limit(movie) == "Sorry, you are not old enough to watch Lady Bird."


def test_allowed_18plus_decorator():
    @age_limit_18plus_method
    def check_age_limit(movie: Movie):
        return f"You are allowed to watch {movie.name}."

    movie = Movie("Interstellar", 21)
    assert check_age_limit(movie) == "You are allowed to watch Interstellar."


def test_not_allowed_18plus_decorator():
    @age_limit_18plus_method
    def check_age_limit(movie: Movie):
        return f"You are allowed to watch {movie.name}."

    movie = Movie("Interstellar", 15)
    assert check_age_limit(movie) == "Sorry, you are not old enough to watch Interstellar."


@patch("builtins.input", side_effect=["Ponyo", 8, 6])
def test_main_allowed_6plus(mock_input):
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        main()
        assert mock_stdout.getvalue().strip() == "You are allowed to watch Ponyo."


@patch("builtins.input", side_effect=["Ponyo", 4, 6])
def test_main_not_allowed_6plus(mock_input):
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        main()
        assert mock_stdout.getvalue().strip() == "Sorry, you are not old enough to watch Ponyo."


@patch("builtins.input", side_effect=["Monster", 14, 13])
def test_main_allowed_13plus(mock_input):
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        main()
        assert mock_stdout.getvalue().strip() == "You are allowed to watch Monster."


@patch("builtins.input", side_effect=["Monster", 12, 13])
def test_main_not_allowed_13plus(mock_input):
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        main()
        assert mock_stdout.getvalue().strip() == "Sorry, you are not old enough to watch Monster."


@patch("builtins.input", side_effect=["The Hunt", 21, 18])
def test_main_allowed_18plus(mock_input):
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        main()
        assert mock_stdout.getvalue().strip() == "You are allowed to watch The Hunt."


@patch("builtins.input", side_effect=["The Hunt", 15, 18])
def test_main_not_allowed_18plus(mock_input):
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        main()
        assert mock_stdout.getvalue().strip() == "Sorry, you are not old enough to watch The Hunt."


@patch("builtins.input", side_effect=["The Hunt", 21, 0])
def test_main_invalid_action(mock_input):
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        main()
        assert mock_stdout.getvalue().strip() == "Invalid action! Please choose 6/13/18."
