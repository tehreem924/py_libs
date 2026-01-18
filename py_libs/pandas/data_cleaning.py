import pandas as pd

# Data cleaning = The process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset.

df = pd.read_csv('tips.csv')

print("Original DataFrame:")
print(df.to_string())

# 1. drop duplicates
df = df.drop_duplicates()
print("\nDataFrame after dropping duplicates:")
print(df.to_string())

# 2. handle missing values
df = df.dropna(subset=['tip'])# drop rows where 'tip' is NaN
print(df.to_string())
df = df.fillna({'size': 'None'})# fillna = Fill NA/NaN values using the specified method
print("\nDataFrame after handling missing values:")
print(df.to_string())

# 3. fix inconsistent values
df['day'] = df['day'].replace({'Thur': 'Thu'}) # standardize 'Thur' to 'Thu'
df['day'] = df['day'].str.lower() # capitalize first letter
print(df.to_string())

# 4. correct data types
df['total_bill'] = pd.to_numeric(df['total_bill'], errors='coerce') # convert to numeric, set errors to NaN
df['smoker'] = df['smoker'].map({'Yes': True, 'No': False}) # convert to boolean

print(df.to_string())
