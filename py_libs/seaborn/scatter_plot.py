import seaborn as sns
import matplotlib.pyplot as plt


ds = sns.get_dataset_names()  # to see available datasets in seaborn
print(ds)

penguins = sns.load_dataset('penguins')
print(penguins)

sns.scatterplot(data=penguins, x='flipper_length_mm', y='bill_length_mm', hue='species')# hue adds color based on species
plt.show() 

# Additional example: scatter plot with size variation
sns.scatterplot(data=penguins, x='flipper_length_mm', y='bill_length_mm', size='body_mass_g', hue='species', sizes=(20, 200))# sizes(20,200) gives size range for points from 20 to 200 
plt.show()