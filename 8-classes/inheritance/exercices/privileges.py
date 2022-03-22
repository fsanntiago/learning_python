""" 9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges. """

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


class Privileges:
    def __init__(self, privileges: List[str] = []) -> None:
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges this administrator has."""
        print("\nPrivileges:")
        if not self.privileges:
            print("- This user has no privileges.")
            return
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """A user with administrative privileges."""

    def __init__(
        self, first_name: str, last_name: str, username: str, email: str, location: str
    ):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges()


fabricio = Admin("fabricio", "santiago", "fsantiago", "fabricios@gmail.com", "brazil")
fabricio.describe_user()

fabricio.privileges.show_privileges()

print("\nAdding privileges...")
fabricio_privileges = [
    "can reset passwords",
    "can moderate discussions",
    "can suspend accounts",
]

fabricio.privileges.privileges = fabricio_privileges
fabricio.privileges.show_privileges()
