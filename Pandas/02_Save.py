import pandas as pd

data = {
    "Name": ['rahul', 'sonia', 'yash'],
    "Age" : [23, 24, 22],
    "City" : ['pune', 'mumbai', 'bangalore']

}

df = pd.DataFrame(data)
print(df)

#df.to_csv("output.csv", index= False)
df.to_excel("output.xlsx", index= False)