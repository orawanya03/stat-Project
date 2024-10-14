import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('C:/งานโอม/cpe203 stat/Tips/archive/clean.csv')

# Create the boxplot with size as a factor
plt.figure(figsize=(10, 6))
sns.boxplot(x='size', y='tip', data=data)
plt.title('Boxplot of Tips by Size')
plt.xlabel('Size')
plt.ylabel('Tip')
plt.show()
