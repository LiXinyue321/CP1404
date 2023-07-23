"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random


def main():
    """Program get score and display its status"""
    score = float(input("Enter score: "))
    print(determine_status(score))
    random_score = random.randint(1, 100)
    print(determine_status(random_score))


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