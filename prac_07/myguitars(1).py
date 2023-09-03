"""
CP1404/CP5632 Practical
Program to read guitars.csv file and display guitars
"""

from guitar import Guitar


def main():
    """Read and display all guitars from guitars.csv"""
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    print("These are my guitars:")
    display_guitars(guitars)

    guitars.sort()
    print("These are my guitars sorted by year:")
    display_guitars(guitars)

    add_guitar(guitars)

    write_guitars_to_file(guitars)


def write_guitars_to_file(guitars):
    """Write guitars to guitars.csv"""
    out_file = open('guitars.csv', 'w')
    for guitar in guitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    out_file.close()


def add_guitar(guitars):
    """Add new guitar to the list"""
    print("Please add new guitars (Stop when the name gets a blank enter):")
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = input("Year: ")
        cost = input("Cost: $")
        guitar = Guitar(name, int(year), float(cost))
        guitars.append(guitar)
        print("New guitar added. Here are all the guitars:")
        display_guitars(guitars)


def display_guitars(guitars):
    """Display all the guitars"""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar.name:>30} ({guitar.year}), worth ${guitar.cost:10,.2f}")


main()
