"""
vertically
Horizontally

vstack() row wise
hstack() column wise

"""

import numpy as np

arr1 = np.array([10,20,30,40])
arr2 = np.array([50,60,70,80])

print(np.vstack((arr1, arr2))) # vertical stack
print(np.hstack((arr1, arr2))) # horizontal stack