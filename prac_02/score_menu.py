"""
CP1404 - Practical 2
score_menu
Menu to provide the user a list of options based on an inputted score
"""
MENU = """
(1) - Get Score
(2) - Print Result
(3) - Print Stars
(4) - Quit
"""
MIN_SCORE = 0
MAX_SCORE = 100


def main():
    score = "empty"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "4":
        if choice == "1":
            score = score_input()
        elif choice == "2":
            checkscore(score)
        elif choice == "3":
            print_stars(score)
        print(MENU)
        choice = input(">>> ").upper()


def print_stars(score):
    if score == "empty":
        print("No score, Please press 3")
    else:
        for i in range(score):
            print("*", end='',)


def score_input():
    score = int(input("Enter score: "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def checkscore(score):
    if score == "empty":
        print("No score, press 1")
    else:
        if score < 0 or score > 100:
            print("Invalid score")
        elif score >= 50:
            print("Passable")
        elif score >= 90:
            print("Excellent")
        else:
            print("Bad")


main()