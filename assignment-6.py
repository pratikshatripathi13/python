class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name

    def show_bank(self):
        print("Bank:", self.bank_name)


class SavingsAccount(Bank):
    def save(self):
        print("Managing savings account")


class LoanAccount(Bank):
    def loan(self):
        print("Managing loan account")


class Customer(SavingsAccount, LoanAccount):
    def manage(self):
        self.show_bank()
        self.save()
        self.loan()


c = Customer("State Bank")
c.manage()
