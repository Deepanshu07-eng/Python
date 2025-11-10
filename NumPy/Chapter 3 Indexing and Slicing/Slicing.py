"""
Slicing
*Start
*Stop
*Step

array[start:stop:step]

arr[start:end],  Start to end-1

negative step, -1 reverse


"""
import numpy as np

arr = np.array([10,20,30,40,50])

print(arr[1:4]) #from index 1 to index 3
print(arr[1:5:3]) #from index 1 to index 4 with step 3
print(arr[::-1]) #reverse the array
print(arr[4:1:-1]) #from index 4 to index 2 in reverse order
print(arr[:4])#from start to index 3
print(arr[::2]) #from start to end with step 2