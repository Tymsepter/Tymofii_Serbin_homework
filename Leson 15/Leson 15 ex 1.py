class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello {self.firstname} {self.lastname} and I`m {self.age} years old")


a = Person("Carl", "Johnson", "26")

a.talk()
