import pandas as pd



data = {
    "Name": ['Rahul', 'Sonia', 'Yash', 'Drishti', 'Deepanshu', 'Ankita', 'Karan', 'Simran', 'Amit', 'Neha', 'Rohan', 'Pooja'],
    "Age" : [23, 24, 22, 21, 25, 23, 24, 22, 26, 21, 27, 23],
    "City" : ['Pune', 'Mumbai', 'Bangalore', 'Delhi', 'Chennai', 'Kolkata', 'Hyderabad', 'Ahmedabad', 'Jaipur', 'Lucknow', 'Surat', 'Indore'],
    "Salary": [50000, 60000, 55000, 52000, 58000, 62000, 59000, 61000, 63000, 54000, 65000, 57000],
    "Performance score": [85, 90, 88, 82, 87, 91, 89, 86, 92, 84, 93, 83]
}

df = pd.DataFrame(data)
print(df)

# .loc[] method->  to update value ( Kisi bhi specific cell ko excess kr skte h or update kar skte hai)
# df.loc[row_index, 'Column_name'] = new_value 

df.loc[0, "Salary"] = 52000
df.loc[3, "City"] = "Noida"

print(df)