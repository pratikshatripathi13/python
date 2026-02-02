class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)


class Dancer(Person):
    def dance(self):
        print(self.name, "is dancing")


class Singer(Person):
    def sing(self):
        print(self.name, "is singing")


class Performer(Dancer, Singer):
    def perform(self):
        self.show()
        self.dance()
        self.sing()


p = Performer("Amit")
p.perform()
