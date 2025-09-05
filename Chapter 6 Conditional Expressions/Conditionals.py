# In python programming, we must be able to execute instructions on a condition(s) being met.

#This is what conditions are for :-

# IF, ELSE and ELIF in PYTHON

a = int(input("Enter your Age: "))

# IF - ELSE Ladder

if(a>18):
    print("You are Eligible for voting")
    print("Good for you and for Congress party haha lol")  
else:
    print("You are not Eligible for voting")


# IF -ELSE -ELSE ladder


if(a>18):
    print("You are Eligible for voting")
    print("Good for you and for Congress party haha lol")
elif(a<0):
    print("Go to your mumma's belly or fathers ball's back! Its your choice lol!")
else:
    print("You are not Eligible for voting")