import seaborn as sns
import matplotlib.pyplot as plt

# FacetGrid = Split the dataset by category and plot each subset side by side

tips = sns.load_dataset("tips")

# Create FacetGrid
g = sns.FacetGrid(tips, col="sex", row="time")

# Map a plot type onto the grid
g.map(sns.scatterplot, "total_bill", "tip")
plt.show()

# Histogram of tips by day
g = sns.FacetGrid(tips, col="day")
g.map(sns.histplot, "tip")
plt.show()

# Scatterplot with hue
g = sns.FacetGrid(tips, col="day", hue="sex")
g.map(sns.scatterplot, "total_bill", "tip")
g.add_legend()
plt.show()