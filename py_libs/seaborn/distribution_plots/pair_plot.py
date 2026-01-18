import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
print(iris)

# Example 4 of distribution plot: 
# pair plot = matrix of scatter plots for all variable / numerical columns in the dataset


# compulsory arguments: data=dataset
sns.pairplot(data=iris, hue='species', diag_kind='kde')# diag_kind can be 'hist' or 'kde' , it gives distribution plots on the diagonal
plt.suptitle('Pair Plot of Iris Dataset', y=1.02)
plt.show()