import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


penguins = sns.load_dataset('penguins')
print(penguins)

# categorical plot: bar plot= used to display the relationship between a categorical variable and a numerical variable using rectangular bars
# compulsory arguments: data = dataset, x = categorical column, y = numerical column

# simple example

sns.barplot(data=penguins, x='species', y='flipper_length_mm', hue='island', estimator=np.mean)# estimator argument defines the statistical function used to aggregate data.
plt.title('Average Flipper Length by Species and Island')   
plt.show()