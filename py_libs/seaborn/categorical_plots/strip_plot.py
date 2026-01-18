import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# stripplot	=Raw data points, Points may overlap (use jitter)

# Syntax ➡️ sns.stripplot(x="category", y="numeric_column", data=df)

# Basic stripplot
# sns.stripplot(x="day", y="total_bill", data=tips)

# With jitter to avoid overlap
# sns.stripplot(x="day", y="total_bill", data=tips, jitter=True, palette="Set2")

# With hue (gender)
sns.stripplot(x="day", y="total_bill", hue="sex", data=tips, dodge=True, palette="pastel")
plt.legend(loc=0)
plt.show()
