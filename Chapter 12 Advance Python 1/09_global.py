
a = 32    #Global variable

def fun():
    global a
    a =3    #local variable
    print(a)

fun()
print(a)


