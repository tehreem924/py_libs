import seaborn as sns
import matplotlib.pyplot as  plt

tips= sns.load_dataset('tips')

plt.figure(figsize=(8,6))
sns.set_style("whitegrid")
sns.set_context('talk')
sns.swarmplot(x='day',y='tip',data=tips,hue='sex',dodge=True,palette='afmhot')
plt.legend(loc=0)
plt.show()