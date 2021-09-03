import datetime
import re



date = str(datetime.date.today())
date = '年 年 9月'
p = r'年 年 (.*)月'
this_month = re.search(p, date).group(1)
this_month = this_month.strip('0')
print(this_month)
print('a')