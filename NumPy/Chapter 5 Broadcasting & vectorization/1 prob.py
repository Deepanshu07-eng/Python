prices = [1000,2000,3000] #in rupees

discout = 10

final_prices = []

for price in prices:
    final_price = price - (price * discout / 100)
    final_prices.append(final_price)    

print("Final prices after discount:", final_prices)