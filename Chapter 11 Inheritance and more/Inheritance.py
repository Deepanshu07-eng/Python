# Inheritance is a way of creating a new class from an existing class.

class employee:
    company = "infosys"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary} ")
    
'''
class programmer:
    company = "Microsoft"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary} ")

    def showlanguage(self):
        print(f"The name of programmer is {self.name} and {self.name} is good in {self.language} language")
'''

class programmer(employee):
    company = "microsoft"
    def showLanguage(self):
        print(f"The name of programmer is {self.name} and {self.name} is good in {self.language} language")

a = employee()
b = programmer()

print(a.company, b.company)


# Types of Inheritance
#   1.Single Inheritance
#   2.Multiple inheritance
#   3.Multilevel inheritance