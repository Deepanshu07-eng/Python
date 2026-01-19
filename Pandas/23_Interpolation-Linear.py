import pandas as pd

data={
    "Time": [1,2,3,4,5],
    "Value": [10, None, 30, None, 50]
}

df = pd.DataFrame(data)
print('Before interpolations')
print(df)

df['Value'] = df['Value'].interpolate(method="linear")
print('After interpolation')
print(df)


'''
When to use Interpolation:
    1- Timer series data with missing values
    2- Numeric data with missing values where trend is to be maintained
    3- avoid droping rows/columns with missing values
    
'''
