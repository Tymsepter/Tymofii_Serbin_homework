# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers)
# as the second parameter.
# Then return the sum or product of all the numbers in the arbitrary parameter.

def make_operation(*args):
    return_value = 0
    for num in args:
        return_value += num
    return return_value


print(make_operation(5, 10, 49, 75, 62))
