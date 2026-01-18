import pandas as pd

df = pd.read_csv('tips.csv')
print(df) # show truncated output(first & last 5 rows)
# print(df.to_string())

df = pd.read_json('tips.json')
print(df)
print(df.to_string())
