import pandas as pd

# Read the CSV file
df = pd.read_csv('C:/งานโอม/cpe203 stat/Tips/archive/tips.csv')

# Define the columns where you want to detect outliers
columns_to_check = ['total_bill', 'tip', 'size']

# Define a function to detect outliers using the IQR method
def detect_outliers_iqr(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = (data < lower_bound) | (data > upper_bound)
    return outliers

# Loop through each column and print the rows that contain outliers
for column in columns_to_check:
    outliers = detect_outliers_iqr(df[column])
    print(f"Outliers in column '{column}':")
    print(df[outliers])
