import seaborn as sns
import matplotlib.pyplot as plt

# Clustermap = Heatmap + clustering	,it Groups similar rows/columns
 
# Example dataset
iris = sns.load_dataset("iris")
print(iris)
species = iris.pop('species')
sns.clustermap(iris)
plt.show()
