import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Heatmap = Color-coded values, used for Correlations, pivot tables

crashes = sns.load_dataset('car_crashes')

# Select only numeric columns
# Correlation matrix
corr = crashes.select_dtypes(include=['float64', 'int64']).corr()

# # One-hot encode categorical columns (like 'abbrev')
# crashes_encoded = pd.get_dummies(crashes, drop_first=True)
# # Correlation matrix
# corr = crashes_encoded.corr()

# Heatmap
sns.heatmap(corr, annot=True, cmap="viridis", linewidths=0.5)
plt.tight_layout()
plt.show()


#  pivot table = summarize data by grouping and aggregating values.

tips = sns.load_dataset("tips")
# Pivot table: average tip by day and gender
pivot = pd.pivot_table( tips, values="tip", index="day", columns="sex", aggfunc="mean" )
sns.heatmap(pivot, annot=True, cmap="viridis", linewidths=0.5)
plt.tight_layout()
plt.show()