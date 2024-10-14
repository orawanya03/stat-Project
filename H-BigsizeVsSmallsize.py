import pandas as pd
from scipy import stats

# ขั้นที่ 2: โหลดข้อมูล
data = pd.read_csv('C:/งานโอม/cpe203 stat/Tips/archive/clean.csv') 
# ขั้นที่ 3: ทำการแปลงตัวแปรตามที่ต้องการ
data['total_bill'] = data['total_bill'].astype(float)
data['tip'] = data['tip'].astype(float)
data['sex'] = data['sex'].map({'M': 1, 'F': 0})  # แปลงเพศเป็นตัวเลข (ชาย = 1, หญิง = 0)
data['smoker'] = data['smoker'].map({'Yes': 1, 'No': 0})  # แปลงการสูบบุหรี่เป็นตัวเลข (สูบ = 1, ไม่สูบ = 0)
data['day'] = data['day'].map({'Sun': 1, 'Mon': 2, 'Tue': 3, 'Wed': 4, 'Thu': 5, 'Fri': 6, 'Sat': 7})  # แปลงวันให้เป็นตัวเลข

# ขั้นที่ 4: แบ่งกลุ่มข้อมูล
group1 = data[data['size'] >= 3]  # กลุ่มใหญ่
group2 = data[data['size'] < 3]   # กลุ่มเล็ก

# ขั้นที่ 5: ทดสอบสมมติฐาน
t_statistic, p_value = stats.ttest_ind(group1['tip'], group2['tip'])
print("p-value =", p_value)
print("t-test =", t_statistic)
# ขั้นที่ 6: ตัดสินใจ
if p_value < 0.05:
    print("สรุป: กลุ่มใหญ่มีแนวโน้มที่จะให้ทิปมากขึ้น")
else:
    print("สรุป: ไม่มีหลักฐานเพียงพอที่จะสรุปว่ากลุ่มใหญ่มีแนวโน้มที่จะให้ทิปมากขึ้น")
