""" 9-13. Dice: Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll it
10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times. """


from random import randint


class Die:
    """Represent a die, which can be rolled."""

    def __init__(self, sides: int = 6) -> None:
        """Initialize the die."""
        self.sides = sides

    def roll_die(self) -> int:
        """Return a number between 1 and the number of sides."""
        return randint(1, self.sides)


# Make a 6 - sided die, and show the results of 10 rolls
d6 = Die()

results = [d6.roll_die() for roll_num in range(10)]
print("10 rolls of a 6-sided die:")
print(results)

# Make a 10 - sided die, and show the results of 10 rolls
d10 = Die(10)

results = [d10.roll_die() for roll_num in range(10)]
print("\n10 rolls of a 10-sided die:")
print(results)

# Make a 20 - sided die, and show the results of 10 rolls
d20 = Die(20)

results = [d20.roll_die() for roll_num in range(10)]
print("\n10 rolls of a 20-sided die:")
print(results)
