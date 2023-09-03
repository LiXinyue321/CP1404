"""
CP1404/CP5632 Practical
Guitar class
"""

VINTAGE_AGE = 50
CURRENT_YEAR = 2023


class Guitar:
    """"Represent a guitar object"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a guitar"""
        return f"{self.name} ({self.year}) : {self.cost}"

    def __lt__(self, other):
        """Less than, used for sorting guitars by year"""
        return self.year < other.year

    def get_age(self):
        """Get the age of the guitar based on current year"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a guitar vintage or not"""
        return self.get_age() > VINTAGE_AGE

