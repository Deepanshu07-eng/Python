import pandas as pd



data = {
    "Name": ['Rahul', 'Sonia', 'Yash', 'Drishti', 'Deepanshu', 'Ankita', 'Karan', 'Simran', 'Amit', 'Neha', 'Rohan', 'Pooja'],
    "Age" : [23, 24, 22, 21, 25, 23, 24, 22, 26, 21, 27, 23],
    "City" : ['Pune', 'Mumbai', 'Bangalore', 'Delhi', 'Chennai', 'Kolkata', 'Hyderabad', 'Ahmedabad', 'Jaipur', 'Lucknow', 'Surat', 'Indore'],
    "Salary": [50000, 60000, 55000, 52000, 58000, 62000, 59000, 61000, 63000, 54000, 65000, 57000],
    "Performance score": [85, 90, 88, 82, 87, 91, 89, 86, 92, 84, 93, 83]
}

df = pd.DataFrame(data)

high_salary = df[df['Salary'] > 60000]
print('Employees with salary greater than 60000')
print(high_salary)

# filtering rows salary > 50k  and age > 25

filtered_data = df[(df['Age']> 25) & (df["Salary"] > 50000)]
print('\nEmployees with age greater than 25 and salary greater than 50000')
print(filtered_data)