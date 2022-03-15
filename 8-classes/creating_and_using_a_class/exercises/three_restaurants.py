""" 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance. """


class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, restaurant_name: str, cuisine_type: str):
        """Initialize the restaurant.

        Args:
            restaurant_name (str): Restaurant name.
            cuisine_type (str): Restaurant cuisine type.
        """
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.restaurant_name} serves wonderful {self.cuisine_type}"
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        print(f"\n{self.restaurant_name} is open.")


esconderijo_bar = Restaurant("esconderijo bar", "brazilian food")
esconderijo_bar.describe_restaurant()

burger_house = Restaurant("burger house", "ameriacan food")
burger_house.describe_restaurant()

mangiare = Restaurant("mangiare", "italian food")
mangiare.describe_restaurant()
