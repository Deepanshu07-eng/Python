class employee:
    language = "Python" # This is a class attribute
    salary = "1000000"


    def __init__(self, name, salary, language): # __(underscore) se start hone wale methods ko ( Dunder ) method kehte hai. which is automatically called.
        self.name = name
        self.salary = salary
        self.language = language
        
        print("I am creating an object")


    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod   # if you dont want to add self then you have to write @staticmethod. 
    def greet():
        print("Good morning")


Deepanshu = employee("Deepanshu", 1300000, "C++")
# Deepanshu.name = "Deepanshu" # this is an Instance attribute.

print(Deepanshu.name, Deepanshu.salary, Deepanshu.language)
 