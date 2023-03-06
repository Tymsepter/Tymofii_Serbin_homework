class Person:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.surname = surname

    def __repr__(self):
        return f"{self.name}, {self.surname}, {self.age}, {self.gender}"


class Student(Person):
    def __init__(self, name, surname, age, gender, scholarship):
        super().__init__(name, surname, age, gender)
        self.scholarship = scholarship

    def __repr__(self):
        return f"{self.name}, {self.surname}, {self.age}, {self.gender}, {self.scholarship}"


class Teacher(Person):
    def __init__(self, name, surname, age, gender, salary):
        super().__init__(name, surname, age, gender)
        self.salary = salary

    def __repr__(self):
        return f"{self.name}, {self.surname}, {self.age}, {self.gender}, {self.salary}"


teacher = Teacher("Fadi", "Ahmad", 26, "male", "1000$")
student = Student("Tymofii", "Serbin", 20, "male", "50$")

print(repr(teacher))
print(repr(student))
