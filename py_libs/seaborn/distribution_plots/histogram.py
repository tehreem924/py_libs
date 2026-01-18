import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
print(iris)

# Example 1 of distribution plot: 
# histogram shows frequency distribution of a single variable (numerical) using bars 

# compulsory arguments: data=dataset, x=column name to plot
sns.histplot(data=iris, x='sepal_length', bins=10, kde=True)# bins = number of bars, kde = kernel density estimate --> smooth curve
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()


