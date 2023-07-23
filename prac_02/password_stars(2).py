"""
CP1404 - Practical
This program check user input valid length password and print asterisks
"""

MINIMUM_LENGTH = 6


def main():
    """Get password and print asterisks using functions"""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    """Get password from user and ensure it has minimum length"""
    password = input(f"Please enter password at least {minimum_length}: ")
    while len(password) < minimum_length:
        password = input(f"Please enter password at least {minimum_length}: ")
    return password


def print_asterisks(password):
    """Print asterisks as many as the characters of the password"""
    print("*" * len(password))


main()