'''
ndim -> means number of dimensions of the array.
For example, a 2D array has 2 dimensions (rows and columns).
'''

import numpy as np

arr1 = np.array([12, 23, 31])
arr2 = np.array([[12, 23, 31], [54, 56, 68]])
arr3 = np.array([[[12, 23, 31], [54, 56, 68], [72, 85, 98]]])

print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)