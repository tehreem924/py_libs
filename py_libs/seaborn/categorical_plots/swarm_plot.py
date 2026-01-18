import seaborn as sns
import matplotlib.pyplot as plt

# swarmplot = Raw data points, Points never overlap (auto-adjusted)
# Often combined with boxplots or violinplots

tips = sns.load_dataset("tips")
# Syntax ➡️ sns.stripplot(x="category", y="numeric_column", data=df)

# Basic swarmplot
# sns.violinplot(x="day", y="total_bill", data=tips)
# sns.swarmplot(x="day", y="total_bill", data=tips)

# With hue (gender)
sns.swarmplot(x="day", y="total_bill", hue="sex", data=tips, palette="pastel", dodge=True)
plt.legend(loc=0)
plt.show()
