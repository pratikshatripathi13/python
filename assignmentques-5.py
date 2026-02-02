class Company:
    def __init__(self, company_name):
        self.company_name = company_name

    def show_company(self):
        print("Company:", self.company_name)


class Programmer(Company):
    def code(self):
        print("Writing code")


class Tester(Company):
    def test(self):
        print("Testing software")


class SoftwareEngineer(Programmer, Tester):
    def develop(self):
        self.show_company()
        self.code()
        self.test()


se = SoftwareEngineer("TechCorp")
se.develop()
