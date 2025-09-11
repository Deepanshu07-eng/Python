"""
FUNCTIONS: A function is a group of statements performing a specific task.

"""
'''
a = int(input("Enter the number"))
b = int(input("Enter the number"))
c = int(input("Enter the number"))

average = (a + b + c)/3
print(average)

a = int(input("Enter the number"))
b = int(input("Enter the number"))
c = int(input("Enter the number"))

average = (a + b + c)/3
print(average)

'''
#Dont do like this, Do it with Function.

#Function Defination
def avg():
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    c = int(input("Enter the number: "))

    average = (a + b + c)/3
    print(average)

#Function call
avg()
avg()
avg()
avg() #this run 4 times

''' TWO TYPES OF FUNCTION '''
# 1 Built in Function. ( Already present in function )
# 2 User Defined Function. ( Defined by the user )