list = [ 2, 5, 4, 6, 3 ]

'''
squaredList= []
for item in list:
    squaredList.append(item*item)
'''

#Using List Comprehensions

squaredList = [i*i for i in list]


print(squaredList)
