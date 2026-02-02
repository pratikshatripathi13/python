# 1. Create a base class University. Derive Student and Teacher from it. 
#    Then create TeachingAssistant that inherits from both Student and Teacher 
#    and implements methods for studying, teaching, and assisting.
class university:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("name",self.name)
class student(university):
    def __init__(self,name, regno):
        self.regno=regno
        university.__init___(self, name)
    def showregno(self):
        print("regno",self.regno)
class teacher(university):
    def __init__(self, name,teachid):
        university.__init__(self, name)
        self.teachid=teachid
    def showteacher(self):
        print("teacher id is:",self.teachid)
    

c=teacher("lpu",12345)
c.showteacher()
c.show()
