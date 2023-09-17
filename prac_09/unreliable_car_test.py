"""
CP1404 Practical
UnreliableCar class tests
"""

from unreliable_car import UnreliableCar


def main():
    """Test some cars with different reliability"""

    broken_car = UnreliableCar("Unreliable", 100, 10)
    good_car = UnreliableCar("Perfect", 100, 100)
    print(broken_car)
    print(good_car)

    # Try to drive 40 km
    distance = broken_car.drive(40)
    print(f"Drove {distance} km.")
    distance = good_car.drive(40)
    print(f"Drove {distance} km.")

    # Try to drive another 50 km
    distance = broken_car.drive(50)
    print(f"Drove {distance} km.")
    distance = good_car.drive(40)
    print(f"Drove {distance} km.")

    print(broken_car)
    print(good_car)

main()
