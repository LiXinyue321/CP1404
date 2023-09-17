"""
CP1404/CP5632 Practical
Taxi simulator
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator program"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        user_choice = input(">>> ").lower()

        if user_choice == "q":
            print(f"Total trip cost: ${total_bill:.2f}")
            print("Taxis are now:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            break
        elif user_choice == "c":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")

            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
            except (ValueError, IndexError):
                print("Invalid taxi choice")
        elif user_choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
                continue

            distance_to_drive = float(input("Drive how far? "))
            current_taxi.drive(distance_to_drive)
            trip_cost = current_taxi.get_fare()
            print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
            total_bill += trip_cost
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")


main()