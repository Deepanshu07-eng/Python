import pandas as pd

data = {
    "Name": ['Rahul', 'Sonia', 'Yash', 'Drishti', 'Deepanshu', 'Ankita', 'Karan', 'Simran', 'Amit', 'Neha', 'Rohan', 'Pooja'],
    "Age" : [23, 24, 22, 21, 25, 23, 24, 22, 26, 21, 27, 23],
    "City" : ['Pune', 'Mumbai', 'Bangalore', 'Delhi', 'Chennai', 'Kolkata', 'Hyderabad', 'Ahmedabad', 'Jaipur', 'Lucknow', 'Surat', 'Indore'],
    "Salary": [50000, 60000, 55000, 52000, 58000, 62000, 59000, 61000, 63000, 54000, 65000, 57000],
    "Performance score": [85, 90, 88, 82, 87, 91, 89, 86, 92, 84, 93, 83]
}

df = pd.DataFrame(data)

#display the dataframe
print("Sample DataFrame")
print(df)

print("Names (Single columns return series)")
name = df['Name']
print(name)


#Selecting Multiple Columns

subset = df[['Name', 'Age', 'City']]
print("\nSubset with name, age and city columns")
print(subset)