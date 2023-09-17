from car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):

        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if randint(1, 100) > self.reliability:
            distance = 0

        return super().drive(distance)
