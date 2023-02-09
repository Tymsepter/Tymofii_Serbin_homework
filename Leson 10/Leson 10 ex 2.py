# Write a function that takes in two numbers from the user via input(),
# call the numbers a and b, and then returns the value of squared a divided by b,
# construct a try-except block which raises an exception if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).


def divide_and_square():
    try:
        a = float(input("Enter a number: "))
        b = float(input("Enter another number: "))
        result = a**2 / b
        print(result)
        return result
    except (ValueError, ZeroDivisionError):
        print("Both values must be numbers and b can't be zero.")


divide_and_square()
