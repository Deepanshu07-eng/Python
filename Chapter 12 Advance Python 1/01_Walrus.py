'''
Newly Added Feature in PYTHON

1. Walrus Operator
The walrus operator (:=), introduced in python 3.8, allows you to assign values to variable as part of an expression. this operator, named for its
resemblance to the eyes and tusks of a walrus, is officially called the "Assignment Expression".

'''

#Using walvus operator

if (n := len([1,2,3,4,5])) > 3:
    print(f"List is too long ({n} elements, exprected <=3)") 

#Output: list is too long (5 elements, expected <= 3)