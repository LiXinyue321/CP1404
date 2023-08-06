"""
CP1404 - Practical 4
list_exercises
code that checks username validity and categories number inputs
"""

# 1. Security Checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter username:")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")

# 2. Numbers
numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average of the numbers is", sum(numbers) / len(numbers))
