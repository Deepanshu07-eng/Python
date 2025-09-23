class demo:
    a = 4


o = demo()

print(o.a) # it print class attribute because instance attribute is not present.

o.a = 0 # instance attrivute is set

print(o.a) # prints the instance attribute because instance attribute is present
