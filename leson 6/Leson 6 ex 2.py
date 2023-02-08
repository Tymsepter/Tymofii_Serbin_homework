# Generate 2 lists with the length of 10 with random integers from 1 to 10
# and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

import random

list_1 = []
while len(list_1) < 10:
    a = random.randint(1, 10)
    list_1.append(a)

list_2 = []
while len(list_2) < 10:
    a = random.randint(1, 10)
    list_2.append(a)

a = list(set(list_1).intersection(list_2))

print(a)
