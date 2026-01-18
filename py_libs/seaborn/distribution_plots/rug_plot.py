import seaborn as sns
import matplotlib.pyplot as plt


crashes = sns.load_dataset('car_crashes')
print(crashes)

# Example 5 of distribution plot: 
# rug plot = small vertical lines along x-axis showing individual data points distribution


# compulsory arguments: data=dataset, x=column name to plot
sns.rugplot(data=crashes, x='total',hue='abbrev', height=0.5, alpha=0.7)# height controls the height of the rug lines, alpha controls transparency
plt.title('Rug Plot of Total Car Crashes by State')
plt.xlabel('Total Car Crashes per 1B miles')
plt.ylabel('Density')
plt.show()