import pandas as pd
from scipy import stats

# Load the data
data = pd.read_csv('C:/งานโอม/cpe203 stat/Tips/archive/clean.csv')

# Separate data into two groups based on total_bill (e.g., high_total_bill and low_total_bill)
high_total_bill = data[data['total_bill'] >= data['total_bill'].median()]
low_total_bill = data[data['total_bill'] < data['total_bill'].median()]

# Perform t-test
t_statistic, p_value = stats.ttest_ind(high_total_bill['tip'], low_total_bill['tip'])

# Decide based on p-value
alpha = 0.05
print("p_value = ",p_value)
if p_value < alpha:
    print("สมมติฐาน 'total_bill ที่มากมีแนวโน้มที่จะให้ทิปมากขึ้น' เป็นจริง")
else:
    print("สมมติฐาน 'total_bill ที่มากมีแนวโน้มที่จะให้ทิปมากขึ้น' เป็นเท็จ")
