import datetime
import re



date = str(datetime.date.today())
date = '2021-10-9'
p = r'-(.*)-'
this_month = re.search(p, date).group(1)
this_month = this_month.strip('0')
print(this_month)