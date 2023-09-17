from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")

    menu_choice = input("(q)uit, (c)hoose taxi, (d)rive\n>>> ").upper()
    while menu_choice != "Q":
        print("Taxis available:")
        if menu_choice == "C":
            i = 0
            for taxi in enumerate(taxis):
                i += 1



main()
