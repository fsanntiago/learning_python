# 6-7. People: Start with the program you wrote for Exercise 6-1
# (page 99). Make two new dictionaries representing different people,
# and store all three dictionaries in a list called people. Loop
# through your list of people. As you loop through the list, print
# everything you know about each person.

# Make empty list to store people in
people = []

# Define some people, and store them to the list
person = {
    'first_name': 'fabricio',
    'last_name': 'santiago',
    'age': 21,
    'city': 'timoteo',
    }
people.append(person)

person = {
    'first_name': 'lena',
    'last_name': 'smith',
    'age': 18,
    'city': 'miami',
    }
people.append(person)

person = {
    'first_name': 'david',
    'last_name': 'wood',
    'age': 45,
    'city': 'boston',
    }
people.append(person)

# Display all of the information in the dictionary.
for person in people:
    name_full = f"{person['first_name']} {person['last_name']}"
    age = f"{person['age']}"
    city = f"{person['city']}"
    print(f"{name_full.title()} of {city.title()} is {age} years old.")
