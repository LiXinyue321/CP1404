"""
CP1404 Practical
UnreliableCar class, it is derived form Car
"""

from car import Car
from random import randint


class UnreliableCar(Car):
    """Class represent an unreliable version of a car"""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car based on the reliability"""
        if randint(1, 100) > self.reliability:
            distance = 0
        else:
            distance = super().drive(distance)

        return distance
