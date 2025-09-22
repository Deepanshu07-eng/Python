class employee:
    language = "Python" # This is a class attribute
    salary = "1000000"

Deepanshu = employee()
Deepanshu.name = "Deepanshu" # this is an Instance attribute.
print(Deepanshu.name, Deepanshu.language, Deepanshu.salary)

Rahul = employee()
print(Rahul.language, Rahul.salary)

'''
OBJECT : An object is an instantiation of a class. When class is defined,
        a template (info) is defined. Memory is allocated after object intantation.

'''
'''
Modelling a problem in OOPS

we identify the following in our problem.

* Noun -> Class -> Employee
* Adjectives -> Attributes -> name, age, salary
* Verbs -> Methods -> getSalary(), increment()

'''

# Here name is object attribute and salary and language and class
# attributes as they directly belong to the class.

