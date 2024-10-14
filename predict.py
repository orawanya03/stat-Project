import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the data
data = pd.read_csv('C:/งานโอม/cpe203 stat/Tips/archive/tips.csv')

# Drop columns 'sex', 'smoker', 'day', and 'time'
data.drop(['sex', 'smoker', 'day', 'time'], axis=1, inplace=True)

# Split the data into features (X) and target variable (y)
X = data[['total_bill', 'size']]
y = data['tip']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print("Training R-squared:", train_score)
print("Testing R-squared:", test_score)

# Make predictions
# Example new data with input features
# total_bill = 50.0, size = 6
new_data = pd.DataFrame({'total_bill': [50.0], 'size': [1]})
predicted_tip = model.predict(new_data)
print("Predicted tip amount:", predicted_tip)
