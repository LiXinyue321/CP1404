"""
CP1404 - Practical 4
quick_picks
code that asks the user how many "quick picks" they wish to generate. The program then generates that many lines of
output. Each line consists of 6 random numbers between 1 and 45.
"""

import random

NUMBERS_PER_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


def main():
    """Quick picks program that choose sets of random numbers"""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("number_of_quick_picks must be a positive integer!")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            while number in quick_pick:
                number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            quick_pick.append(number)
        quick_pick.sort()

        print(" ".join(f"{number:2}" for number in quick_pick))


main()