from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def speed(self):
        pass

class Car(Vehicle):
    def speed(self):
        print("Car speed is 120 km/h")

c = Car()
c.speed()
