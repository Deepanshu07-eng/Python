# Function jo apne aap ko hi call krta hai

'''
Factorial of 5 = 5 x 4 x 3 x 2 x 1

factorial of 0 = 1

factorial (n) = n x n-1 x n-1 x .... 3 x 2 x 1

factorial of(n) = n*factorial(n-1)

'''

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)

n = int(input("Enter a number:"))
print(f"The factorial of {n} is :{factorial(n)}")
