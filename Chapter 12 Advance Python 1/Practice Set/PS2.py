'''
Q2 -> Write a program to print third, fifth and seventh element from a list using enumerate function.

'''

list = [12,42,53,63,14,53,134,64,621]

for i, item in enumerate (list):
    if i==2 or i==4 or i==7:
        print(item)