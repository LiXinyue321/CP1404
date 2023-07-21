"""
CP1404 - Practical 2
password_stars
Ask user for password then print password length in *'s
"""


def main():
    min_length = 6
    password = get_password(min_length)
    print("*" * len(password))


def get_password(min_length):

    password = input("Enter password: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long")
        password = input("Enter password: ")
    return password


main()