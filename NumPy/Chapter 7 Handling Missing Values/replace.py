# np.isinf(array)  10^1000, 1/0

import numpy as np

arr = np.array([10,20,np.inf, 40, 50, np.inf])

print(np.isinf(arr))

cleaned_arr = np.nan_tonum(arr, posinf = 1000, neginf = -1000)

print(cleaned_arr)