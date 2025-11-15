import pandas as pd

# read data from CSV file into a dataframe

df = pd.read_csv("customers-1000.csv")  #use encoding = "latin1" if needed for special characters or error in terminal

print(df)

# read excel data set

df = pd.read_excel("superstore.xls" )

print(df)