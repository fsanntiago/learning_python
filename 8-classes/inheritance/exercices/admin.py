""" 9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method. """


from typing import List


class User:
    "Represent a simple user profile."
    _total_user = 0

    def __init__(
        self, first_name: str, last_name: str, username: str, email: str, location: str
    ):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user"""
        print(f"Welcome back, {self.username}")


class Admin(User):
    """A user with administrative privileges."""

    def __init__(
        self, first_name: str, last_name: str, username: str, email: str, location: str
    ):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges: List[str] = []

    def show_privileges(self):
        """Display the privileges this administrator has."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"{privilege}")


fabricio = Admin("fabricio", "santiago", "fsantiago", "fabricios@gmail.com", "brazil")
fabricio.describe_user()

fabricio.privileges = [
    "can reset passwords",
    "can moderate discussions",
    "can suspend accounts",
]

fabricio.show_privileges()
