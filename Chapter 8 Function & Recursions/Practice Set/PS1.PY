# Write a program using functions to find the gretest of three numbers.



def greatest(a,b,c):

    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
c = int(input("Enter number three: "))

print(greatest(a,b,c))