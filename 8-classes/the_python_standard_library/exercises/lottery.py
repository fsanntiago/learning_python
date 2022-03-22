""" 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and
five letters. Randomly select four numbers or letters from the list and print a
message saying that any ticket matching these four numbers or letters wins a
prize. """

from random import choice
from typing import Any, List

possibilities = [10, 2, 39, 40, 12, 49, 73, 94, 41, 21, "k", "d", "a", "f", "i"]
winning_ticket: List[Any] = []

print("Let's see what the winning ticket is...")

# We don't want to repeat winning numbers or letters
while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)

    # Only add the pulled item to the winning ticket if it hasn't already been pulled.
    if pulled_item not in winning_ticket:
        winning_ticket.append(pulled_item)
print(winning_ticket)
