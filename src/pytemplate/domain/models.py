from dataclasses import dataclass


@dataclass
class Movie:
    name: str
    customer_age: int


def movie_factory(name: str, customer_age: int) -> Movie:
    return Movie(name, customer_age)
