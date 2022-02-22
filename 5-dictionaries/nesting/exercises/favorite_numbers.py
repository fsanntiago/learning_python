# 6-10. Favorite Numbers: Modify your program from Exercise 6-2
# (page 99) so each person can have more than one favorite number.
# Then print each person’s name along with their favorite numbers.

favorite_numbers = {
    'maria': [12, 65, 98, 20],
    'peter': [7],
    'gabriel': [52, 7],
    'kelly': [71, 84, 90],
    'tiago': [21, 45],
    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"- {number}")
