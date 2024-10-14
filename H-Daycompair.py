import pandas as pd
from scipy.stats import ttest_ind

# ขั้นที่ 1: นำเข้าไลบรารีที่จำเป็น
import pandas as pd
from scipy.stats import ttest_ind

# ขั้นที่ 2: โหลดข้อมูล
data = pd.read_csv('C:/งานโอม/cpe203 stat/Tips/archive/tips.csv')

# ขั้นที่ 3: แปลงข้อมูล 'day' เป็นตัวเลข
data['day'] = data['day'].map({'Sun': 1, 'Mon': 2, 'Tue': 3, 'Wed': 4, 'Thu': 5, 'Fri': 6, 'Sat': 7})

# ขั้นที่ 4: แบ่งข้อมูลตามวันของสัปดาห์
sunday_tips = data[data['day'] == 1]['tip']
saturday_tips = data[data['day'] == 7]['tip']

# ขั้นที่ 5: ทดสอบสมมติฐานด้วย t-test
t_statistic, p_value = ttest_ind(sunday_tips, saturday_tips)

# ขั้นที่ 6: ตัดสินใจ
if p_value < 0.05:
    print("สรุป: มีความแตกต่างที่มีนัยสำคัญในการให้ทิปในวันหยุดสุดสัปดาห์")
else:
    print("สรุป: ไม่มีหลักฐานเพียงพอที่จะสรุปว่ามีความแตกต่างที่มีนัยสำคัญในการให้ทิปในวันหยุดสุดสัปดาห์")

# แสดงค่า p-value
print("p-value:", p_value)
