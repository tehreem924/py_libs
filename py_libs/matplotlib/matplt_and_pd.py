import matplotlib.pyplot as plt
import pandas as pd

# Creating a sample DataFrame
df = pd.read_csv('tips.csv')
print(df)

# Plotting using DataFrame's plot method
df.plot(x='total_bill', y='tip', kind='scatter', color='blue', title='Total Bill vs Tip')
plt.xlabel('Total Bill')    
plt.ylabel('Tip')
plt.tight_layout()
plt.show()

# Alternative way using matplotlib directly
plt.scatter(df['total_bill'], df['tip'], color='blue')
plt.title('Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()

## bar-chart using DataFrame
# df_grouped = df.groupby('day').size()# size() --> counts number of occurrences in each group
# df_grouped.plot(kind='bar', color='orange', title='Number of Bills per Day')
# plt.xlabel('Day')
# plt.ylabel('Number of Bills')
# plt.tight_layout()
# plt.show()

# Alternative way using matplotlib directly
days = df['day'].value_counts().index
counts = df['day'].value_counts().values
plt.bar(days, counts, color='orange')
plt.title('Number of Bills per Day')
plt.xlabel('Day')
plt.ylabel('Number of Bills')
plt.show()