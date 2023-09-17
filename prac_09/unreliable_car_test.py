from unreliable_car import UnreliableCar


def main():
    broken_car = UnreliableCar("Broken car", 100, 20)
    broken_car.drive(40)
    print(broken_car)


main()
