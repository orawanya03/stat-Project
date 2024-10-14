import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('C:/งานโอม/cpe203 stat/Tips/archive/tips.csv')

# Create the scatterplot with trend line
plt.figure(figsize=(10, 6))
sns.regplot(x='total_bill', y='tip', data=data)
plt.title('Scatterplot of Tip Amount by Total Bill with Trend Line')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()
