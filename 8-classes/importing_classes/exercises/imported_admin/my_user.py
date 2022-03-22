""" 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173).
Store the classes User, Privileges, and Admin in one module. Create a sepa-
rate file, make an Admin instance, and call show_privileges() to show that
everything is working correctly. """

from users import Admin

maria = Admin("maria", "rose", "maria_rose", "maria@gmail.com", "Chile")
maria.describe_user()

maria_privileges = [
    "can reset passwords",
    "can moderate discussions",
    "can suspend accounts",
]
maria.privileges.privileges = maria_privileges

print(f"\nThe admin {maria.username} has these privileges: ")
maria.privileges.show_privileges()
