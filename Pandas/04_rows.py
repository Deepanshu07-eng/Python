# head() #tail()
#head(n), head() = 5 rows
#rail(n), tail() = 5 rows

import pandas as pd
df = pd.read_csv("customers-1000.csv")

print('Displaying first 10 rows of the dataframe')
print(df.head(10))

print('\nDisplaying last 10 rows of the dataframe')
print(df.tail(10))


