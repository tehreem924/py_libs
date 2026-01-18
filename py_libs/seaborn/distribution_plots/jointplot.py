import seaborn as sns
import matplotlib.pyplot as plt 


diamonds = sns.load_dataset('diamonds')
print(diamonds)

# Example 2 of distribution plot: 
# joint plot = combination of scatter plot and histograms/KDE plots

# compulsory arguments: data=dataset, x=column name for x-axis, y=column name for y-axis
sns.jointplot(data=diamonds,x='carat', y='price',kind='scatter',hue='cut', height=8)# kind can be 'scatter', 'kde', 'hex', etc.
plt.suptitle('Joint Plot of Carat vs Price', y=0.99) # y=1.02 to adjust title position, suptitle --> title for the entire figure
plt.tight_layout()
plt.show()