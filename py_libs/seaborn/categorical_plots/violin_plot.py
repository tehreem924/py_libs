import seaborn as sns
import matplotlib.pyplot as plt

# Violinplot = Boxplot + KDE distribution, its good for	Understanding shape of distribution

# Sample dataset
tips = sns.load_dataset("tips")

# Syntax ➡️ sns.violinplot(x="category", y="numeric_column", data=df)
sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', palette='Set2', split=True)
plt.show()