"""
array[index]  #1d array
array[row, column] #2d array

"""


import numpy as np

arr = np.array([10,20,30,40,50])

print(arr[0]) #first element
print(arr[2]) #third element
print(arr[-1])  #last element

'''
If i do -> print(arr[10]) it raises an IndexError because index 10 is out of bounds for array of size 5.
'''