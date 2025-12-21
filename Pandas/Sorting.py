# SORTING DATA

# Sorting data in 1 Column

import pandas as pd

# Single Value -> df.sort_values(by="", ascending=True, inplace=True)
# Multiple Values -> df.sort_values(by=["", ""], ascending=[True, False], inplace=True)
data ={
    "Name": ['Rahul', 'Sonia', 'Yash', 'Drishti', 'Piyush', 'Deepanshu', 'Ankita', 'Karan', 'Simran', 'Amit', 'Neha', 'Rohan', 'Pooja'],
    "Age" : [23, 24, 22, 21, 25, 23, 24, 22, 26, 21, 27, 23, 23],
    "City" : ['Pune', 'Mumbai', 'Bangalore', 'Delhi', 'Chennai', 'Kolkata', 'Hyderabad', 'Ahmedabad', 'Jaipur', 'Lucknow', 'Surat', 'Indore', 'Patna'],
    "Salary": [50000, 60000,55000, 52000, 58000, 62000, 59000, 61000, 63000, 54000, 65000, 57000, 56000],
    "Performance score": [85, 90, 88, 82, 87, 91, 89, 86, 92, 84, 93, 83, 80]
}

df = pd.DataFrame(data)
df.sort_values(by="Age", ascending=True, inplace=True)  #Sorting age by ascending order
print(df)


# Sorting data in Multiple Columns
df.sort_values(by=["Age", "Salary"], ascending=False, inplace=True)  #Sorting age and salary by descending order
print(df)