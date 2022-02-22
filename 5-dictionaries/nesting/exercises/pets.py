# Make several dictionaries, where each dictionary represents a
# different pet. In each dictionary, include the kind of animal and
# the owner’s name. Store these dictionaries in a list called pets.
# Next, loop through your list and as you do, print everything you know
# about each pet.

# Makes  empty list
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'dog',
    'name': 'jack',
    'owner': 'peter',
    'weight': 17,
    }
pets.append(pet)

pet = {
    'animal type': 'horse',
    'name': 'magic',
    'owner': 'john',
    'weight': 300,
    }
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'luna',
    'owner': 'helena',
    'weight': 4,
    }
pets.append(pet)

# Displays information about each pet
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"{key.title()}: {str(value).title()}")
