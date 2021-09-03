import datetime
import re



date = str(datetime.date.today())
p = r'-(.*)-'
this_month = re.search(p, date).group(1)
print(this_month)