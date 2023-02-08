# Write a Python program to get the largest number from a list of random numbers with the length of 10

# Constraints: use only while loop and random module to generate numbers

import random

list_1 = []
while len(list_1) < 10:
    a = random.randrange(1, 100)
    list_1.append(a)
print(list_1)
min_numb = min(list_1)
print(min_numb)
