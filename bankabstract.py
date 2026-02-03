from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def interest_rate(self):
        pass

class SBI(Bank):
    def interest_rate(self):
        print("SBI interest rate is 6%")

b = SBI()
b.interest_rate()
