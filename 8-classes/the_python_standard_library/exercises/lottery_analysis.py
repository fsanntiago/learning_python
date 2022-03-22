""" 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
the kind of lottery you just modeled. Make a list or tuple called my_ticket.
Write a loop that keeps pulling numbers until your ticket wins. Print a message
reporting how many times the loop had to run to give you a winning ticket. """

from random import choice
from typing import Any, List

Ticket = List[Any]


def get_winning_ticket(possibilities: List[Any]) -> Ticket:
    """Return a winning ticket from a set of possibilities."""
    winning_ticket: Ticket = []

    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)
    return winning_ticket


def check_ticket(played_ticket: Ticket, winning_ticket: Ticket) -> bool:
    """Check all elements in the played ticket.
    If any are not in the winning ticket, return False."""
    for item in played_ticket:
        if item not in winning_ticket:
            result = False
    return result


def make_random_ticket(possibilities: List[Any]) -> Ticket:
    """Return a random ticket from a set of possibilities."""
    ticket: Ticket = []

    while len(ticket) < 4:
        pulled_item = choice(possibilities)

        if pulled_item not in ticket:
            ticket.append(pulled_item)
    return ticket


possibilities = [10, 2, 39, 40, 12, 49, 73, 94, 41, 21, "k", "d", "a", "f", "i"]
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

# Let's set a max number of tries, in case this takes forever!
max_tries = 1_000_000


while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1

    if plays >= max_tries:
        break


if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
