"""
CP1404 - Practical 3
files
Reads code from .txt files
"""

# Code to ask the user for their name, then opens a file called "name.txt" and writes that name to it
name = input("Name: ")
with open("names.txt", "w") as name_file:
    print(name, file=name_file)

# Code to open "name.txt" and read the name then print, "Your name is:(name)"
with open("names.txt", "r") as name_file:
    name = name_file.read().strip()
print(f"Your name is {name}")

# Code to open "numbers.txt", reads only the first two numbers and adds them together then print the result (59)
with open("numbers.txt", "r") as numbers_file:
    lines = numbers_file.readlines()
result = int(lines[0]) + int(lines[1])
print(f"Sum of first two numbers: {result:,}")

# Code to open "numbers.txt", read all three numbers and adds them together then print the result (459)
with open("numbers.txt", "r") as numbers_file:
    total = 0
    for line in numbers_file:
        total += int(line.strip())
print(f"Sum of all numbers: {total:,}")