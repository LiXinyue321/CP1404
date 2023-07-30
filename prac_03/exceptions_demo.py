"""
CP1404 - Practical 3
exceptions_demo
Demonstrates exceptions using a fraction calculator
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    while denominator == 0:
        print("Denominator must not be 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# QUESTIONS
# 1. When will a ValueError occur?
# This error occurs when the users input is not a number and cannot produce an integer (For example: denominator="Fish")

# 2. When will a ZeroDivisionError occur?
# This occurs when the denominator=0