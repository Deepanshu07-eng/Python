import numpy as np

arr_2d= np.array([[10,20,30],[40,50,60]])

new_arr_2d= np.delete(arr_2d, 0, axis=0)  # Delete the first row
print(new_arr_2d)