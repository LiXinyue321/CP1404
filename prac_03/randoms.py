"""
CP1404 - Practical 3
randoms
program to produce random values
"""

import random

print(random.randint(5, 20))  # line 1, the maximum is 20.
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# Question 1: Smallest:5 Largest:19 I saw a 9
# Question 2: Smallest:3 Largest:9,I saw a 9, No it could not produce a 4
# Question 3: I saw a float number (3.858242212661559),Smallest:2.5 Largest is 5.49..


random_number = random.randrange(1, 101)