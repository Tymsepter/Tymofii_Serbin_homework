# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.

# If the string length is less than 2, return instead of the empty string.

a: str = input("print the sentence by 1;2 or 10 letters:")
if a > (a[0]):
    print((a[0:2]) + (a[-2]) + (a[-1]))
elif a == a[-1]:
    print("0")
