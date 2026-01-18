import pandas as pd

# aggregation = Functions that summarize data
df = pd.read_csv('tips.csv')

# Whole DataFrame
print(df.mean(numeric_only=True)) # mean of all numeric columns
print(df.sum(numeric_only = True))
print(df.min(numeric_only=True))
print(df.max(numeric_only = True))
print(df.count())

#Single Column
print(df['total_bill'].mean())
print(df['tip'].sum())
print(df['size'].min())
print(df['size'].max())
print(df['tip'].count())
#Multiple Columns
print(df[['total_bill','tip']].mean())

# groupby()
grouped = df.groupby('day')
print(grouped['total_bill'].mean())
print(grouped['tip'].sum())
print(grouped['size'].max())
print(grouped['total_bill'].count())
# multiple aggregations
print(grouped['total_bill'].agg(['mean','sum','max','min','count']))
print(grouped.agg({'total_bill':'mean','tip':'sum','size':'max'}))
