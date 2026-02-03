from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass

class Developer(Employee):
    def salary(self):
        print("Developer salary is 8 LPA")

e = Developer()
e.salary()
