"""A collection of classes for modeling users."""

from typing import List


class User:
    """Represent a simple user profile."""

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
