#np.nan_to_num(array, nan =value ) default = 0

import numpy as np

arr = np.array([10, np.nan, 30 ,40 , np.nan, 60])

cleaned_arr = np.nan_to_num(arr, nan =1000) #default zero

print(cleaned_arr)