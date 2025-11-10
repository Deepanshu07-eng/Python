#Fancy Indexing

import numpy as np

arr = np.array([10,20,30,40,50])

print(arr[[0,3,4]]) #elements at index 0,3,4

# Boolean Masking

print(arr[arr> 25])