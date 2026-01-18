import pandas as pd

# df = pd.read_csv('tips.csv', index_col='size')# index (optional)
df = pd.read_csv('tips.csv')

print(df)
print(df) # show truncated output(first & last 5 rows)

#selection by column name
print(df['total_bill'])
print(df[['total_bill','tip']].to_string())
#selection by row index
print(df.iloc[0])# first row
print(df.iloc[0:3])# first three rows
print(df.iloc[0:3,0:2])# first three rows and first two columns
#selection by row and column labels
print(df.loc[0:2,['total_bill','tip']])# first three rows and specific columns
# filtering rows based on condition
print(df[df['total_bill']>20]) 

bill = input("Enter bill: ")
try:
    print(df.loc[df['total_bill'] == float(bill)])

except KeyError:
    print("{bill} not found in the dataset.")