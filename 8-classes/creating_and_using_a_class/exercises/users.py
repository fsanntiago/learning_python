""" 9-3. Users: Make a class called User . Create two attributes called first_name
and last_name , and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.

Create several instances representing different users, and call both methods
for each user. """


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


fsantiago = User("fabricio", "santiago", "fsantiago", "fabricio@gmail.com", "brazil")
fsantiago.describe_user()


m_ferreira = User("maria", "ferreira", "m_ferreira", "maria@gmail.com", "chile")
m_ferreira.describe_user()
