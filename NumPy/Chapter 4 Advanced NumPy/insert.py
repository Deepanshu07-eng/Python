"""
np.insert(array, index, value, axis=None)
array = Prigional array
index = Index before which values are inserted
value = Values to insert into array
axis = Axis along which to insert values. If axis is not given, array is flattened first

axis =0, row-wise
axis =1, column wise
"""

import numpy as np

arr = np.array([10,20,30,40,50])
new_arr = np.insert(arr,3, 100)
print(new_arr)


