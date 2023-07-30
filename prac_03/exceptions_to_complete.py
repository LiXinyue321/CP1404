"""
CP1404 - Practical 3
exceptions_to_complete
Program that gets an integer from the user and does not crash when a non-number is entered
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)