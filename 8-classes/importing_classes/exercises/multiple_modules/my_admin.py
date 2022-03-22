""" 9-12. Multiple Modules: Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly. """

from admin import Admin

peter = Admin("peter", "rose", "peter_rose", "peter@gmail.com", "Chile")
peter.describe_user()

peter_privileges = [
    "can reset passwords",
    "can moderate discussions",
    "can suspend accounts",
]
peter.privileges.privileges = peter_privileges

print(f"\nThe admin {peter.username} has these privileges: ")
peter.privileges.show_privileges()
