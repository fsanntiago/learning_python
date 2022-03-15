""" 9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 162). Write a method called increment_login
_attempts() that increments the value of login_attempts by 1. Write another
method called reset_login_attempts() that resets the value of login_attempts
to 0.

Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts() . Print login_attempts again to
make sure it was reset to 0. """


class User:
    "Represent a simple user profile."

    def __init__(
        self, first_name: str, last_name: str, username: str, email: str, location: str
    ):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user"""
        print(f"Welcome back, {self.username}")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_atempts to 0."""
        self.login_attempts = 0


fsantiago = User("fabricio", "santiago", "fsantiago", "fabricio@gmail.com", "brazil")
fsantiago.describe_user()
fsantiago.greet_user()

print("\nMaking 3 login attempts...")
fsantiago.increment_login_attempts()
fsantiago.increment_login_attempts()
fsantiago.increment_login_attempts()
print(f" - Login attempts: {fsantiago.login_attempts}")

print("Resetting login attempts...")
fsantiago.reset_login_attempts()
print(f" - Login attempts: {fsantiago.login_attempts}")
