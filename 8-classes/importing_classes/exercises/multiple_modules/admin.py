"""A collection of classes for modeling an admin user account."""

from typing import List

from user import User


class Admin(User):
    """A user with administrative privileges."""

    def __init__(
        self, first_name: str, last_name: str, username: str, email: str, location: str
    ):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges()


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
