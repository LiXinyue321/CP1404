"""
CP1404/CP5632 Practical
SilverServiceTaxi class tests
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test some silver service taxis"""
    silver_service_taxi = SilverServiceTaxi("Hummer", 200, 4)
    silver_service_taxi.drive(18)
    print(silver_service_taxi)
    print(silver_service_taxi.get_fare())

    silver_service_taxi = SilverServiceTaxi("FancyCar", 300, 3)
    silver_service_taxi.drive(20)
    print(silver_service_taxi)
    print(silver_service_taxi.get_fare())

main()
