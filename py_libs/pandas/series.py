import pandas as pd

# series = A one-dimensional labeled array capable of holding any data type
data = [100,200,300,400,450]

series = pd.Series(data)
print(series)

series = pd.Series(data, index=['A', 'B', 'C','D','E'])
print(series)
print(series.loc['A'])# Access by label
print(series.iloc[2])# Access by position
print(series[series>=300])# filtering


calories = {'day1': 420, 'day2': 380, 'day3': 390}
calories['day4'] = 450
series = pd.Series(calories)    
series['day5'] = 500
series.loc['day6'] = 600
print(series)
print(series.loc['day1'])# Access by label
print(series[series>=450])
