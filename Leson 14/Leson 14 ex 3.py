def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, type_):
                    print(f"Error: Argument {arg} is not of type {type_}.")
                    return False
                if len(arg) > max_length:
                    print(f"Error: Argument {arg} is too long (max {max_length} characters).")
                    return False
                if not all(symbol in arg for symbol in contains):
                    print(f"Error: Argument {arg} does not contain all required symbols {contains}.")
                    return False
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('jordan@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
