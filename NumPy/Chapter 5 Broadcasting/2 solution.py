"""
Using broadcasting, we can reduce time and space complexity when performing operations on arrays of different shapes.

"""
import numpy as np

prices = np.array([1000,2000,3000,4000, 5000, 6000]) #in rupees
discount = 10

final_prices = prices - (prices * discount / 100)

print(final_prices)