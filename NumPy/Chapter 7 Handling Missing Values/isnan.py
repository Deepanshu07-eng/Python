#np.isnan(array)

import numpy as np

arr = np.array([10, np.nan, 30 ,40 , np.nan, 60])

print(np.isnan(arr))

# print(np.nan == np.nan)  # False because NaN is not equal to anything, including itself
# we cannt compare NaN with anything