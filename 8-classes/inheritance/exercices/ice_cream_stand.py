""" 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method. """


from typing import List


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


class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    flavors: List[str] = []

    def __init__(self, name: str, cuisine_type: str = "ice cream"):
        """Initialize an ice cream stand."""
        super().__init__(name, cuisine_type)

    def show_flavors(self):
        """Display the flavors available."""
        if not self.flavors:
            print("\nThere aren't flavors available.")
            return

        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"  -{flavor.title()}")

    def add_flavors(self, *flavors):
        """Add new flavors."""
        if not flavors:
            print("\nDon't have any to add")
            return

        print("\nAdding Flavors:")
        for flavor in flavors:
            current_flavor = flavor
            if current_flavor not in self.flavors:
                print(f"Add {current_flavor}...")
                self.flavors.append(current_flavor)


ice_house = IceCreamStand("The Ice House")

ice_house.show_flavors()

flavors = ["vanilla", "chocolate", "neapolitan", "strawberry"]
ice_house.add_flavors(*flavors)
ice_house.show_flavors()
