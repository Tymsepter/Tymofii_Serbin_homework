def logger(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} called with {args}, {kwargs}")
        return func(*args, **kwargs)

    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(5, 2)
square_all(2, 5, 78, 9)
