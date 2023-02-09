# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except statment to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?


def oops():
    raise IndexError("IndexError occurred ")


def catch_error():
    try:
        oops()
    except IndexError as error:
        print("Caught IndexError:", error)


catch_error()
