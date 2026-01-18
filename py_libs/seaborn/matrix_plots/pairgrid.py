import seaborn as sns
import matplotlib.pyplot as plt

# PairGrid is a flexible matrix of subplots for visualizing pairwise relationships between multiple variables.
    
# Load dataset
iris = sns.load_dataset("iris")

# Initialize PairGrid
g = sns.PairGrid(iris)

# Map plots
g.map_diag(sns.histplot)        # Diagonal: histograms
g.map_upper(sns.scatterplot)    # Upper triangle: scatterplots
g.map_lower(sns.kdeplot)        # Lower triangle: density plots

plt.show()

g = sns.PairGrid(iris, hue="species")
g.map_diag(sns.histplot)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot, fill=True)
g.add_legend()
plt.show()
