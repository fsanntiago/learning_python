# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite
# numbers. Think of five names, and use them as keys in your
# dictionary. Think of a favorite number for each person, and store
# each as a value in your dictionary. Print each person’s name and
# their favorite number. For even more fun, poll a few friends and get
# some actual data for your program.
favorite_numbers = {
    'maria': 12,
    'peter': 7,
    'gabriel': 52,
    'kelly': 71,
    'tiago': 21,
    }

for key in favorite_numbers:
    print(f"{key.title()}'s favorite number is {favorite_numbers[key]}.")