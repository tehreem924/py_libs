import pandas as pd

#filtering = Selecting data based on conditions
df = pd.read_csv('tips.csv')
print(df)
# filtering rows based on condition
print(df[df['total_bill']>40].to_string()) 

# filtering with logical operators
high_bill_and_large_size = df[(df['total_bill'] > 40) & (df['size'] >= 4)]
print(high_bill_and_large_size.to_string())