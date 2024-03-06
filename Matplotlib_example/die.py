from random import randint


class Die:
    """Class represents one die"""

    def __init__(self, num_sides=6):
        """By default, create a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random integer between 1 and num_sides."""
        return randint(1, self.num_sides)