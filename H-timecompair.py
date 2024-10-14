import pandas as pd
from scipy.stats import ttest_ind

# ขั้นที่ 1: นำเข้าไลบรารีที่จำเป็น
import pandas as pd
from scipy.stats import ttest_ind

# ขั้นที่ 2: โหลดข้อมูล
data = pd.read_csv('C:/งานโอม/cpe203 stat/Tips/archive/tips.csv')

# ขั้นที่ 3: แปลงข้อมูลเวลาเป็นตัวเลข (1=เที่ยง, 2=เย็น)
data['time'] = data['time'].map({'Lunch': 1, 'Dinner': 2})

# ขั้นที่ 4: แบ่งข้อมูลเป็นกลุ่มตามเวลา
lunch_tips = data[data['time'] == 1]['tip']
dinner_tips = data[data['time'] == 2]['tip']

# ขั้นที่ 5: ทดสอบสมมติฐานด้วย t-test
t_statistic, p_value = ttest_ind(lunch_tips, dinner_tips)

# ขั้นที่ 6: ตัดสินใจ
if p_value < 0.05:
    print("สรุป: มีความแตกต่างที่มีนัยสำคัญในการให้ทิประหว่างกลุ่มเวลาเที่ยงและเย็น")
else:
    print("สรุป: ไม่มีหลักฐานเพียงพอที่จะสรุปว่ามีความแตกต่างที่มีนัยสำคัญในการให้ทิประหว่างกลุ่มเวลาเที่ยงและเย็น")

# แสดงค่า p-value
print("p-value:", p_value)
