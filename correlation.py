import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the data
data = pd.read_csv('C:/งานโอม/cpe203 stat/Tips/archive/tips.csv')

# Encode categorical variables
label_encoder = LabelEncoder()
data['sex'] = label_encoder.fit_transform(data['sex'])
data['smoker'] = label_encoder.fit_transform(data['smoker'])
data['day'] = label_encoder.fit_transform(data['day'])
data['time'] = label_encoder.fit_transform(data['time'])

# Calculate the correlation matrix
correlation_matrix = data[['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']].corr()

# Print the correlation matrix
print(correlation_matrix)

# Extract the correlation between tip and other variables
tip_correlation = correlation_matrix['tip']

# Print the correlation between tip and other variables
print("Correlation with tip:")
print(tip_correlation)
