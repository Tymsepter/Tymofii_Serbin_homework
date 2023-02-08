# Write a program that takes your name as input, and then your age as input and greets you with the following:

# “Hello <name>, on your next birthday you’ll be <age+1> years”

name = input("What is your name?:")
age = input("How old are you?:")
age = int(age) + 1
print(f"Hello,  {name}  on your next birthday you’ll be   {age}  years")
