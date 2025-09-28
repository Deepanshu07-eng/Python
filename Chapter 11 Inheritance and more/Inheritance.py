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

'''
1 SINGLE INHERITANCE
-> single inheritance occurs while child class inherits only a single parent class.
    
    Base -> Derived

2 MULTIPLE INHERITANCE
->  Multiple inheritance occurs when the child class inherits from more than one parent class.

    Parent 1
                 ->    Child
    Parent 2
    
3 MULTILEVEL INHERITANCE
-> 
'''