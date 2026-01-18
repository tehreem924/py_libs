import seaborn as sns
import matplotlib.pyplot as plt

# Countplot	Shows frequency of categories ,its dataType is Categorical only

# Sample dataset
tips = sns.load_dataset("tips")

# Syntax ➡️ sns.countplot(x="category", data=df)

sns.countplot(x="day",  data=tips)
plt.show()
# Count plot with hue (gender)
sns.countplot(x="day", hue="sex", data=tips, palette="pastel")
plt.show()