def outer_function():
    message = "Hello Gendalph! "

    def inner_function():
        print(message + "How are you?")

    return inner_function


my_func = outer_function()
my_func()
