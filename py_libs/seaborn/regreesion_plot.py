import seaborn as sns
import matplotlib.pyplot as plt

# regression = visualize the relationship between two variables along with a fitted regression line
 
penguins = sns.load_dataset('penguins')
 
#lmplot = linear model plot , it fits and plots a regression line
sns.lmplot(data=penguins, x='flipper_length_mm', y='bill_length_mm', hue='species', height=6, aspect=1.5)# aspect controls the width/height ratio
plt.show()
 
 
# Load dataset
tips = sns.load_dataset("tips")

sns.lmplot(x="total_bill", y="tip", hue="sex", data=tips, aspect=1.5, height=5)
plt.title("Regression Plot with Hue - Total Bill vs Tip")
plt.show()