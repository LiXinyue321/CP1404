"""
CP1404/CP5632 - Practical
Program can let user get valid score, determine the score's status and print stars
"""

import random


MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should  as many stars as the score)
(Q)uit"""


def main():
    """Program to determine status of random valid score and print stars"""
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = random.randint(1, 100)
            print(f"The valid score: {score}")
        elif choice == "P":
            print(determine_status(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("invalid option")
        print(MENU)
        choice = input(">>>").upper()
    print("Thanks for your use")


def print_stars(score):
    """Print as many stars as score"""
    for i in range(score):
        print("*", end="")
    print()


def determine_status(score):
    """Determine score status"""
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
