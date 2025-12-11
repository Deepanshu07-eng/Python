import pandas as pd

data = {
    "Name": ['Rahul', 'Sonia', 'Yash', 'Drishti', 'Piyush', 'Deepanshu', 'Ankita', 'Karan', 'Simran', 'Amit', 'Neha', 'Rohan', 'Pooja'],
    "Age" : [23, 24, 22, 21, 25, 23, 24, 22, 26, 21, 27,None,23],
    "City" : ['Pune', 'Mumbai', 'Bangalore', None,'Delhi', 'Chennai', 'Kolkata', 'Hyderabad', 'Ahmedabad', 'Jaipur', 'Lucknow', 'Surat', 'Indore'],
    "Salary": [50000, 60000,55000, 52000, 58000, 62000, 59000,None, 61000, 63000, 54000, 65000, 57000],
    "Performance score": [85, 90, 88, 82, 87, 91, 89,None, 86, 92, 84, 93, 83]
}

df = pd.DataFrame(data)
print(df)

#interpolation Methods:
# 1: Linear (default)
# 2: Time
# 3: Polynomial

df.interpolate(method="Linear", axis=0, inplace=True)
print(df)