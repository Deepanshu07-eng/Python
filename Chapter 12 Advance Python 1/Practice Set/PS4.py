'''
Write a program to display a/b where a and b are integer, if b=0, display infinite by handling the 'zeroDivisionError'.
'''

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a/b)

except ZeroDivisionError as v:
    print("Infinite")