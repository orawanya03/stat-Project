import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('C:/งานโอม/cpe203 stat/Tips/archive/clean.csv')

# Map the day names to numeric values for better visualization
day_order = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
data['day'] = pd.Categorical(data['day'], categories=day_order, ordered=True)

# Create the boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='day', y='tip', data=data)
plt.title('Boxplot of Tips by Day')
plt.xlabel('Day')
plt.ylabel('Tip')
plt.show()
