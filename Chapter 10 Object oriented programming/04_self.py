class employee:
    language = "Python" # This is a class attribute
    salary = "1000000"

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod   # if you dont want to add self then you have to write @staticmethod. 
    def greet():
        print("Good morning")


Deepanshu = employee()
Deepanshu.language = "C++" # this is an Instance attribute.

Deepanshu.greet()
Deepanshu.getInfo() 
# employee.getInfo(harry)
