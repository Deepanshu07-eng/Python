# Formulae to convert celcious to fehrenheit 
'''
->"c = 5*(f-32)/9 "
'''


def f_to_c(f):
    return 5*(f-32)/9


f = int(input("Enter temperature in F: "))
sol = f_to_c(f)
print(f"{round(sol, 2)}°C")