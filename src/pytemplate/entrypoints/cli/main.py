from src.pytemplate.domain.models import movie_factory
from src.pytemplate.service.checkout import Checkout


def main():
    name = input("Enter the name of the movie: ")
    customer_age = int(input("Enter your age: "))
    age_limit = int(input("Enter the age limit of the movie (6/13/18): "))

    checkout = Checkout()
    movie = movie_factory(name, customer_age)

    if age_limit == 6:
        result = checkout.buy_ticket_for_children(movie)
    elif age_limit == 13:
        result = checkout.buy_ticket_for_teens(movie)
    elif age_limit == 18:
        result = checkout.buy_ticket_for_adults(movie)
    else:
        print("Invalid action! Please choose 6/13/18.")
        return

    print(result)
