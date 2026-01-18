import seaborn as sns
import matplotlib.pyplot as plt

# Boxplot = Shows statistical distribution (median, quartiles, outliers) ,its dataType is( Categorical + numerical)
# Median → Q2 = The line inside the box.
# Interquartile Range (IQR) → (Q3-Q2) → The box itself (from Q1=25%values to Q3=75% values).
# Whiskers → Extend to show variability outside the upper and lower quartiles.
# Outliers → Individual points plotted beyond the whiskers.

tips= sns.load_dataset('tips')

sns.boxplot(x="day", y="tip", data=tips, hue='sex')
# plt.legend(loc=0)
plt.show()
