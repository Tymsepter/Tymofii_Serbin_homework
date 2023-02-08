import random
# Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.
a = random.randrange(10)
b = input("guess the number from 1 - 10:")
if a == int(b):
    print("You guessed it! It`s :", a)
elif a != b:
    print("You guessed wrong =( it`s :", a)
