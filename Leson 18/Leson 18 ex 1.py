import re


def validate_email(func):
    def wrapper(self, name, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Incorrect email address")
        return func(self, name, email)

    return wrapper


class User:
    @validate_email
    def __init__(self, name, email):
        self.name = name
        self.email = email


try:
    user1 = User("Fadi Ahmad", "fadiahmad@mail.com")
    print("User created:", user1.name, user1.email)
except ValueError as e:
    print("Error creating user:", str(e))

try:
    user2 = User("Tymofii Serbin", "tymofiiserbin.com")
    print("User created:", user2.name, user2.email)
except ValueError as e:
    print("Error, user not created:", str(e))

try:
    user3 = User("Garold", "garold@mail")
    print("User created:", user3.name, user3.email)
except ValueError as e:
    print("Error, user not created:", str(e))
