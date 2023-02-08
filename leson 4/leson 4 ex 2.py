# Make a program that checks if a string
# is in the right format for a phone number.
# The program should check that the string contains
# only numerical characters and is only 10 characters long.
# Print a suitable message depending on the outcome of the string evaluation.
import re

a = input("Print your phone number")
if re.search("[0-9]", a):
    print("")
else:
    print("In the number are written the letters")

if a[10:]:
    print("Incorrect number length")
elif a[9:]:
    print("Correсt nuber")
elif a[:8]:
    print("Incorrect number length")
