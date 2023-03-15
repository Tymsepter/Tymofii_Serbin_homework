class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        return "Гав"


class Cat(Animal):
    def talk(self):
        return "Няв"


def animal_talk(animal):
    print(animal.talk())


dog = Dog()
cat = Cat()

animal_talk(dog)
animal_talk(cat)
