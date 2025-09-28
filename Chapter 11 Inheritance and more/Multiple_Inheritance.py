class employee:
    company = "infosys"
    name = "Deepanshu"
    salary = 1200000
    def show(self):
        print(f"The name of the employee is {self.name} working in {self.company} and the salary is {self.salary} ")
    
class coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the language here is your language: {self.language}")


class programmer(employee, coder):
    company = "microsoft"
    def showLanguage(self):
        print(f"The name of programmer is {self.name} and {self.name} is good in {self.language} language and the comapany name is {self.company}")

a = employee()
b = programmer()

b.show()
b.showLanguage()
b.printLanguage()