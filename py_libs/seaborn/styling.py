import seaborn as sns
import matplotlib.pyplot as plt

# dfs = sns.get_dataset_names()
# print(dfs)

planets = sns.load_dataset('planets')
print(planets)

# styling the plot  

sns.set_style('whitegrid') # other options: dark, white, ticks, darkgrid
plt.figure(figsize=(10,6)) # setting figure size
sns.set_context('notebook', font_scale=1.2) # other options: paper, talk , poster -->( smaller, larger text, largest text )respectively
sns.set_palette('deep') # other options: deep, muted, bright, dark, colorblind
sns.scatterplot(data= planets, x='mass',y='distance',hue='year' )
# sns.despine() # removes top and right spines for a cleaner look

plt.show()