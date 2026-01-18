import seaborn as sns
import matplotlib.pyplot as plt 

iris = sns.load_dataset('iris')
print(iris) 

# Example 3 of distribution plot: 
# KDE plot = kernel density estimate plot --> smooth curve showing data distribution 

# compulsory arguments: data=dataset, x=column name to plot
sns.kdeplot(data=iris, x='sepal_width', hue='species', fill=True, alpha=0.5)# fill=True fills the area under the curve, alpha=transparency level
plt.title('KDE of Sepal Width by Species')          
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Density')
plt.show()