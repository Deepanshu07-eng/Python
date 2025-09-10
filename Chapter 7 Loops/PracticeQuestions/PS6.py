# 5! = 1 X 2 X 3 X 4 X 5 
'''
#Using While loop

n = int(input("Enter Number: "))

i =1
mul = 1

while(i<=n):
    mul *= i
    i += 1

print(mul)
'''
#Using For Loop

n= int(input("Enter Your number: "))

product =1
for i in range(1,n+1):
    product = product*i

print(f"The Factorial of {n} is {product}")

